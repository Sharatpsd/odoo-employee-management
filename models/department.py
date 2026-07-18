from odoo import fields, models


class EmployeeDepartment(models.Model):
    _name = "employee.management.department"
    _description = "Employee Department"
    _order = "name"

    name = fields.Char(string="Department Name", required=True)
    code = fields.Char(string="Department Code")
    active = fields.Boolean(default=True)

    employee_ids = fields.One2many(
        "employee.management.employee",
        "department_id",
        string="Employees",
    )