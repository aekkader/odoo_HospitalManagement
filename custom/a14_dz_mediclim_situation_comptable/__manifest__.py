# -*- coding: utf-8 -*-
{
    'name': "Mediclim Situation Comptable",

    'summary': """
        a14_dz_mediclim_situation_comptable""",

    'description': """
        a14_dz_mediclim_situation_comptable""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'a14_dz_mediclim'],

    # always loaded
    'data': [
        'views/situation_comptable.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
