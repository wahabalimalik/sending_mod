# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# 
# 
# ---------------------------------------------------------------------
from openerp import models, fields, api

class capital_gain(models.Model):

	_name      = 'capital_gain.capital_gain'
	_inherit   = ['mail.thread', 'ir.needaction_mixin']

	name           = fields.Many2one('res.partner','Client Name', required=True)
	description    = fields.Many2one('cash_receipts_id','Description', required=True)
	year_purchase  = fields.Many2one('account.fiscalyear')
	year_sale      = fields.Many2one('account.fiscalyear')
	assets         = fields.Many2one('wealth.assets',domain="[('assets_id.name.id','=',name)]", required=True)
	sale_value     = fields.Float()
	purchase_value = fields.Float()
	capital_gain   = fields.Float()

	@api.onchange('sale_value','purchase_value')
	def _onchange_get_capital_gain(self):
		self.capital_gain = self.sale_value - self.purchase_value