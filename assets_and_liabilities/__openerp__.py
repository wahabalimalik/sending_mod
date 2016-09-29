# -*- coding: utf-8 -*-
{
    'name': "assets_and_liabilities",

    'summary': """
        Assets and Liabilities""",

    'description': """
        Assets and Liabilities
    """,

    'author': "Ali",
    'website': "http://oxenlab.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','income_tax_return'],

    # always loaded
    'data': [
        'templates.xml',
    ],
}