from openerp import models, fields, api

# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------

from openerp import models, fields, api
class income_tax_returns(models.Model):
	_name    = 'income.tax.returns'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	state    = fields.Selection([
		('draft', 'Draft'),
        ('prepared', 'Prepared'),
        ('submitted', 'Submitted'),
        ],default='draft')
	name           = fields.Char(string="Name")
	group          = fields.Many2one('res.partner')
	client_name    = fields.Many2one('res.partner','Client Name', required=True)
	tax_year       = fields.Many2one('account.fiscalyear', 'Tax Year')
	description    = fields.Text('Description')
	period         = fields.Char('Period')
	unit_price     = fields.Float('Unit Price', required=True)
	prepared_by    = fields.Many2one('hr.employee', 'Prepared by')
	comparative_id = fields.Many2one('comparative.wealth', string = 'Comparative Wealth')
	_defaults      = { 'name': lambda self,cr,uid,context={}: self.pool.get('ir.sequence').get(cr, uid, 'income.tax.returns'), }

	@api.multi
	def queru_subbmitted_btn(self):
		invoice_recs            = self.env['account.invoice']
		account_id              = self.env['account.account'].search([('code','=',110200)])
		account_id_invoice_line = self.env['account.account'].search([('code','=',200000)])
		invoice_line_data       = [
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