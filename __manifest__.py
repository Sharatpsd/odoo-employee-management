{
    'name': 'Employee Management',
    'summary': 'Manage internal employee records',
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'author': 'Odoo Development Team',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
    ],
    'application': True,
    'installable': True,
}
