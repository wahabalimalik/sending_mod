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
	less_rebates            = fields.Float(string="Less: Rebates")
	taxable_income          = fields.Float(string="Taxable Income")
	tax_rate                = fields.Float(string="Rate of Tax")
	tax_liability           = fields.Float(string="Tax Liability")
	portion_of_minimum_tax  = fields.Float(string="Portion of Minimum Tax")
	payable_tax             = fields.Float(string="Total Tax Payable")
	tax_adjust              = fields.Float(string="Tax deducted Adjustable")
	tax_deduct_min          = fields.Float(string="Tax deducted Minimum")
	total_tax               = fields.Float(string="Total Tax")
	refund_adjust           = fields.Float(string="Refund Adjustment")
	tax_ratio               = fields.Float(string="Tax Payable/ (Refundable)")

	income_under_ftr        = fields.Float(string="Income under FTR")
	tax_deduct              = fields.Float(string="Tax deducted")

	description             = fields.Text()
	amount                  = fields.Float()

	tax_computation_ntr_id  = fields.One2many('income.under.ntr', 'income_under_ntr_id')
	tax_computation_ftr_id  = fields.One2many('income.under.ftr', 'income_under_ftr_id')
	tax_deduct_link_id      = fields.One2many('tax.deduct', 'tax_deduct_id')

	@api.onchange('tax_computation_ntr_id')
	def _onchange_ntr_id(self):
		self.income_under_ntr = sum(line.amount for line in self.tax_computation_ntr_id if line.tax_type!='exempt')

	@api.onchange('tax_computation_ftr_id')
	def _onchange_ftr_id(self):
		self.income_under_ftr = sum(line.amount for line in self.tax_computation_ftr_id)
		self.tax_deduct = sum(line.tax for line in self.tax_computation_ftr_id)


	@api.onchange('tax_deduct_link_id')
	def _onchange_tax_deduct(self):
		self.tax_adjust = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type=='adjustable')
		self.tax_deduct_min = sum(line.amount for line in self.tax_deduct_link_id if line.tax_type=='minimum')
				
	@api.onchange('income_under_ntr','less_rebates','tax_rate','portion_of_minimum_tax','tax_adjust','tax_deduct_min','refund_adjust')
	def onchange_assesment_form_field(self):
		self.taxable_income = self.income_under_ntr - self.less_rebates
		self.tax_liability  = self.taxable_income * self.tax_rate
		self.payable_tax    = self.tax_liability + self.portion_of_minimum_tax
		self.total_tax      = self.payable_tax - self.tax_adjust
		self.total_tax      = self.total_tax - self.tax_deduct_min
		self.tax_ratio      = self.total_tax - self.refund_adjust