# # -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.exceptions import Warning

class expense_form_extension(models.Model):

	_inherit = 'hr.expense.expense'

	hide_button1 = fields.Boolean()
	hide_button2 = fields.Boolean()
	advance      = fields.Float()
	returned     = fields.Float()
	net          = fields.Float(readonly = True, compute="_compute_total_line")
	
	@api.multi
	def _compute_total_line(self):
		self.net = self.advance - self.returned

	@api.multi
	def my_btn(self):
		self.write({'state': 'paid'})

	@api.multi
	def advance_btn(self):

		self.hide_button1=True
		statement_recs =self.env['account.bank.statement'].search([('state','=','open')])
		y=0
		for x in statement_recs:
			y += 1
		if y>1:
			raise Warning('Multiple Cash Books are open..Only one required')
		elif y<1:
			raise Warning('No Cash Book is open!')
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
		    	'amount':self.advance *-1
		    	})
	
	@api.multi
	def returned_btn(self):
		self.hide_button2=True
		statement_recs =self.env['account.bank.statement'].search([('state','=','open')])
		y=0
		for x in statement_recs:
			y += 1
		if y>1:
			raise Warning('Multiple Cash Books are open..Only one required')
		elif y<1:
			raise Warning('No Cash Book is open!')
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

class loan_management(models.Model):
	_inherit = 'hr.expense.expense'

	loan            = fields.Boolean()
	loan_start_date = fields.Date('Start Date', required=True)
	loan_end_date   = fields.Date('End Date', required=True)
	installments    = fields.Integer(string="No of Installment")
	loan_paid       = fields.Float(string="Loan Paid")
	loan_remaining  = fields.Float(string="Loan Remaining")

	pringle         = fields.One2many('loan.1122','cringle')

	@api.onchange('advance','loan_paid')
	@api.depends('advance','loan_paid','loan')
	def _onchange_amount(self):
		if self.loan != False:
			self.loan_remaining= self.advance - self.loan_paid
		return

	@api.multi
	def show_btn(self):
		self.pringle.unlink()
		nn = str(self.employee_id.name)
		active_class =self.env['hr.payslip.line'].search([('employee_id','=',nn)])
		for x in active_class:
			start_date = str(x.slip_id.date_from)
			end_date = str(x.slip_id.date_to)
			if x.code == 'BASIC' and int(start_date[:4]) >= int(self.loan_start_date[:4]) and int(start_date[5:7]) >= int(self.loan_start_date[5:7]) and int(start_date[8:]) >= int(self.loan_start_date[8:]) and int(end_date[:4]) <= int(self.loan_end_date[:4]) and int(end_date[5:7]) <= int(self.loan_end_date[5:7]) and int(end_date[8:]) <= int(self.loan_end_date[8:]) :
				for y in self:
					y.pringle.create({
						'name'     : x.name,
						'date'     : x.date,
						'slip_id'  : x.slip_id.id,
						'amount'   : x.amount,
						'cringle'  : y.id
						})
class loan_management_1122(models.Model):
	_name = 'loan.1122'
	name = fields.Char()
	date = fields.Date()
	slip_id = fields.Integer()
	amount = fields.Float()
	cringle  = fields.Many2one('hr.expense.expense',
        ondelete='cascade')
class loan_management_1(models.Model):
	_inherit = 'hr.payslip.line'
	date = fields.Date()