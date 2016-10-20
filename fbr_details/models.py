# -*- coding: utf-8 -*-

from openerp import models, fields, api

class fbr_details(models.Model):
    _inherit   = 'res.partner'

    user_id             = fields.Char(string="User Id")
    password            = fields.Char()
    pin                 = fields.Char()
    cell_no             = fields.Integer(string="Cell No")
    email               = fields.Char()
    registered_address  = fields.Char(string="Registered Address")
    address_1           = fields.Char()
    address_2           = fields.Char()