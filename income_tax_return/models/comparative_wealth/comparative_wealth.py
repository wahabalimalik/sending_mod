# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class comparative_wealth(models.Model):
	_name                             = 'comparative.wealth'
	_inherit                          = ['mail.thread', 'ir.needaction_mixin']
	name                       = fields.Many2one('res.partner','Client Name', required=True)
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

	# total_summery_2005 = fields.Float(compute="_compute_total_line")
	# total_summery_2006 = fields.Float(compute="_compute_total_line")
	# total_summery_2007 = fields.Float(compute="_compute_total_line")
	# total_summery_2008 = fields.Float(compute="_compute_total_line")
	# total_summery_2009 = fields.Float(compute="_compute_total_line")
	# total_summery_2010 = fields.Float(compute="_compute_total_line")
	# total_summery_2011 = fields.Float(compute="_compute_total_line")
	# total_summery_2012 = fields.Float(compute="_compute_total_line")
	# total_summery_2013 = fields.Float(compute="_compute_total_line")
	# total_summery_2014 = fields.Float(compute="_compute_total_line")
	# total_summery_2015 = fields.Float(compute="_compute_total_line")
	# total_summery_2016 = fields.Float(compute="_compute_total_line")
	# total_summery_2017 = fields.Float(compute="_compute_total_line")
	# total_summery_2018 = fields.Float(compute="_compute_total_line")
	# total_summery_2019 = fields.Float(compute="_compute_total_line")
	# total_summery_2020 = fields.Float(compute="_compute_total_line")

	# total_expense_2005 = fields.Float(compute="_compute_total_line")
	# total_expense_2006 = fields.Float(compute="_compute_total_line")
	# total_expense_2007 = fields.Float(compute="_compute_total_line")
	# total_expense_2008 = fields.Float(compute="_compute_total_line")
	# total_expense_2009 = fields.Float(compute="_compute_total_line")
	# total_expense_2010 = fields.Float(compute="_compute_total_line")
	# total_expense_2011 = fields.Float(compute="_compute_total_line")
	# total_expense_2012 = fields.Float(compute="_compute_total_line")
	# total_expense_2013 = fields.Float(compute="_compute_total_line")
	# total_expense_2014 = fields.Float(compute="_compute_total_line")
	# total_expense_2015 = fields.Float(compute="_compute_total_line")
	# total_expense_2016 = fields.Float(compute="_compute_total_line")
	# total_expense_2017 = fields.Float(compute="_compute_total_line")
	# total_expense_2018 = fields.Float(compute="_compute_total_line")
	# total_expense_2019 = fields.Float(compute="_compute_total_line")
	# total_expense_2020 = fields.Float(compute="_compute_total_line")

	# total_income_2005 = fields.Float(compute="_compute_total_line")
	# total_income_2006 = fields.Float(compute="_compute_total_line")
	# total_income_2007 = fields.Float(compute="_compute_total_line")
	# total_income_2008 = fields.Float(compute="_compute_total_line")
	# total_income_2009 = fields.Float(compute="_compute_total_line")
	# total_income_2010 = fields.Float(compute="_compute_total_line")
	# total_income_2011 = fields.Float(compute="_compute_total_line")
	# total_income_2012 = fields.Float(compute="_compute_total_line")
	# total_income_2013 = fields.Float(compute="_compute_total_line")
	# total_income_2014 = fields.Float(compute="_compute_total_line")
	# total_income_2015 = fields.Float(compute="_compute_total_line")
	# total_income_2016 = fields.Float(compute="_compute_total_line")
	# total_income_2017 = fields.Float(compute="_compute_total_line")
	# total_income_2018 = fields.Float(compute="_compute_total_line")
	# total_income_2019 = fields.Float(compute="_compute_total_line")
	# total_income_2020 = fields.Float(compute="_compute_total_line")

	# total_2005 = fields.Float(string="Total_2005 : " , compute="_compute_total_line")
	# total_2006 = fields.Float(string="Total_2006 : " , compute="_compute_total_line")
	# total_2007 = fields.Float(string="Total_2007 : " , compute="_compute_total_line")
	# total_2008 = fields.Float(string="Total_2008 : " , compute="_compute_total_line")
	# total_2009 = fields.Float(string="Total_2009 : " , compute="_compute_total_line")
	# total_2010 = fields.Float(string="Total_2010 : " , compute="_compute_total_line")
	# total_2011 = fields.Float(string="Total_2011 : " , compute="_compute_total_line")
	# total_2012 = fields.Float(string="Total_2012 : " , compute="_compute_total_line")
	# total_2013 = fields.Float(string="Total_2013 : " , compute="_compute_total_line")
	# total_2014 = fields.Float(string="Total_2014 : " , compute="_compute_total_line")
	# total_2015 = fields.Float(string="Total_2015 : " , compute="_compute_total_line")
	# total_2016 = fields.Float(string="Total_2016 : " , compute="_compute_total_line")
	# total_2017 = fields.Float(string="Total_2017 : " , compute="_compute_total_line")
	# total_2018 = fields.Float(string="Total_2018 : " , compute="_compute_total_line")
	# total_2019 = fields.Float(string="Total_2019 : " , compute="_compute_total_line")
	# total_2020 = fields.Float(string="Total_2020 : " , compute="_compute_total_line")

	# @api.multi
	# def _compute_total_line(self):

	# 	self.total_summery_2005 = sum(line.y2005 for line in self.wealth_assets_ids)
	# 	self.total_summery_2006 = sum(line.y2006 for line in self.wealth_assets_ids)
	# 	self.total_summery_2007 = sum(line.y2007 for line in self.wealth_assets_ids)
	# 	self.total_summery_2008 = sum(line.y2008 for line in self.wealth_assets_ids)
	# 	self.total_summery_2009 = sum(line.y2009 for line in self.wealth_assets_ids)
	# 	self.total_summery_2010 = sum(line.y2010 for line in self.wealth_assets_ids)
	# 	self.total_summery_2011 = sum(line.y2011 for line in self.wealth_assets_ids)
	# 	self.total_summery_2012 = sum(line.y2012 for line in self.wealth_assets_ids)
	# 	self.total_summery_2013 = sum(line.y2013 for line in self.wealth_assets_ids)
	# 	self.total_summery_2014 = sum(line.y2014 for line in self.wealth_assets_ids)
	# 	self.total_summery_2015 = sum(line.y2015 for line in self.wealth_assets_ids)
	# 	self.total_summery_2016 = sum(line.y2016 for line in self.wealth_assets_ids)
	# 	self.total_summery_2017 = sum(line.y2017 for line in self.wealth_assets_ids)
	# 	self.total_summery_2018 = sum(line.y2018 for line in self.wealth_assets_ids)
	# 	self.total_summery_2019 = sum(line.y2019 for line in self.wealth_assets_ids)
	# 	self.total_summery_2020 = sum(line.y2020 for line in self.wealth_assets_ids)

	# 	self.total_income_2005 = sum(line.y2005 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2006 = sum(line.y2006 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2007 = sum(line.y2007 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2008 = sum(line.y2008 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2009 = sum(line.y2009 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2010 = sum(line.y2010 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2011 = sum(line.y2011 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2012 = sum(line.y2012 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2013 = sum(line.y2013 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2014 = sum(line.y2014 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2015 = sum(line.y2015 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2016 = sum(line.y2016 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2017 = sum(line.y2017 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2018 = sum(line.y2018 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2019 = sum(line.y2019 for line in self.wealth_reconciliation_income_ids)
	# 	self.total_income_2020 = sum(line.y2020 for line in self.wealth_reconciliation_income_ids)


	# 	self.total_expense_2005 = sum(line.y2005 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2006 = sum(line.y2006 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2007 = sum(line.y2007 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2008 = sum(line.y2008 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2009 = sum(line.y2009 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2010 = sum(line.y2010 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2011 = sum(line.y2011 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2012 = sum(line.y2012 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2013 = sum(line.y2013 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2014 = sum(line.y2014 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2015 = sum(line.y2015 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2016 = sum(line.y2016 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2017 = sum(line.y2017 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2018 = sum(line.y2018 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2019 = sum(line.y2019 for line in self.wealth_reconciliation_expense_ids)
	# 	self.total_expense_2020 = sum(line.y2020 for line in self.wealth_reconciliation_expense_ids)


	# 	self.total_2005 = self.total_summery_2005 - self.total_income_2005 - self.total_expense_2005
	# 	self.total_2006 = self.total_summery_2006 - self.total_income_2006 - self.total_expense_2006
	# 	self.total_2007 = self.total_summery_2007 - self.total_income_2007 - self.total_expense_2007
	# 	self.total_2008 = self.total_summery_2008 - self.total_income_2008 - self.total_expense_2008
	# 	self.total_2009 = self.total_summery_2009 - self.total_income_2009 - self.total_expense_2009
	# 	self.total_2010 = self.total_summery_2010 - self.total_income_2010 - self.total_expense_2010
	# 	self.total_2011 = self.total_summery_2011 - self.total_income_2011 - self.total_expense_2011
	# 	self.total_2012 = self.total_summery_2012 - self.total_income_2012 - self.total_expense_2012
	# 	self.total_2013 = self.total_summery_2013 - self.total_income_2013 - self.total_expense_2013
	# 	self.total_2014 = self.total_summery_2014 - self.total_income_2014 - self.total_expense_2014
	# 	self.total_2015 = self.total_summery_2015 - self.total_income_2015 - self.total_expense_2015
	# 	self.total_2016 = self.total_summery_2016 - self.total_income_2016 - self.total_expense_2016
	# 	self.total_2017 = self.total_summery_2017 - self.total_income_2017 - self.total_expense_2017
	# 	self.total_2018 = self.total_summery_2018 - self.total_income_2018 - self.total_expense_2018
	# 	self.total_2019 = self.total_summery_2019 - self.total_income_2019 - self.total_expense_2019
	# 	self.total_2020 = self.total_summery_2020 - self.total_income_2020 - self.total_expense_2020