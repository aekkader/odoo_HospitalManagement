# -*- coding: utf-8 -*-
{
    'name': "a14_dz_mediclim_situation_client",

    'summary': """
        a14_dz_mediclim_situation_client""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','a14_dz_mediclim_situation_comptable'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/situation_client.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
