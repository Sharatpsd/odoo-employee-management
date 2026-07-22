from odoo import api, fields, models


class EmployeeDepartment(models.Model):
    _name = "employee.management.department"
    _description = "Employee Department"
    _order = "name"

    name = fields.Char(string="Department Name", required=True)
    code = fields.Char(string="Department Code")
    active = fields.Boolean(default=True)

    manager_id = fields.Many2one(
        "employee.management.employee",
        string="Manager"
    )

    employee_ids = fields.One2many(
        "employee.management.employee",
        "department_id",
        string="Employees",
    )

    employee_count = fields.Integer(
        string="Employee Count",
        compute="_compute_employee_count",
    )

    @api.depends("employee_ids")
    def _compute_employee_count(self):
        data = self.env["employee.management.employee"]._read_group(
            domain=[("department_id", "in", self.ids)],
            groupby=["department_id"],
            aggregates=["__count"],
        )
        count_map = {department.id: count for department, count in data}
        for rec in self:
            rec.employee_count = count_map.get(rec.id, 0)

    def action_view_employees(self):
        self.ensure_one()
        return {
            "name": "Employees",
            "type": "ir.actions.act_window",
            "res_model": "employee.management.employee",
            "view_mode": "kanban,list,form",
            "domain": [("department_id", "=", self.id)],
            "context": {"default_department_id": self.id},
        }