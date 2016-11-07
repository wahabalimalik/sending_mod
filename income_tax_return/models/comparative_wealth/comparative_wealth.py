# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api
import datetime as dt

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
	capital_working_workbook_id       = fields.One2many('capital_working.capital_working', 'capital_working_id')
	capital_working_workbook_ids      = fields.One2many('capital_working.capital_working', 'capital_working_id')

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
		self.cash_closing_1_ids.unlink()
		self.cash_closing_2_ids.unlink()
		self.cash_opening_ids.unlink()
		self.wealth_reconciliation_opening_ids.unlink()

		years = {
			'y2005' : '2005',
			'y2006' : '2006',
			'y2007' : '2007',
			'y2008' : '2008',
			'y2009' : '2009',
			'y2010' : '2010',
			'y2011' : '2011',
			'y2012' : '2012',
			'y2013' : '2013',
			'y2014' : '2014',
			'y2015' : '2015',
			'y2016' : '2016',
			'y2017' : '2017',
			'y2018' : '2018',
			'y2019' : '2019',
			'y2020' : '2020',
			}

		tax_profited = self.env['tax.computation'].search([('client_name.id','=',self.name.id)])
		for x in tax_profited:
			self.wealth_reconciliation_income_ids.create({
				'description' : 'Business Income',
				'y2005'		  :(x.tax_profit if x.tax_year.code == "2005" else None),		
				'y2006'		  :(x.tax_profit if x.tax_year.code == "2006" else None),
				'y2007'		  :(x.tax_profit if x.tax_year.code == "2007" else None),
				'y2008'		  :(x.tax_profit if x.tax_year.code == "2008" else None),
				'y2009'		  :(x.tax_profit if x.tax_year.code == "2009" else None),
				'y2010'		  :(x.tax_profit if x.tax_year.code == "2010" else None),
				'y2011'		  :(x.tax_profit if x.tax_year.code == "2011" else None),
				'y2012'		  :(x.tax_profit if x.tax_year.code == "2012" else None),
				'y2013'		  :(x.tax_profit if x.tax_year.code == "2013" else None),
				'y2014'		  :(x.tax_profit if x.tax_year.code == "2014" else None),
				'y2015'		  :(x.tax_profit if x.tax_year.code == "2015" else None),
				'y2016'		  :(x.tax_profit if x.tax_year.code == "2016" else None),
				'y2017'		  :(x.tax_profit if x.tax_year.code == "2017" else None),
				'y2018'		  :(x.tax_profit if x.tax_year.code == "2018" else None),
				'y2019'		  :(x.tax_profit if x.tax_year.code == "2019" else None),
				'y2020'		  :(x.tax_profit if x.tax_year.code == "2020" else None),
				'receipt_type' : 'taxable',
				'wealth_income_id' : self.id
				})

		for y in self:

			for x in self.cash_receipts_ids.search([('receipt_type','=','income'),('receipts_id.id','=',self.id)]):

				y.wealth_reconciliation_income_ids.create({
					'description' : x.description,
					'receipt_type': x.tax_type,
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

			for x in self.cash_receipts_ids.search([('receipt_type','=','capital_gain'),('receipts_id.id','=',self.id)]):
				if x.capital_gain.capital_gain > 0 :
					y.wealth_reconciliation_income_ids.create({
						'description' : x.description,
						'receipt_type': x.tax_type,
						'y2005' : (x.capital_gain.capital_gain if x.y2005 > 0 else 0),
						'y2006' : (x.capital_gain.capital_gain if x.y2006 > 0 else 0),
						'y2007' : (x.capital_gain.capital_gain if x.y2007 > 0 else 0),
						'y2008' : (x.capital_gain.capital_gain if x.y2008 > 0 else 0),
						'y2009' : (x.capital_gain.capital_gain if x.y2009 > 0 else 0),
						'y2010' : (x.capital_gain.capital_gain if x.y2010 > 0 else 0),
						'y2011' : (x.capital_gain.capital_gain if x.y2011 > 0 else 0),
						'y2012' : (x.capital_gain.capital_gain if x.y2012 > 0 else 0),
						'y2013' : (x.capital_gain.capital_gain if x.y2013 > 0 else 0),
						'y2014' : (x.capital_gain.capital_gain if x.y2014 > 0 else 0),
						'y2015' : (x.capital_gain.capital_gain if x.y2015 > 0 else 0),
						'y2016' : (x.capital_gain.capital_gain if x.y2016 > 0 else 0),
						'y2017' : (x.capital_gain.capital_gain if x.y2017 > 0 else 0),
						'y2018' : (x.capital_gain.capital_gain if x.y2018 > 0 else 0),
						'y2019' : (x.capital_gain.capital_gain if x.y2019 > 0 else 0),
						'y2020' : (x.capital_gain.capital_gain if x.y2020 > 0 else 0),
						'wealth_income_id' : y.id
						})
				elif x.capital_gain.capital_gain < 0 :
					capital_gain = x.capital_gain.capital_gain * -1
					y.wealth_reconciliation_expense_ids.create({
						'description' : x.description,
						'receipt_type': x.tax_type,
						'y2005' : (capital_gain if x.y2005 > 0 else 0),
						'y2006' : (capital_gain if x.y2006 > 0 else 0),
						'y2007' : (capital_gain if x.y2007 > 0 else 0),
						'y2008' : (capital_gain if x.y2008 > 0 else 0),
						'y2009' : (capital_gain if x.y2009 > 0 else 0),
						'y2010' : (capital_gain if x.y2010 > 0 else 0),
						'y2011' : (capital_gain if x.y2011 > 0 else 0),
						'y2012' : (capital_gain if x.y2012 > 0 else 0),
						'y2013' : (capital_gain if x.y2013 > 0 else 0),
						'y2014' : (capital_gain if x.y2014 > 0 else 0),
						'y2015' : (capital_gain if x.y2015 > 0 else 0),
						'y2016' : (capital_gain if x.y2016 > 0 else 0),
						'y2017' : (capital_gain if x.y2017 > 0 else 0),
						'y2018' : (capital_gain if x.y2018 > 0 else 0),
						'y2019' : (capital_gain if x.y2019 > 0 else 0),
						'y2020' : (capital_gain if x.y2020 > 0 else 0),
						'wealth_expense_id' : y.id
						})

			for x in self.cash_receipts_ids.search([('receipt_type','=','liability'),('receipts_id.id','=',self.id)]):

				liability_2005 = x.y2005
				liability_2006 = x.y2006 + (liability_2005 if int(years['y2006']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2007 = x.y2007 + (liability_2006 if int(years['y2007']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2008 = x.y2008 + (liability_2007 if int(years['y2008']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2009 = x.y2009 + (liability_2008 if int(years['y2009']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2010 = x.y2010 + (liability_2009 if int(years['y2010']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2011 = x.y2011 + (liability_2010 if int(years['y2011']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2012 = x.y2012 + (liability_2011 if int(years['y2012']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2013 = x.y2013 + (liability_2012 if int(years['y2013']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2014 = x.y2014 + (liability_2013 if int(years['y2014']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2015 = x.y2015 + (liability_2014 if int(years['y2015']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2016 = x.y2016 + (liability_2015 if int(years['y2016']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2017 = x.y2017 + (liability_2016 if int(years['y2017']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2018 = x.y2018 + (liability_2017 if int(years['y2018']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2019 = x.y2019 + (liability_2018 if int(years['y2019']) <= int(dt.datetime.now().year) else 0 ) 
				liability_2020 = x.y2020 + (liability_2019 if int(years['y2020']) <= int(dt.datetime.now().year) else 0 ) 

				y.wealth_liability_ids.create({
					'description' : x.description,
					'y2005' : liability_2005,
					'y2006' : liability_2006,
					'y2007' : liability_2007,
					'y2008' : liability_2008,
					'y2009' : liability_2009,
					'y2010' : liability_2010,
					'y2011' : liability_2011,
					'y2012' : liability_2012,
					'y2013' : liability_2013,
					'y2014' : liability_2014,
					'y2015' : liability_2015,
					'y2016' : liability_2016,
					'y2017' : liability_2017,
					'y2018' : liability_2018,
					'y2019' : liability_2019,
					'y2020' : liability_2020,
					'liability_id' : y.id
					})

			for x in self.cash_payments_ids.search([('receipt_type','=','expense'),('payments_id.id','=',self.id)]):
				y.wealth_reconciliation_expense_ids.create({
					'description' : x.description,
					'receipt_type': x.tax_type,
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

			for x in self.cash_payments_ids.search([('receipt_type','=','loan_repayment'),('payments_id.id','=',self.id)]):
				# vv = (x.y2019 + x.y2018 + x.y2017 + x.y2016 + x.y2015 + x.y2014 + x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)            
				# print "pppppppppppppppppppp"
				# print vv
				for z in self.wealth_liability_ids:
					if z.description == x.description:

						wealth_liability_y2005 = z.y2005
						wealth_liability_y2006 = z.y2006 - (x.y2005)  
						wealth_liability_y2007 = z.y2007 - (x.y2006 + x.y2005)  
						wealth_liability_y2008 = z.y2008 - (x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2009 = z.y2009 - (x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2010 = z.y2010 - (x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2011 = z.y2011 - (x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2012 = z.y2012 - (x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2013 = z.y2013 - (x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2014 = z.y2014 - (x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2015 = z.y2015 - (x.y2014 + x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2016 = z.y2016 - (x.y2015 + x.y2014 + x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2017 = z.y2017 - (x.y2016 + x.y2015 + x.y2014 + x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2018 = z.y2018 - (x.y2017 + x.y2016 + x.y2015 + x.y2014 + x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2019 = z.y2019 - (x.y2018 + x.y2017 + x.y2016 + x.y2015 + x.y2014 + x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005)  
						wealth_liability_y2020 = z.y2020 - (x.y2019 + x.y2018 + x.y2017 + x.y2016 + x.y2015 + x.y2014 + x.y2013 + x.y2012 + x.y2011 + x.y2010 + x.y2009 + x.y2008 + x.y2007 + x.y2006 + x.y2005) 

						
						z.y2005 = (wealth_liability_y2005 - x.y2005 if int(years['y2005']) <= int(dt.datetime.now().year) else 0 )
						z.y2006 = (wealth_liability_y2006 - x.y2006 if int(years['y2006']) <= int(dt.datetime.now().year) else 0 )
						z.y2007 = (wealth_liability_y2007 - x.y2007 if int(years['y2007']) <= int(dt.datetime.now().year) else 0 )
						z.y2008 = (wealth_liability_y2008 - x.y2008 if int(years['y2008']) <= int(dt.datetime.now().year) else 0 )
						z.y2009 = (wealth_liability_y2009 - x.y2009 if int(years['y2009']) <= int(dt.datetime.now().year) else 0 )
						z.y2010 = (wealth_liability_y2010 - x.y2010 if int(years['y2010']) <= int(dt.datetime.now().year) else 0 )
						z.y2011 = (wealth_liability_y2011 - x.y2011 if int(years['y2011']) <= int(dt.datetime.now().year) else 0 )
						z.y2012 = (wealth_liability_y2012 - x.y2012 if int(years['y2012']) <= int(dt.datetime.now().year) else 0 )
						z.y2013 = (wealth_liability_y2013 - x.y2013 if int(years['y2013']) <= int(dt.datetime.now().year) else 0 )
						z.y2014 = (wealth_liability_y2014 - x.y2014 if int(years['y2014']) <= int(dt.datetime.now().year) else 0 )
						z.y2015 = (wealth_liability_y2015 - x.y2015 if int(years['y2015']) <= int(dt.datetime.now().year) else 0 )
						z.y2016 = (wealth_liability_y2016 - x.y2016 if int(years['y2016']) <= int(dt.datetime.now().year) else 0 )
						z.y2017 = (wealth_liability_y2017 - x.y2017 if int(years['y2017']) <= int(dt.datetime.now().year) else 0 )
						z.y2018 = (wealth_liability_y2018 - x.y2018 if int(years['y2018']) <= int(dt.datetime.now().year) else 0 )
						z.y2019 = (wealth_liability_y2019 - x.y2019 if int(years['y2019']) <= int(dt.datetime.now().year) else 0 )
						z.y2020 = (wealth_liability_y2020 - x.y2020 if int(years['y2020']) <= int(dt.datetime.now().year) else 0 )

			for x in self.cash_reconciliation_balance_ids:
				y.cash_opening_ids.create({
					'description':x.description,
					'receipt_type':x.receipt_type,
					'y2005': 0,
					'y2006': x.y2005,
					'y2007': x.y2006,
					'y2008': x.y2007,
					'y2009': x.y2008,
					'y2010': x.y2009,
					'y2011': x.y2010,
					'y2012': x.y2011,
					'y2013': x.y2012,
					'y2014': x.y2013,
					'y2015': x.y2014,
					'y2016': x.y2015,
					'y2017': x.y2016,
					'y2018': x.y2017,
					'y2019': x.y2018,
					'y2020': x.y2019,
					'opening_id':y.id
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

			for x in self.cash_closing_2_ids:
				y.wealth_reconciliation_opening_ids.create({
					'description': 'Opening',
					'y2005': 0,
					'y2006': x.y2005,
					'y2007': x.y2006,
					'y2008': x.y2007,
					'y2009': x.y2008,
					'y2010': x.y2009,
					'y2011': x.y2010,
					'y2012': x.y2011,
					'y2013': x.y2012,
					'y2014': x.y2013,
					'y2015': x.y2014,
					'y2016': x.y2015,
					'y2017': x.y2016,
					'y2018': x.y2017,
					'y2019': x.y2018,
					'y2020': x.y2019,
					'wealth_open_id':y.id
					})

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


		own_id_1 = []
		for y in self.wealth_assets_ids:
			own_id_1.append(y.own_id)
		for x in self.cash_reconciliation_balance_ids.search([('reconciliation_balance_id.id','=',self.id),('id','!=',own_id_1)]):
			self.wealth_assets_ids.create({
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
				'own_id': x.id,
				'assets_id' : self.id
				})
		
		for x in self.cash_reconciliation_balance_ids.search([('reconciliation_balance_id.id','=',self.id),('id','=',own_id_1)]):
			for z in self.wealth_assets_ids:
				if z.own_id == x.id :
					print "zzzzzzzzzzzzzzzzzzzkkkkkkkkkkkkkkkkk"
					print x.description
					print x.y2016
					print z.y2016
					z.description = x.description
					z.y2005 = x.y2005
					z.y2006 = x.y2006
					z.y2007 = x.y2007
					z.y2008 = x.y2008
					z.y2009 = x.y2009
					z.y2010 = x.y2010
					z.y2011 = x.y2011
					z.y2012 = x.y2012
					z.y2013 = x.y2013
					z.y2014 = x.y2014
					z.y2015 = x.y2015
					z.y2016 = x.y2016
					z.y2017 = x.y2017
					z.y2018 = x.y2018
					z.y2019 = x.y2019
					z.y2020 = x.y2020
					z.own_id = x.id
					z.assets_id = self.id

		for x in self.capital_working_workbook_ids.search([('capital_working_id.id','=',self.id),('id','!=',own_id_1)]):
			self.wealth_assets_ids.create({
				'description' : 'Capital ' + x.business.business,
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
				'own_id': x.id,
				'assets_id' : self.id
				})
		for x in self.capital_working_workbook_ids.search([('capital_working_id.id','=',self.id),('id','=',own_id_1)]):
			for z in self.wealth_assets_ids:
				if z.own_id == x.id :
					z.description = 'Capital ' + x.business.business
					z.y2005 = x.y2005
					z.y2006 = x.y2006
					z.y2007 = x.y2007
					z.y2008 = x.y2008
					z.y2009 = x.y2009
					z.y2010 = x.y2010
					z.y2011 = x.y2011
					z.y2012 = x.y2012
					z.y2013 = x.y2013
					z.y2014 = x.y2014
					z.y2015 = x.y2015
					z.y2016 = x.y2016
					z.y2017 = x.y2017
					z.y2018 = x.y2018
					z.y2019 = x.y2019
					z.y2020 = x.y2020
					z.own_id = x.id
					z.assets_id = self.id

		for x in self.cash_receipts_ids.search([('receipts_id.id','=',self.id)]):
			for z in self.wealth_assets_ids:
				if z.description == x.description and x.receipt_type == 'asset':
					z.description = x.description + '.'
					z.y2005 = z.y2005 - x.y2005
					z.y2006 = z.y2006 - x.y2006
					z.y2007 = z.y2007 - x.y2007
					z.y2008 = z.y2008 - x.y2008
					z.y2009 = z.y2009 - x.y2009
					z.y2010 = z.y2010 - x.y2010
					z.y2011 = z.y2011 - x.y2011
					z.y2012 = z.y2012 - x.y2012
					z.y2013 = z.y2013 - x.y2013
					z.y2014 = z.y2014 - x.y2014
					z.y2015 = z.y2015 - x.y2015
					z.y2016 = z.y2016 - x.y2016
					z.y2017 = z.y2017 - x.y2017
					z.y2018 = z.y2018 - x.y2018
					z.y2019 = z.y2019 - x.y2019
					z.y2020 = z.y2020 - x.y2020
					z.own_id = x.id
					z.assets_id = self.id
			for z in self.wealth_assets_ids:
				if z.description == x.description and x.receipt_type == 'capital_gain':
					# print 'hahhahahahahhahhahahahahahaha'
					# gg = x.description
					# print gg[-1]
					# print gg[:5]
					# # if gg[-1] == '.' :
					# # 	gg = x.description[0:(len(x.description)-1)]
					# # print gg
					z.description = x.description + '.'
					z.y2005 = (z.y2005 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2005' else z.y2005 ) 
					z.y2006 = (z.y2006 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2006' else z.y2006 ) 
					z.y2007 = (z.y2007 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2007' else z.y2007 ) 
					z.y2008 = (z.y2008 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2008' else z.y2008 ) 
					z.y2009 = (z.y2009 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2009' else z.y2009 ) 
					z.y2010 = (z.y2010 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2010' else z.y2010 ) 
					z.y2011 = (z.y2011 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2011' else z.y2011 ) 
					z.y2012 = (z.y2012 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2012' else z.y2012 ) 
					z.y2013 = (z.y2013 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2013' else z.y2013 ) 
					z.y2014 = (z.y2014 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2014' else z.y2014 ) 
					z.y2015 = (z.y2015 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2015' else z.y2015 ) 
					z.y2016 = (z.y2016 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2016' else z.y2016 ) 
					z.y2017 = (z.y2017 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2017' else z.y2017 ) 
					z.y2018 = (z.y2018 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2018' else z.y2018 ) 
					z.y2019 = (z.y2019 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2019' else z.y2019 ) 
					z.y2020 = (z.y2020 - x.capital_gain.purchase_value if x.capital_gain.year_sale.code == '2020' else z.y2020 ) 
					z.own_id = x.id
					z.assets_id = self.id

	@api.multi
	def upload_assets(self):
		own_id_1 = []
		for y in self.wealth_assets_ids:
			own_id_1.append(y.own_id)
		for x in self.cash_payments_ids.search([('receipt_type','=','asset'),('payments_id.id','=',self.id),('id','!=',own_id_1)]):
			self.wealth_assets_ids.create({
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
				'own_id': x.id,
				'assets_id' : self.id
				})

		
		for x in self.cash_payments_ids.search([('receipt_type','=','asset'),('payments_id.id','=',self.id),('id','=',own_id_1)]):
			for y in self.wealth_assets_ids:
				if y.own_id == x.id :
					y.description = x.description
					y.y2005 = (y.y2005 if x.y2005 == 0 else x.y2005)
					y.y2006 = (y.y2006 if x.y2006 == 0 else x.y2006)
					y.y2007 = (y.y2007 if x.y2007 == 0 else x.y2007)
					y.y2008 = (y.y2008 if x.y2008 == 0 else x.y2008)
					y.y2009 = (y.y2009 if x.y2009 == 0 else x.y2009)
					y.y2010 = (y.y2010 if x.y2010 == 0 else x.y2010)
					y.y2011 = (y.y2011 if x.y2011 == 0 else x.y2011)
					y.y2012 = (y.y2012 if x.y2012 == 0 else x.y2012)
					y.y2013 = (y.y2013 if x.y2013 == 0 else x.y2013)
					y.y2014 = (y.y2014 if x.y2014 == 0 else x.y2014)
					y.y2015 = (y.y2015 if x.y2015 == 0 else x.y2015)
					y.y2016 = (y.y2016 if x.y2016 == 0 else x.y2016)
					y.y2017 = (y.y2017 if x.y2017 == 0 else x.y2017)
					y.y2018 = (y.y2018 if x.y2018 == 0 else x.y2018)
					y.y2019 = (y.y2019 if x.y2019 == 0 else x.y2019)
					y.y2020 = (y.y2020 if x.y2020 == 0 else x.y2020)
					y.own_id = x.id
					y.assets_id = self.id

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