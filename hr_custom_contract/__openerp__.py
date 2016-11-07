# -*- coding: utf-8 -*-
{
    'name': "hr_custom_contract",

    'summary': "Addition of bonus , loan etc etc fields in Contract Form",

    'description': "Fields are added in the Contract Form",

    'author': "Tax Tech",
    'website': "http://www.taxtech.com",


    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_payroll',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'wizard/employee_payslip_view.xml',
        'payslip_custom_report.xml'
    ],
}
