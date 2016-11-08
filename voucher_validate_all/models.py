# -*- coding: utf-8 -*-

from openerp import models, fields, api

class voucher_validate_all(models.Model):
    _inherit = 'account.voucher'

    @api.multi
    def validae_all(self):
    	all_v = self.env['account.voucher'].search([])
    	for x in all_v:
    		x.write({'state' : 'posted'})