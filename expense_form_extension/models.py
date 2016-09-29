# # -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning

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

	@api.multi
	def advance_btn(self):

	    statement_recs =self.env['account.bank.statement'].search([('state','=','open')])
	    y=0
	    for x in statement_recs:
	    	y += 1
	    if y!=1:
	    	raise Warning('Multiple statements are open..Please Open only one')
	    else:
		    respected_tree =statement_recs.line_ids
		    x=0
		    for n in respected_tree:
		    	x=x+1
		    respected_tree.create({
		    	'sequence':x+1,
		    	'statement_id': statement_recs.id,
		    	'date' :self.date,
		    	'name': self.name,
		    	'employee':self.employee_id.id,
		    	'amount':self.advance
		    	})
	@api.multi
	def returned_btn(self):

	    statement_recs =self.env['account.bank.statement'].search([('state','=','open')])
	    y=0
	    for x in statement_recs:
	    	y += 1
	    if y!=1:
	    	raise Exception('Multiple statements are open..Please Open only one')
	    else:
		    respected_tree =statement_recs.line_ids
		    x=0
		    for n in respected_tree:
		    	x=x+1
		    respected_tree.create({
		    	'sequence':x+1,
		    	'statement_id': statement_recs.id,
		    	'date' :self.date,
		    	'name': self.name,
		    	'employee':self.employee_id.id,
		    	'amount':self.returned
		    	})
class expense_form_extension_1(models.Model):
	_inherit = 'account.bank.statement.line'
	employee = fields.Many2one('hr.employee')
	# expnse_id = fields.Many2one('hr.expense.expense')
	    