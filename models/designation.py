from odoo import api, fields, models


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

    employee_count = fields.Integer(
        string="Employee Count",
        compute="_compute_employee_count",
    )

    @api.depends("employee_ids")
    def _compute_employee_count(self):
        data = self.env["employee.management.employee"]._read_group(
            domain=[("designation_id", "in", self.ids)],
            groupby=["designation_id"],
            aggregates=["__count"],
        )
        count_map = {designation.id: count for designation, count in data}
        for rec in self:
            rec.employee_count = count_map.get(rec.id, 0)

    def action_view_employees(self):
        self.ensure_one()
        return {
            "name": "Employees",
            "type": "ir.actions.act_window",
            "res_model": "employee.management.employee",
            "view_mode": "kanban,list,form",
            "domain": [("designation_id", "=", self.id)],
            "context": {"default_designation_id": self.id},
        }