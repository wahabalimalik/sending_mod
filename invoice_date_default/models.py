# -*- coding: utf-8 -*-
from openerp import models, fields, api

class invoice_date_default(models.Model):
    _inherit = 'account.invoice'

    invoice_date = fields.Date(default=fields.Date.today)