# -*- coding: utf-8 -*-

{
    'name': "Income Tax Returns",

    'summary': "Income Tax Return",

    'description': "Income Tax Return",

    'author': "Ali",
    'website': "http://oxenlab.com",


    # any module necessary for this one to work correctly
    'depends': ['base','sale','hr',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'sequence/sequence.xml',
        'sequence/sequence1.xml',
        'wizards/wizards.xml'
    ],
    'installable' : True,
}