# -*- coding: utf-8 -*-
#####################################################################
###########  Fields for WorkBook 'Capital Working' ##########
#####################################################################

from openerp import models, fields, api

class capital_working(models.Model):
	_name = 'capital_working.capital_working'
	business = fields.Char(string = "Business", required=True)
	y2005 = fields.Float(string = "2005")
	y2006 = fields.Float(string = "2006")
	y2007 = fields.Float(string = "2007")
	y2008 = fields.Float(string = "2008")
	y2009 = fields.Float(string = "2009")
	y2010 = fields.Float(string = "2010")
	y2011 = fields.Float(string = "2011")
	y2012 = fields.Float(string = "2012")
	y2013 = fields.Float(string = "2013")
	y2014 = fields.Float(string = "2014")
	y2015 = fields.Float(string = "2015")
	y2016 = fields.Float(string = "2016")
	y2017 = fields.Float(string = "2017")
	y2018 = fields.Float(string = "2018")
	y2019 = fields.Float(string = "2019")
	y2020 = fields.Float(string = "2020")
	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	capital_working_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Capital Working", required=True)

class capital_working_sub(models.Model):
	_name = 'capital_working_sub.capital_working_sub'
	business = fields.Char(string = "Business", required=True)
	capital_working_id = fields.One2many('capital_working_sub_sub.capital_working_sub_sub', 'capital_working_sub_id')

class capital_working_sub_sub(models.Model):
	_name = 'capital_working_sub_sub.capital_working_sub_sub'
	description = fields.Char(required=True)
	y2005 = fields.Float(string = "2005")
	y2006 = fields.Float(string = "2006")
	y2007 = fields.Float(string = "2007")
	y2008 = fields.Float(string = "2008")
	y2009 = fields.Float(string = "2009")
	y2010 = fields.Float(string = "2010")
	y2011 = fields.Float(string = "2011")
	y2012 = fields.Float(string = "2012")
	y2013 = fields.Float(string = "2013")
	y2014 = fields.Float(string = "2014")
	y2015 = fields.Float(string = "2015")
	y2016 = fields.Float(string = "2016")
	y2017 = fields.Float(string = "2017")
	y2018 = fields.Float(string = "2018")
	y2019 = fields.Float(string = "2019")
	y2020 = fields.Float(string = "2020")
	sequence = fields.Integer(string ='Sequence')
	_order   = 'sequence'

	capital_working_sub_id = fields.Many2one('capital_working_sub.capital_working_sub',
        ondelete='cascade', string="Capital Working Sub", required=True)