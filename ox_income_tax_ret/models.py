string="Total : " , # -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------

from openerp import models, fields, api
class ox_income_tax_returns(models.Model):
	_name = 'ox.income.tax.returns'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	state = fields.Selection([
            ('draft', 'Draft'),
            ('prepared', 'Prepared'),
            ('submitted', 'Submitted'),
            ],default='draft')
	name = fields.Char(string="Name")
	ntn = fields.Char(required=True)
	# 'res.partner','NTN', 
	client_name = fields.Many2one('res.partner','Client Name', required=True)
	tax_year = fields.Many2one('account.fiscalyear', 'Tax Year')
	description = fields.Text('Description')
	period = fields.Char('Period')
	unit_price = fields.Float('Unit Price', required=True)
	prepared_by = fields.Many2one('hr.employee', 'Prepared by')
	comparative_id = fields.Many2one('comparative.wealth', string = 'Comparative Wealth')
	_defaults = { 'name': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'ox.income.tax.returns'), }

	@api.multi
	def queru_subbmitted_btn(self):
		invoice_recs = self.env['account.invoice']
		account_id = self.env['account.account'].search([('code','=',110200)])
		account_id_invoice_line = self.env['account.account'].search([('code','=',200000)])
		invoice_line_data = [
		(0, 0,
			{
				'quantity': 1,
				'name': self.description or 'No Description',
				'account_id': account_id_invoice_line.id,
				'price_unit': self.unit_price,
			}
		)
		]
		res = {
		'partner_id' : self.client_name.id,
		'account_id' : account_id.id,
		'invoice_line' : invoice_line_data,
		}
		invoice_recs.create(res)
		return self.write({'state' : 'submitted'})

	@api.multi
	def btn_draft_to_prepared(self):
		return self.write({'state' : 'prepared'})

	@api.onchange('client_name')
	def onchange_assesment_form_field(self):
		self.ntn = self.client_name.ntn

# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------

class comparative_wealth(models.Model):
	_name = 'comparative.wealth'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	client_name = fields.Many2one('res.partner','Client Name', required=True)
	_defaults = { 'name': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'comparative.wealth'), }
	name = fields.Char(string="Name")
	all_years = fields.Boolean(string="All Years", default=False)
	wealth_statement_id = fields.One2many('wealth.statement', 'wealth_id')
	wealth_statement_ids = fields.One2many('wealth.statement', 'wealth_id')
	wealth_reconciliation_income_id = fields.One2many('wealth.reconciliation.income', 'wealth_income_id')
	wealth_reconciliation_income_ids = fields.One2many('wealth.reconciliation.income', 'wealth_income_id')
	wealth_reconciliation_expense_id = fields.One2many('wealth.reconciliation.expense', 'wealth_expense_id')
	wealth_reconciliation_expense_ids = fields.One2many('wealth.reconciliation.expense', 'wealth_expense_id')

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

		self.total_summery_2005 = sum(line.y2005 for line in self.wealth_statement_ids)
		self.total_summery_2006 = sum(line.y2006 for line in self.wealth_statement_ids)
		self.total_summery_2007 = sum(line.y2007 for line in self.wealth_statement_ids)
		self.total_summery_2008 = sum(line.y2008 for line in self.wealth_statement_ids)
		self.total_summery_2009 = sum(line.y2009 for line in self.wealth_statement_ids)
		self.total_summery_2010 = sum(line.y2010 for line in self.wealth_statement_ids)
		self.total_summery_2011 = sum(line.y2011 for line in self.wealth_statement_ids)
		self.total_summery_2012 = sum(line.y2012 for line in self.wealth_statement_ids)
		self.total_summery_2013 = sum(line.y2013 for line in self.wealth_statement_ids)
		self.total_summery_2014 = sum(line.y2014 for line in self.wealth_statement_ids)
		self.total_summery_2015 = sum(line.y2015 for line in self.wealth_statement_ids)
		self.total_summery_2016 = sum(line.y2016 for line in self.wealth_statement_ids)
		self.total_summery_2017 = sum(line.y2017 for line in self.wealth_statement_ids)
		self.total_summery_2018 = sum(line.y2018 for line in self.wealth_statement_ids)
		self.total_summery_2019 = sum(line.y2019 for line in self.wealth_statement_ids)
		self.total_summery_2020 = sum(line.y2020 for line in self.wealth_statement_ids)

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


		self.total_2005 = self.total_summery_2005 + self.total_income_2005 
		self.total_2006 = self.total_summery_2006 + self.total_income_2006 
		self.total_2007 = self.total_summery_2007 + self.total_income_2007 
		self.total_2008 = self.total_summery_2008 + self.total_income_2008 
		self.total_2009 = self.total_summery_2009 + self.total_income_2009 
		self.total_2010 = self.total_summery_2010 + self.total_income_2010 
		self.total_2011 = self.total_summery_2011 + self.total_income_2011 
		self.total_2012 = self.total_summery_2012 + self.total_income_2012 
		self.total_2013 = self.total_summery_2013 + self.total_income_2013 
		self.total_2014 = self.total_summery_2014 + self.total_income_2014 
		self.total_2015 = self.total_summery_2015 + self.total_income_2015 
		self.total_2016 = self.total_summery_2016 + self.total_income_2016 
		self.total_2017 = self.total_summery_2017 + self.total_income_2017 
		self.total_2018 = self.total_summery_2018 + self.total_income_2018 
		self.total_2019 = self.total_summery_2019 + self.total_income_2019 
		self.total_2020 = self.total_summery_2020 + self.total_income_2020 


		self.total_2005 = self.total_2005 - self.total_expense_2005
		self.total_2006 = self.total_2006 - self.total_expense_2006
		self.total_2007 = self.total_2007 - self.total_expense_2007
		self.total_2008 = self.total_2008 - self.total_expense_2008
		self.total_2009 = self.total_2009 - self.total_expense_2009
		self.total_2010 = self.total_2010 - self.total_expense_2010
		self.total_2011 = self.total_2011 - self.total_expense_2011
		self.total_2012 = self.total_2012 - self.total_expense_2012
		self.total_2013 = self.total_2013 - self.total_expense_2013
		self.total_2014 = self.total_2014 - self.total_expense_2014
		self.total_2015 = self.total_2015 - self.total_expense_2015
		self.total_2016 = self.total_2016 - self.total_expense_2016
		self.total_2017 = self.total_2017 - self.total_expense_2017
		self.total_2018 = self.total_2018 - self.total_expense_2018
		self.total_2019 = self.total_2019 - self.total_expense_2019
		self.total_2020 = self.total_2020 - self.total_expense_2020



# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------

class wealth_statement(models.Model):
	_name = 'wealth.statement'
	description = fields.Char(string = "Description", required=True)
	y2005 = fields.Float(string = "2005")
	y2006 = fields.Float(string = "2006")
	y2007 = fields.Float(string = "2007")
	y2008 = fields.Float(string = "2008")
	y2009 = fields.Float(string = "2009")
	y2010 = fields.Float(string = "2010")
	y2011 = fields.Float(string = "2011")
	y2012 = fields.Float(string = "2012")
	y2013 = fields.Float(string = "2013")
	y2014 = fields.Float(string = "2014")
	y2015 = fields.Float(string = "2015")
	y2016 = fields.Float(string = "2016")
	y2017 = fields.Float(string = "2017")
	y2018 = fields.Float(string = "2018")
	y2019 = fields.Float(string = "2019")
	y2020 = fields.Float(string = "2020")

	wealth_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Statement", required=True)

# ---------------------------------------------------------------------
# For Wealth Reconciliation we need two work books,
# 1-For Income
# 2-For Expense
# So we make two different classes
# First class "wealth_reconciliation_income" is for income records
# First class "wealth_reconciliation_expense" is for expense records
# ----------------------------------------------------------------------

# 1-For Income
class wealth_reconciliation_income(models.Model):
	_name = 'wealth.reconciliation.income'
	description = fields.Char(string = "Description", required=True)
	y2005 = fields.Float(string = "2005")
	y2006 = fields.Float(string = "2006")
	y2007 = fields.Float(string = "2007")
	y2008 = fields.Float(string = "2008")
	y2009 = fields.Float(string = "2009")
	y2010 = fields.Float(string = "2010")
	y2011 = fields.Float(string = "2011")
	y2012 = fields.Float(string = "2012")
	y2013 = fields.Float(string = "2013")
	y2014 = fields.Float(string = "2014")
	y2015 = fields.Float(string = "2015")
	y2016 = fields.Float(string = "2016")
	y2017 = fields.Float(string = "2017")
	y2018 = fields.Float(string = "2018")
	y2019 = fields.Float(string = "2019")
	y2020 = fields.Float(string = "2020")

	wealth_income_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Reconciliation", required=True)

# 2-For Expense
class wealth_reconciliation_expense(models.Model):
	_name = 'wealth.reconciliation.expense'
	description = fields.Char(string = "Description", required=True)
	y2005 = fields.Float(string = "2005")
	y2006 = fields.Float(string = "2006")
	y2007 = fields.Float(string = "2007")
	y2008 = fields.Float(string = "2008")
	y2009 = fields.Float(string = "2009")
	y2010 = fields.Float(string = "2010")
	y2011 = fields.Float(string = "2011")
	y2012 = fields.Float(string = "2012")
	y2013 = fields.Float(string = "2013")
	y2014 = fields.Float(string = "2014")
	y2015 = fields.Float(string = "2015")
	y2016 = fields.Float(string = "2016")
	y2017 = fields.Float(string = "2017")
	y2018 = fields.Float(string = "2018")
	y2019 = fields.Float(string = "2019")
	y2020 = fields.Float(string = "2020")

	wealth_expense_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Reconciliation", required=True)





























