# -*- coding: utf-8 -*-
{
    'name': 'Sales Report Print',
    'version': '0.1',
    'summary': '',
    'sequence': 10,
    'description': """""",
    'category': 'sales',
    'author': 'IATS',
    'maintainer': 'IATS',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'sale_management',
        'report_xlsx'
    ],
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',  
        'report/sales_order_report.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
