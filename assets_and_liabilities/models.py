# -*- coding: utf-8 -*-

from openerp import models, fields, api

class assets_and_liabilities(models.Model):
    _name = 'assets_and_liabilities.assets_and_liabilities'

    name = fields.Char()
    code = fields.Char()