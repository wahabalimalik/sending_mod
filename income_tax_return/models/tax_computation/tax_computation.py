#--------------------------------------------------------------------------------
#
#
#--------------------------------------------------------------------------------

from openerp import models, fields, api

class tax_computation(models.Model):
	_name = 'tax.computation'

	client_name             = fields.Many2one('res.partner','Client Name', required=True)
	tax_year                = fields.Many2one('account.fiscalyear', 'Tax Year')
	group                   = fields.Many2one('res.partner')

	income_under_ntr        = fields.Float(string="Income under NTR")
	exempt_income           = fields.Float(string="Exempt Income ")
	deductible_allowance    = fields.Float(string="Deductible Allowance")
	taxable_income          = fields.Float(string="Taxable Income")
	tax_rate                = fields.Float(string="Rate of Tax")
	tax_liability           = fields.Float(string="Tax Liability")
	portion_of_minimum_tax  = fields.Float(string="Portion of Minimum Tax")
	payable_tax             = fields.Float(string="Total Tax Payable")
	tax_adjust              = fields.Float(string="Tax deducted Adjustable")
	tax_deduct_min          = fields.Float(string="Tax deducted Minimum")
	total_tax               = fields.Float(string="Total Tax")
	tax_credits             = fields.Float(string="Tax Credits")
	refund_adjust           = fields.Float(string="Refund Adjustment")
	tax_ratio               = fields.Float(string="Tax Payable/ (Refundable)")
	rebate                  = fields.Float()

	income_under_ftr        = fields.Float(string="Income under FTR")
	tax_deduct              = fields.Float(string="Tax deducted")
	description             = fields.Text()
	amount                  = fields.Float()

	tax_computation_ntr_id        = fields.One2many('income.under.ntr', 'income_under_ntr_id')
	tax_computation_deductible_id = fields.One2many('deductible.allowance', 'deductible_allowance_id')
	tax_credits_id                = fields.One2many('tax.credits', 'tax_credits_id')
	tax_rebate_id                 = fields.One2many('income.rebate', 'income_rebate_id')
	tax_computation_ftr_id        = fields.One2many('income.under.ftr', 'income_under_ftr_id')
	tax_deduct_link_id            = fields.One2many('tax.deduct', 'tax_deduct_id')

	@api.onchange('tax_computation_ntr_id')
	def _onchange_ntr_id(self):
		self.income_under_ntr = sum(line.amount for line in self.tax_computation_ntr_id if line.tax_type!='exempt')
		self.exempt_income = sum(line.amount for line in self.tax_computation_ntr_id if line.tax_type!='taxable')

	@api.onchange('tax_computation_deductible_id')
	def _onchange_deductible_id(self):
		self.deductible_allowance = sum(line.tax for line in self.tax_computation_deductible_id)

	@api.onchange('tax_rebate_id')
	def _onchange_rebate_id(self):
		self.rebate = sum(line.tax for line in self.tax_rebate_id)

	@api.onchange('tax_credits_id')
	def _onchange_credits_id(self):
		self.tax_credits = sum(line.tax for line in self.tax_credits_id)

	@api.onchange('tax_computation_ftr_id')
	def _onchange_ftr_id(self):
		self.income_under_ftr = sum(line.amount for line in self.tax_computation_ftr_id)
		self.tax_deduct = sum(line.tax for line in self.tax_computation_ftr_id)

	@api.onchange('tax_deduct_link_id')
	def _onchange_tax_deduct(self):
		self.tax_adjust = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type=='adjustable')
		self.tax_deduct_min = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type=='minimum')
				
	@api.onchange('income_under_ntr','deductible_allowance','tax_rate','portion_of_minimum_tax','tax_adjust','tax_deduct_min','refund_adjust')
	def onchange_assesment_form_field(self):
		self.taxable_income = self.income_under_ntr - self.deductible_allowance
		self.tax_liability  = self.taxable_income * self.tax_rate
		self.payable_tax    = self.tax_liability + self.portion_of_minimum_tax
		self.total_tax      = self.payable_tax - self.tax_adjust
		self.total_tax      = self.total_tax - self.tax_deduct_min
		self.tax_ratio      = self.total_tax - self.refund_adjust

	@api.multi
	def update_computation(self):
		self.tax_computation_ntr_id.unlink()
		self.tax_computation_ftr_id.unlink()
		self.tax_deduct_link_id.unlink()
		required_class = self.env['comparative.wealth'].search([('name','=',self.client_name.id)])

		for y in self:
			for x in required_class.wealth_reconciliation_income_ids:
				dic = {
				x.y2005 : '2005',
				x.y2006 : '2006',
				x.y2007 : '2007',
				x.y2008 : '2008',
				x.y2009 : '2009',
				x.y2010 : '2010',
				x.y2011 : '2011',
				x.y2012 : '2012',
				x.y2013 : '2013',
				x.y2014 : '2014',
				x.y2015 : '2015',
				x.y2016 : '2016',
				x.y2017 : '2017',
				x.y2018 : '2018',
				x.y2019 : '2019',
				x.y2020 : '2020',
				}
				for key, value in dic.iteritems():
					if x.receipt_type != 'ftr' and dic[key] == self.tax_year.code:
						y.tax_computation_ntr_id.create({
							'description' : x.description,
							'tax_type':x.receipt_type,
							'amount':key,
							'income_under_ntr_id': y.id,
							})
					elif x.receipt_type == 'ftr' and dic[key] == self.tax_year.code:

						y.tax_computation_ftr_id.create({
							'description' : x.description,
							'amount':key,
							'income_under_ftr_id': y.id,
							})
			for x in required_class.wealth_reconciliation_expense_ids:
				dic = {
				x.y2005 : '2005',
				x.y2006 : '2006',
				x.y2007 : '2007',
				x.y2008 : '2008',
				x.y2009 : '2009',
				x.y2010 : '2010',
				x.y2011 : '2011',
				x.y2012 : '2012',
				x.y2013 : '2013',
				x.y2014 : '2014',
				x.y2015 : '2015',
				x.y2016 : '2016',
				x.y2017 : '2017',
				x.y2018 : '2018',
				x.y2019 : '2019',
				x.y2020 : '2020',
				}
				for key, value in dic.iteritems():
					if x.receipt_type != 'expense' and dic[key] == self.tax_year.code:
						y.tax_deduct_link_id.create({
							'description' : x.description,
							'tax_type':x.receipt_type,
							'amount':key,
							'tax_deduct_id': y.id,
							})
	@api.multi
	def get_tax_rate(self):
		required_class = self.env['tax_rates_table.tax_rates_table'].search([('tax_year','=',self.tax_year.id)])
		tax_rate_book = required_class.business_rates_table_ids
		for x in tax_rate_book:
			if x.amount_from <= self.taxable_income <= x.amount_to:
				self.tax_rate = x.rate_of_tax