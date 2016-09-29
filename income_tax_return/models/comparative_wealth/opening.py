# -*- coding: utf-8 -*-
#####################################################
###########  Fields for WorkBook 'Opening' ##########
#####################################################

from openerp import models, fields, api

class opening(models.Model):
	_name = 'opening'
	description = fields.Char(string = "Description", required=True)
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

	receipt_type = fields.Selection([
            ('cash', 'Cash'),
            ('bank', 'Bank'),
            ])

	opening_id = fields.Many2one('comparative.wealth',
        ondelete='cascade', string="Wealth Reconciliation", required=True)