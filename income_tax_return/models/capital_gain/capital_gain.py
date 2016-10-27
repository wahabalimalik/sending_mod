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
	description    = fields.Many2one('receipts',string = "Description", required=True)
	year_purchase  = fields.Many2one('account.fiscalyear')
	year_sale      = fields.Many2one('account.fiscalyear')
	assets         = fields.Many2one('wealth.assets', required=True)
	purchase_value = fields.Float()
	sale_value     = fields.Float()
	capital_gain   = fields.Float()
