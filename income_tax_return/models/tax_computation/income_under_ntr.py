# -*- coding: utf-8 -*-
###############################################################
########### Fields for WorkBook "Income Under NTR" ##########
###############################################################

from openerp import models, fields, api

class income_under_ntr(models.Model):
	_name = 'income.under.ntr'

	description = fields.Char()
	amount      = fields.Float()
	tax_type    = fields.Selection([
            ('taxable', 'Taxable'),
            ('exempt', 'Exempt'),
            ('salary', 'Salary'),
            ])

	income_under_ntr_id = fields.Many2one('tax.computation',
        ondelete='cascade', required=True)