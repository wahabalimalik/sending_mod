# -*- coding: utf-8 -*-

from openerp import models, fields, api

class expense_form_extension(models.Model):
	_inherit = 'hr.expense.expense'

	advance = fields.Float()
	returned = fields.Float()
	net = fields.Float(readonly = True, compute="_compute_total_line")
	@api.multi
	def _compute_total_line(self):
		self.net = self.advance - self.returned
	@api.multi
	def my_btn(self):
		self.write({'state': 'paid'})	