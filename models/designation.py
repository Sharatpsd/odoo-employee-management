from odoo import fields, models


class EmployeeDesignation(models.Model):
    _name = "employee.management.designation"
    _description = "Employee Designation"
    _order = "name"

    name = fields.Char(string="Designation", required=True)

    department_id = fields.Many2one(
        "employee.management.department",
        string="Department",
        ondelete="restrict",
    )

    active = fields.Boolean(default=True)

    employee_ids = fields.One2many(
        "employee.management.employee",
        "designation_id",
        string="Employees",
    )