# -*- coding: utf-8 -*-
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': 10,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'license': 'LGPL-3',
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
