# -*- coding: utf-8 -*-
from openerp import models, fields, api
from dateutil import relativedelta as rd
import datetime as dt

class hr_oms(models.Model):
    _inherit = 'hr.employee'
    age = fields.Char()
    oms_experience  = fields.Integer(string ="OMS Experience :")
    @api.onchange('birthday','family_id','employee_expert_id')
    def _onchange_things(self):
    	if(self.birthday):
    		difference = rd.relativedelta(dt.date(int(str(dt.datetime.now())[0:4]),int(str(dt.datetime.now())[5:7]),int(str(dt.datetime.now())[8:10])),dt.date(int(str(self.birthday)[0:4]),int(str(self.birthday)[5:7]),int(str(self.birthday)[8:])))
    		self.age = "{0.years}".format(difference)

    	no_of_kids = 0
    	for x in self.family_id:
    		if (x.kid_name):
    			no_of_kids +=1
    			self.children = no_of_kids

    	self.total_experience = sum(int(x.total_experience_diff) for x in self.employee_expert_id if x.total_experience_diff)
    	self.oms_experience   = sum(int(x.total_experience_diff) for x in self.employee_expert_id if x.total_experience_diff and (x.company == "OMS" or x.company =="oms"  or x.company =="Oms"))


class family_info(models.Model):
	_name = 'family_info'
	kid_name = fields.Char('Kid Name')
	sex = fields.Char('Sex')
	dob = fields.Date('Date of Birth')
	age = fields.Integer('Age')
	family_info_id = fields.Many2one('hr.employee','Family Information')

	@api.onchange('dob')
	def _onchange_dob(self):
		if(self.dob):
			difference = rd.relativedelta(dt.date(int(str(dt.datetime.now())[0:4]),int(str(dt.datetime.now())[5:7]),int(str(dt.datetime.now())[8:10])),dt.date(int(str(self.dob)[0:4]),int(str(self.dob)[5:7]),int(str(self.dob)[8:])))
			self.age = "{0.years}".format(difference)

class cost_centre(models.Model):
	_name = 'cost_centre.cost_centre'

	name = fields.Char()
	code = fields.Char()
	working_address = fields.Char('Working Address')