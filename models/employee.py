from odoo import fields, models


class EmployeeManagementEmployee(models.Model):
    _name = 'employee.management.employee'
    _description = 'Managed Employee'
    _order = 'name'

    name = fields.Char(required=True, index=True)
    employee_code = fields.Char(required=True, copy=False, index=True)
    email = fields.Char()
    phone = fields.Char()
    department = fields.Char()
    job_title = fields.Char()
    joining_date = fields.Date()
    active = fields.Boolean(default=True)
    notes = fields.Text()

    _employee_code_unique = models.Constraint(
        'UNIQUE(employee_code)',
        'Employee code must be unique.',
    )
