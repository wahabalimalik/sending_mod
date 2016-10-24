# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class comparative_wealth(models.Model):
	_name                             = 'comparative.wealth'
	_inherit                          = ['mail.thread', 'ir.needaction_mixin']
	name                              = fields.Many2one('res.partner','Client Name', required=True)
	# _defaults                         = { 'name': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'comparative.wealth'), }
	# name                              = fields.Char(string="Name")
	all_years                         = fields.Boolean(string="All Years", default=False)
	group                             = fields.Many2one('res.partner')

	wealth_assets_id                  = fields.One2many('wealth.assets', 'assets_id')
	wealth_assets_ids                 = fields.One2many('wealth.assets', 'assets_id')
	wealth_liability_id               = fields.One2many('wealth.liability', 'liability_id')
	wealth_liability_ids              = fields.One2many('wealth.liability', 'liability_id')
	wealth_reconciliation_opening_id  = fields.One2many('wealth.reconciliation.open', 'wealth_open_id')
	wealth_reconciliation_opening_ids = fields.One2many('wealth.reconciliation.open', 'wealth_open_id')	
	wealth_reconciliation_income_id   = fields.One2many('wealth.reconciliation.income', 'wealth_income_id')
	wealth_reconciliation_income_ids  = fields.One2many('wealth.reconciliation.income', 'wealth_income_id')
	wealth_reconciliation_expense_id  = fields.One2many('wealth.reconciliation.expense', 'wealth_expense_id')
	wealth_reconciliation_expense_ids = fields.One2many('wealth.reconciliation.expense', 'wealth_expense_id')
	cash_opening_id                   = fields.One2many('opening', 'opening_id')
	cash_opening_ids                  = fields.One2many('opening', 'opening_id')
	cash_receipts_id                  = fields.One2many('receipts', 'receipts_id')
	cash_receipts_ids                 = fields.One2many('receipts', 'receipts_id')
	cash_payments_id                  = fields.One2many('payments', 'payments_id')
	cash_payments_ids                 = fields.One2many('payments', 'payments_id')
	cash_reconciliation_balance_id    = fields.One2many('reconciliation.balance', 'reconciliation_balance_id')
	cash_reconciliation_balance_ids   = fields.One2many('reconciliation.balance', 'reconciliation_balance_id')
	cash_closing_1_id                 = fields.One2many('closing_1.closing_1', 'closing_1_id')
	cash_closing_1_ids                = fields.One2many('closing_1.closing_1', 'closing_1_id')
	cash_closing_2_id                 = fields.One2many('closing_2.closing_2', 'closing_2_id')
	cash_closing_2_ids                = fields.One2many('closing_2.closing_2', 'closing_2_id')


	ttl_2011 = fields.Float(string="Total_2011 : " , compute="_compute_reconciliation_difference")
	ttl_2012 = fields.Float(string="Total_2012 : " , compute="_compute_reconciliation_difference")
	ttl_2013 = fields.Float(string="Total_2013 : " , compute="_compute_reconciliation_difference")
	ttl_2014 = fields.Float(string="Total_2014 : " , compute="_compute_reconciliation_difference")
	ttl_2015 = fields.Float(string="Total_2015 : " , compute="_compute_reconciliation_difference")
	ttl_2016 = fields.Float(string="Total_2016 : " , compute="_compute_reconciliation_difference")
	ttl_2017 = fields.Float(string="Total_2017 : " , compute="_compute_reconciliation_difference")
	ttl_2018 = fields.Float(string="Total_2018 : " , compute="_compute_reconciliation_difference")
	ttl_2019 = fields.Float(string="Total_2019 : " , compute="_compute_reconciliation_difference")
	ttl_2020 = fields.Float(string="Total_2020 : " , compute="_compute_reconciliation_difference")

	@api.multi
	def _compute_reconciliation_difference(self):

		self.ttl_2011 = sum(line.y2011 for line in self.cash_opening_ids) + sum(line.y2011 for line in self.cash_receipts_ids)
		self.ttl_2012 = sum(line.y2012 for line in self.cash_opening_ids) + sum(line.y2012 for line in self.cash_receipts_ids)
		self.ttl_2013 = sum(line.y2013 for line in self.cash_opening_ids) + sum(line.y2013 for line in self.cash_receipts_ids)
		self.ttl_2014 = sum(line.y2014 for line in self.cash_opening_ids) + sum(line.y2014 for line in self.cash_receipts_ids)
		self.ttl_2015 = sum(line.y2015 for line in self.cash_opening_ids) + sum(line.y2015 for line in self.cash_receipts_ids)
		self.ttl_2016 = sum(line.y2016 for line in self.cash_opening_ids) + sum(line.y2016 for line in self.cash_receipts_ids)
		self.ttl_2017 = sum(line.y2017 for line in self.cash_opening_ids) + sum(line.y2017 for line in self.cash_receipts_ids)
		self.ttl_2018 = sum(line.y2018 for line in self.cash_opening_ids) + sum(line.y2018 for line in self.cash_receipts_ids)
		self.ttl_2019 = sum(line.y2019 for line in self.cash_opening_ids) + sum(line.y2019 for line in self.cash_receipts_ids)
		self.ttl_2020 = sum(line.y2020 for line in self.cash_opening_ids) + sum(line.y2020 for line in self.cash_receipts_ids)

		self.ttl_2011 = self.ttl_2011 - sum(line.y2011 for line in self.cash_payments_ids) - sum(line.y2011 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2012 = self.ttl_2012 - sum(line.y2012 for line in self.cash_payments_ids) - sum(line.y2012 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2013 = self.ttl_2013 - sum(line.y2013 for line in self.cash_payments_ids) - sum(line.y2013 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2014 = self.ttl_2014 - sum(line.y2014 for line in self.cash_payments_ids) - sum(line.y2014 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2015 = self.ttl_2015 - sum(line.y2015 for line in self.cash_payments_ids) - sum(line.y2015 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2016 = self.ttl_2016 - sum(line.y2016 for line in self.cash_payments_ids) - sum(line.y2016 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2017 = self.ttl_2017 - sum(line.y2017 for line in self.cash_payments_ids) - sum(line.y2017 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2018 = self.ttl_2018 - sum(line.y2018 for line in self.cash_payments_ids) - sum(line.y2018 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2019 = self.ttl_2019 - sum(line.y2019 for line in self.cash_payments_ids) - sum(line.y2019 for line in self.cash_reconciliation_balance_ids) 
		self.ttl_2020 = self.ttl_2020 - sum(line.y2020 for line in self.cash_payments_ids) - sum(line.y2020 for line in self.cash_reconciliation_balance_ids) 

	total_summery_2005 = fields.Float(compute="_compute_total_line")
	total_summery_2006 = fields.Float(compute="_compute_total_line")
	total_summery_2007 = fields.Float(compute="_compute_total_line")
	total_summery_2008 = fields.Float(compute="_compute_total_line")
	total_summery_2009 = fields.Float(compute="_compute_total_line")
	total_summery_2010 = fields.Float(compute="_compute_total_line")
	total_summery_2011 = fields.Float(compute="_compute_total_line")
	total_summery_2012 = fields.Float(compute="_compute_total_line")
	total_summery_2013 = fields.Float(compute="_compute_total_line")
	total_summery_2014 = fields.Float(compute="_compute_total_line")
	total_summery_2015 = fields.Float(compute="_compute_total_line")
	total_summery_2016 = fields.Float(compute="_compute_total_line")
	total_summery_2017 = fields.Float(compute="_compute_total_line")
	total_summery_2018 = fields.Float(compute="_compute_total_line")
	total_summery_2019 = fields.Float(compute="_compute_total_line")
	total_summery_2020 = fields.Float(compute="_compute_total_line")

	total_expense_2005 = fields.Float(compute="_compute_total_line")
	total_expense_2006 = fields.Float(compute="_compute_total_line")
	total_expense_2007 = fields.Float(compute="_compute_total_line")
	total_expense_2008 = fields.Float(compute="_compute_total_line")
	total_expense_2009 = fields.Float(compute="_compute_total_line")
	total_expense_2010 = fields.Float(compute="_compute_total_line")
	total_expense_2011 = fields.Float(compute="_compute_total_line")
	total_expense_2012 = fields.Float(compute="_compute_total_line")
	total_expense_2013 = fields.Float(compute="_compute_total_line")
	total_expense_2014 = fields.Float(compute="_compute_total_line")
	total_expense_2015 = fields.Float(compute="_compute_total_line")
	total_expense_2016 = fields.Float(compute="_compute_total_line")
	total_expense_2017 = fields.Float(compute="_compute_total_line")
	total_expense_2018 = fields.Float(compute="_compute_total_line")
	total_expense_2019 = fields.Float(compute="_compute_total_line")
	total_expense_2020 = fields.Float(compute="_compute_total_line")

	total_opening_2005 = fields.Float(compute="_compute_total_line")
	total_opening_2006 = fields.Float(compute="_compute_total_line")
	total_opening_2007 = fields.Float(compute="_compute_total_line")
	total_opening_2008 = fields.Float(compute="_compute_total_line")
	total_opening_2009 = fields.Float(compute="_compute_total_line")
	total_opening_2010 = fields.Float(compute="_compute_total_line")
	total_opening_2011 = fields.Float(compute="_compute_total_line")
	total_opening_2012 = fields.Float(compute="_compute_total_line")
	total_opening_2013 = fields.Float(compute="_compute_total_line")
	total_opening_2014 = fields.Float(compute="_compute_total_line")
	total_opening_2015 = fields.Float(compute="_compute_total_line")
	total_opening_2016 = fields.Float(compute="_compute_total_line")
	total_opening_2017 = fields.Float(compute="_compute_total_line")
	total_opening_2018 = fields.Float(compute="_compute_total_line")
	total_opening_2019 = fields.Float(compute="_compute_total_line")
	total_opening_2020 = fields.Float(compute="_compute_total_line")

	total_income_2005 = fields.Float(compute="_compute_total_line")
	total_income_2006 = fields.Float(compute="_compute_total_line")
	total_income_2007 = fields.Float(compute="_compute_total_line")
	total_income_2008 = fields.Float(compute="_compute_total_line")
	total_income_2009 = fields.Float(compute="_compute_total_line")
	total_income_2010 = fields.Float(compute="_compute_total_line")
	total_income_2011 = fields.Float(compute="_compute_total_line")
	total_income_2012 = fields.Float(compute="_compute_total_line")
	total_income_2013 = fields.Float(compute="_compute_total_line")
	total_income_2014 = fields.Float(compute="_compute_total_line")
	total_income_2015 = fields.Float(compute="_compute_total_line")
	total_income_2016 = fields.Float(compute="_compute_total_line")
	total_income_2017 = fields.Float(compute="_compute_total_line")
	total_income_2018 = fields.Float(compute="_compute_total_line")
	total_income_2019 = fields.Float(compute="_compute_total_line")
	total_income_2020 = fields.Float(compute="_compute_total_line")

	total_2005 = fields.Float(string="Total_2005 : " , compute="_compute_total_line")
	total_2006 = fields.Float(string="Total_2006 : " , compute="_compute_total_line")
	total_2007 = fields.Float(string="Total_2007 : " , compute="_compute_total_line")
	total_2008 = fields.Float(string="Total_2008 : " , compute="_compute_total_line")
	total_2009 = fields.Float(string="Total_2009 : " , compute="_compute_total_line")
	total_2010 = fields.Float(string="Total_2010 : " , compute="_compute_total_line")
	total_2011 = fields.Float(string="Total_2011 : " , compute="_compute_total_line")
	total_2012 = fields.Float(string="Total_2012 : " , compute="_compute_total_line")
	total_2013 = fields.Float(string="Total_2013 : " , compute="_compute_total_line")
	total_2014 = fields.Float(string="Total_2014 : " , compute="_compute_total_line")
	total_2015 = fields.Float(string="Total_2015 : " , compute="_compute_total_line")
	total_2016 = fields.Float(string="Total_2016 : " , compute="_compute_total_line")
	total_2017 = fields.Float(string="Total_2017 : " , compute="_compute_total_line")
	total_2018 = fields.Float(string="Total_2018 : " , compute="_compute_total_line")
	total_2019 = fields.Float(string="Total_2019 : " , compute="_compute_total_line")
	total_2020 = fields.Float(string="Total_2020 : " , compute="_compute_total_line")

	@api.multi
	def _compute_total_line(self):

		self.total_summery_2005 = sum(line.y2005 for line in self.wealth_assets_ids)
		self.total_summery_2006 = sum(line.y2006 for line in self.wealth_assets_ids)
		self.total_summery_2007 = sum(line.y2007 for line in self.wealth_assets_ids)
		self.total_summery_2008 = sum(line.y2008 for line in self.wealth_assets_ids)
		self.total_summery_2009 = sum(line.y2009 for line in self.wealth_assets_ids)
		self.total_summery_2010 = sum(line.y2010 for line in self.wealth_assets_ids)
		self.total_summery_2011 = sum(line.y2011 for line in self.wealth_assets_ids)
		self.total_summery_2012 = sum(line.y2012 for line in self.wealth_assets_ids)
		self.total_summery_2013 = sum(line.y2013 for line in self.wealth_assets_ids)
		self.total_summery_2014 = sum(line.y2014 for line in self.wealth_assets_ids)
		self.total_summery_2015 = sum(line.y2015 for line in self.wealth_assets_ids)
		self.total_summery_2016 = sum(line.y2016 for line in self.wealth_assets_ids)
		self.total_summery_2017 = sum(line.y2017 for line in self.wealth_assets_ids)
		self.total_summery_2018 = sum(line.y2018 for line in self.wealth_assets_ids)
		self.total_summery_2019 = sum(line.y2019 for line in self.wealth_assets_ids)
		self.total_summery_2020 = sum(line.y2020 for line in self.wealth_assets_ids)

		self.total_income_2005 = sum(line.y2005 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2006 = sum(line.y2006 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2007 = sum(line.y2007 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2008 = sum(line.y2008 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2009 = sum(line.y2009 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2010 = sum(line.y2010 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2011 = sum(line.y2011 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2012 = sum(line.y2012 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2013 = sum(line.y2013 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2014 = sum(line.y2014 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2015 = sum(line.y2015 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2016 = sum(line.y2016 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2017 = sum(line.y2017 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2018 = sum(line.y2018 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2019 = sum(line.y2019 for line in self.wealth_reconciliation_income_ids)
		self.total_income_2020 = sum(line.y2020 for line in self.wealth_reconciliation_income_ids)

		self.total_opening_2005 = sum(line.y2005 for line in self.cash_opening_ids)
		self.total_opening_2006 = sum(line.y2006 for line in self.cash_opening_ids)
		self.total_opening_2007 = sum(line.y2007 for line in self.cash_opening_ids)
		self.total_opening_2008 = sum(line.y2008 for line in self.cash_opening_ids)
		self.total_opening_2009 = sum(line.y2009 for line in self.cash_opening_ids)
		self.total_opening_2010 = sum(line.y2010 for line in self.cash_opening_ids)
		self.total_opening_2011 = sum(line.y2011 for line in self.cash_opening_ids)
		self.total_opening_2012 = sum(line.y2012 for line in self.cash_opening_ids)
		self.total_opening_2013 = sum(line.y2013 for line in self.cash_opening_ids)
		self.total_opening_2014 = sum(line.y2014 for line in self.cash_opening_ids)
		self.total_opening_2015 = sum(line.y2015 for line in self.cash_opening_ids)
		self.total_opening_2016 = sum(line.y2016 for line in self.cash_opening_ids)
		self.total_opening_2017 = sum(line.y2017 for line in self.cash_opening_ids)
		self.total_opening_2018 = sum(line.y2018 for line in self.cash_opening_ids)
		self.total_opening_2019 = sum(line.y2019 for line in self.cash_opening_ids)
		self.total_opening_2020 = sum(line.y2020 for line in self.cash_opening_ids)

		self.total_expense_2005 = sum(line.y2005 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2006 = sum(line.y2006 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2007 = sum(line.y2007 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2008 = sum(line.y2008 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2009 = sum(line.y2009 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2010 = sum(line.y2010 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2011 = sum(line.y2011 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2012 = sum(line.y2012 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2013 = sum(line.y2013 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2014 = sum(line.y2014 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2015 = sum(line.y2015 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2016 = sum(line.y2016 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2017 = sum(line.y2017 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2018 = sum(line.y2018 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2019 = sum(line.y2019 for line in self.wealth_reconciliation_expense_ids)
		self.total_expense_2020 = sum(line.y2020 for line in self.wealth_reconciliation_expense_ids)


		self.total_2005 = self.total_summery_2005 - (self.total_opening_2005 + self.total_income_2005) - self.total_expense_2005
		self.total_2006 = self.total_summery_2006 - (self.total_opening_2006 + self.total_income_2006) - self.total_expense_2006
		self.total_2007 = self.total_summery_2007 - (self.total_opening_2007 + self.total_income_2007) - self.total_expense_2007
		self.total_2008 = self.total_summery_2008 - (self.total_opening_2008 + self.total_income_2008) - self.total_expense_2008
		self.total_2009 = self.total_summery_2009 - (self.total_opening_2009 + self.total_income_2009) - self.total_expense_2009
		self.total_2010 = self.total_summery_2010 - (self.total_opening_2010 + self.total_income_2010) - self.total_expense_2010
		self.total_2011 = self.total_summery_2011 - (self.total_opening_2011 + self.total_income_2011) - self.total_expense_2011
		self.total_2012 = self.total_summery_2012 - (self.total_opening_2012 + self.total_income_2012) - self.total_expense_2012
		self.total_2013 = self.total_summery_2013 - (self.total_opening_2013 + self.total_income_2013) - self.total_expense_2013
		self.total_2014 = self.total_summery_2014 - (self.total_opening_2014 + self.total_income_2014) - self.total_expense_2014
		self.total_2015 = self.total_summery_2015 - (self.total_opening_2015 + self.total_income_2015) - self.total_expense_2015
		self.total_2016 = self.total_summery_2016 - (self.total_opening_2016 + self.total_income_2016) - self.total_expense_2016
		self.total_2017 = self.total_summery_2017 - (self.total_opening_2017 + self.total_income_2017) - self.total_expense_2017
		self.total_2018 = self.total_summery_2018 - (self.total_opening_2018 + self.total_income_2018) - self.total_expense_2018
		self.total_2019 = self.total_summery_2019 - (self.total_opening_2019 + self.total_income_2019) - self.total_expense_2019
		self.total_2020 = self.total_summery_2020 - (self.total_opening_2020 + self.total_income_2020) - self.total_expense_2020

	@api.multi
	def update(self):
		self.wealth_reconciliation_income_ids.unlink()
		self.wealth_liability_ids.unlink()
		self.wealth_reconciliation_expense_ids.unlink()
		self.wealth_assets_ids.unlink()
		self.cash_closing_1_ids.unlink()
		self.cash_closing_2_ids.unlink()
		for y in self:

			for x in self.cash_receipts_ids.search([('receipt_type','=','income')]):

				y.wealth_reconciliation_income_ids.create({
					'description' : x.description,
					'y2005' : x.y2005,
					'y2006' : x.y2006,
					'y2007' : x.y2007,
					'y2008' : x.y2008,
					'y2009' : x.y2009,
					'y2010' : x.y2010,
					'y2011' : x.y2011,
					'y2012' : x.y2012,
					'y2013' : x.y2013,
					'y2014' : x.y2014,
					'y2015' : x.y2015,
					'y2016' : x.y2016,
					'y2017' : x.y2017,
					'y2018' : x.y2018,
					'y2019' : x.y2019,
					'y2020' : x.y2020,
					'wealth_income_id' : y.id
					})

			for x in self.cash_receipts_ids.search([('receipt_type','=','liability')]):

				y.wealth_liability_ids.create({
					'description' : x.description,
					'y2005' : x.y2005,
					'y2006' : x.y2006,
					'y2007' : x.y2007,
					'y2008' : x.y2008,
					'y2009' : x.y2009,
					'y2010' : x.y2010,
					'y2011' : x.y2011,
					'y2012' : x.y2012,
					'y2013' : x.y2013,
					'y2014' : x.y2014,
					'y2015' : x.y2015,
					'y2016' : x.y2016,
					'y2017' : x.y2017,
					'y2018' : x.y2018,
					'y2019' : x.y2019,
					'y2020' : x.y2020,
					'liability_id' : y.id
					})

			for x in self.cash_payments_ids.search([('receipt_type','=','expense')]):

				y.wealth_reconciliation_expense_ids.create({
					'description' : x.description,
					'y2005' : x.y2005,
					'y2006' : x.y2006,
					'y2007' : x.y2007,
					'y2008' : x.y2008,
					'y2009' : x.y2009,
					'y2010' : x.y2010,
					'y2011' : x.y2011,
					'y2012' : x.y2012,
					'y2013' : x.y2013,
					'y2014' : x.y2014,
					'y2015' : x.y2015,
					'y2016' : x.y2016,
					'y2017' : x.y2017,
					'y2018' : x.y2018,
					'y2019' : x.y2019,
					'y2020' : x.y2020,
					'wealth_expense_id' : y.id
					})

			for x in self.cash_payments_ids.search([('receipt_type','=','asset')]):

				y.wealth_assets_ids.create({
					'description' : x.description,
					'y2005' : x.y2005,
					'y2006' : x.y2006,
					'y2007' : x.y2007,
					'y2008' : x.y2008,
					'y2009' : x.y2009,
					'y2010' : x.y2010,
					'y2011' : x.y2011,
					'y2012' : x.y2012,
					'y2013' : x.y2013,
					'y2014' : x.y2014,
					'y2015' : x.y2015,
					'y2016' : x.y2016,
					'y2017' : x.y2017,
					'y2018' : x.y2018,
					'y2019' : x.y2019,
					'y2020' : x.y2020,
					'assets_id' : y.id
					})

			for x in self.cash_payments_ids.search([('receipt_type','=','loan_repayment')]):

				if y.wealth_liability_ids.description == x.description:
					
					y.wealth_liability_ids.y2005 = y.wealth_liability_ids.y2005 - x.y2005
					y.wealth_liability_ids.y2006 = y.wealth_liability_ids.y2006 - x.y2006
					y.wealth_liability_ids.y2007 = y.wealth_liability_ids.y2007 - x.y2007
					y.wealth_liability_ids.y2008 = y.wealth_liability_ids.y2008 - x.y2008
					y.wealth_liability_ids.y2009 = y.wealth_liability_ids.y2009 - x.y2009
					y.wealth_liability_ids.y2010 = y.wealth_liability_ids.y2010 - x.y2010
					y.wealth_liability_ids.y2011 = y.wealth_liability_ids.y2011 - x.y2011
					y.wealth_liability_ids.y2012 = y.wealth_liability_ids.y2012 - x.y2012
					y.wealth_liability_ids.y2013 = y.wealth_liability_ids.y2013 - x.y2013
					y.wealth_liability_ids.y2014 = y.wealth_liability_ids.y2014 - x.y2014
					y.wealth_liability_ids.y2015 = y.wealth_liability_ids.y2015 - x.y2015
					y.wealth_liability_ids.y2016 = y.wealth_liability_ids.y2016 - x.y2016
					y.wealth_liability_ids.y2017 = y.wealth_liability_ids.y2017 - x.y2017
					y.wealth_liability_ids.y2018 = y.wealth_liability_ids.y2018 - x.y2018
					y.wealth_liability_ids.y2019 = y.wealth_liability_ids.y2019 - x.y2019
					y.wealth_liability_ids.y2020 = y.wealth_liability_ids.y2020 - x.y2020

			y.cash_closing_1_ids.create({
				'description' : 'Closing',
				'y2005' : sum(x.y2005 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2005 for z in self.wealth_reconciliation_income_ids) - sum(c.y2005 for c in self.wealth_reconciliation_expense_ids),
				'y2006' : sum(x.y2006 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2006 for z in self.wealth_reconciliation_income_ids) - sum(c.y2006 for c in self.wealth_reconciliation_expense_ids),
				'y2007' : sum(x.y2007 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2007 for z in self.wealth_reconciliation_income_ids) - sum(c.y2007 for c in self.wealth_reconciliation_expense_ids),
				'y2008' : sum(x.y2008 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2008 for z in self.wealth_reconciliation_income_ids) - sum(c.y2008 for c in self.wealth_reconciliation_expense_ids),
				'y2009' : sum(x.y2009 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2009 for z in self.wealth_reconciliation_income_ids) - sum(c.y2009 for c in self.wealth_reconciliation_expense_ids),
				'y2010' : sum(x.y2010 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2010 for z in self.wealth_reconciliation_income_ids) - sum(c.y2010 for c in self.wealth_reconciliation_expense_ids),
				'y2011' : sum(x.y2011 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2011 for z in self.wealth_reconciliation_income_ids) - sum(c.y2011 for c in self.wealth_reconciliation_expense_ids),
				'y2012' : sum(x.y2012 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2012 for z in self.wealth_reconciliation_income_ids) - sum(c.y2012 for c in self.wealth_reconciliation_expense_ids),
				'y2013' : sum(x.y2013 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2013 for z in self.wealth_reconciliation_income_ids) - sum(c.y2013 for c in self.wealth_reconciliation_expense_ids),
				'y2014' : sum(x.y2014 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2014 for z in self.wealth_reconciliation_income_ids) - sum(c.y2014 for c in self.wealth_reconciliation_expense_ids),
				'y2015' : sum(x.y2015 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2015 for z in self.wealth_reconciliation_income_ids) - sum(c.y2015 for c in self.wealth_reconciliation_expense_ids),
				'y2016' : sum(x.y2016 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2016 for z in self.wealth_reconciliation_income_ids) - sum(c.y2016 for c in self.wealth_reconciliation_expense_ids),
				'y2017' : sum(x.y2017 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2017 for z in self.wealth_reconciliation_income_ids) - sum(c.y2017 for c in self.wealth_reconciliation_expense_ids),
				'y2018' : sum(x.y2018 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2018 for z in self.wealth_reconciliation_income_ids) - sum(c.y2018 for c in self.wealth_reconciliation_expense_ids),
				'y2019' : sum(x.y2019 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2019 for z in self.wealth_reconciliation_income_ids) - sum(c.y2019 for c in self.wealth_reconciliation_expense_ids),
				'y2020' : sum(x.y2020 for x in self.wealth_reconciliation_opening_ids) + sum(z.y2020 for z in self.wealth_reconciliation_income_ids) - sum(c.y2020 for c in self.wealth_reconciliation_expense_ids),
				'closing_1_id' : y.id
				})

			y.cash_closing_2_ids.create({
				'description' : 'Closing',
				'y2005' : sum(x.y2005 for x in self.wealth_assets_ids) - sum(z.y2005 for z in self.wealth_liability_ids),
				'y2006' : sum(x.y2006 for x in self.wealth_assets_ids) - sum(z.y2006 for z in self.wealth_liability_ids),
				'y2007' : sum(x.y2007 for x in self.wealth_assets_ids) - sum(z.y2007 for z in self.wealth_liability_ids),
				'y2008' : sum(x.y2008 for x in self.wealth_assets_ids) - sum(z.y2008 for z in self.wealth_liability_ids),
				'y2009' : sum(x.y2009 for x in self.wealth_assets_ids) - sum(z.y2009 for z in self.wealth_liability_ids),
				'y2010' : sum(x.y2010 for x in self.wealth_assets_ids) - sum(z.y2010 for z in self.wealth_liability_ids),
				'y2011' : sum(x.y2011 for x in self.wealth_assets_ids) - sum(z.y2011 for z in self.wealth_liability_ids),
				'y2012' : sum(x.y2012 for x in self.wealth_assets_ids) - sum(z.y2012 for z in self.wealth_liability_ids),
				'y2013' : sum(x.y2013 for x in self.wealth_assets_ids) - sum(z.y2013 for z in self.wealth_liability_ids),
				'y2014' : sum(x.y2014 for x in self.wealth_assets_ids) - sum(z.y2014 for z in self.wealth_liability_ids),
				'y2015' : sum(x.y2015 for x in self.wealth_assets_ids) - sum(z.y2015 for z in self.wealth_liability_ids),
				'y2016' : sum(x.y2016 for x in self.wealth_assets_ids) - sum(z.y2016 for z in self.wealth_liability_ids),
				'y2017' : sum(x.y2017 for x in self.wealth_assets_ids) - sum(z.y2017 for z in self.wealth_liability_ids),
				'y2018' : sum(x.y2018 for x in self.wealth_assets_ids) - sum(z.y2018 for z in self.wealth_liability_ids),
				'y2019' : sum(x.y2019 for x in self.wealth_assets_ids) - sum(z.y2019 for z in self.wealth_liability_ids),
				'y2020' : sum(x.y2020 for x in self.wealth_assets_ids) - sum(z.y2020 for z in self.wealth_liability_ids),
				'closing_2_id' : y.id
				})

	@api.multi
	def button_open_wizard_method(self):
		return {
		'type': 'ir.actions.act_window',
		'name': 'wizarddd',
		'res_model': 'dedy.yuristiawan.wizard',
		'view_type': 'form',
		'view_mode': 'form',
		'target' : 'new',
		}