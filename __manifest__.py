# -*- coding: utf-8 -*-
{
    'name': "Open-Academy",

    'summary': """Управлять тренировками""",

    'description': """
        Модуль Open Academy для управления обучением:
            - обучающие курсы
            - тренировки
            - регистрация участников
    """,

    'author': "ztn",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'license': "LGPL-3", #  по умолчанию

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
