# -*- coding: utf-8 -*-
{
    'name': "goal_leuwint",

    'summary': """
        Employees and Company Goals """,

    'description': """
        Goals for Employees
    """,

    'author': "Leuwint Technologies",
    'website': "https://leuwint.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Goal',
    'version': '1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
    ],
    'license': 'LGPL-3',
    'application':True,
    'auto_install': False,
    'installable': True,
}
