{
    "name": "Employee Management",
    "version": "19.0.1.0.0",
    "summary": "Employee Management System",
    "author": "Sharat Acharja",
    "category": "Human Resources",
    "license": "LGPL-3",
    "depends": [
        "base",
    ],
 "data": [
    "security/ir.model.access.csv",
    "data/employee_sequence.xml",

    "views/department_views.xml",
    "views/designation_views.xml",
    "views/employee_views.xml",
    "views/employee_kanban_views.xml",
    "views/menu_views.xml",
],
    "application": True,
    "installable": True,
}