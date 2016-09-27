# -*- coding: utf-8 -*-
from openerp import models, fields, api

class firm_partner_analytics(models.Model):
    _inherit = 'account.analytic.line'

    firm_partner = fields.Many2one('res.partner')

    @api.multi
    def update_btn(self):
	    active_class =self.env['account.analytic.line'].search([])
	    for x in active_class:
        	x.firm_partner = x.account_id.custom_firm_partner.id
