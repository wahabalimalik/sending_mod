# -*- coding: utf-8 -*-

from openerp import models, fields, api
class hr_custom_contract(models.Model):
	_inherit = 'hr.contract'
	bonus = fields.Float('Bonus')
	loan_and_advance = fields.Float('Loan & Advance')
	medical_opd = fields.Float('Medical OPD')
	fuel_other = fields.Float('Fuel/others')
	overtime = fields.Float('Overtime')
	sr_other = fields.Float('SR/other')

class hr_custom_employee(models.Model):
	#_name = 'hr.custom.employee'
	_inherit = 'hr.employee'
<<<<<<< HEAD
	show_engineer = fields.Boolean('Is a Engineer ?')
	engineer = fields.Char('PEC #', size=64)
	blood_group = fields.Char('Blood Group', size=10)
=======
	family_id = fields.One2many('family_info','family_info_id',string='Details')
	spouse_name = fields.Char('Spouse Name')
	s_dob = fields.Date('Date of Birth')
	s_contact = fields.Char('Spouse Contact')
	s_cnic = fields.Char('CNIC #')

>>>>>>> e940c95a0b3b071770125acc2c0208fde1719b74
	


class family_info(models.Model):
    _name = 'family_info'
    kid_name = fields.Char('Kid Name')
    sex = fields.Char('Sex')
    dob = fields.Date('Date of Birth')
    age = fields.Integer('Age')
    family_info_id = fields.Many2one('hr.employee','Family Information')
