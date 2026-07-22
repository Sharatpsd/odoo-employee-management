from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EmployeeAttendance(models.Model):
    _name = "employee.management.attendance"
    _description = "Employee Attendance"
    _order = "check_in desc"

    employee_id = fields.Many2one(
        "employee.management.employee",
        string="Employee",
        required=True,
        ondelete="cascade",
    )

    check_in = fields.Datetime(
        string="Check In",
        default=fields.Datetime.now,
        required=True,
    )

    check_out = fields.Datetime(string="Check Out")

    worked_hours = fields.Float(
        string="Worked Hours",
        compute="_compute_worked_hours",
        store=True,
    )

    status = fields.Selection(
        [
            ("checked_in", "Checked In"),
            ("checked_out", "Checked Out"),
        ],
        string="Status",
        compute="_compute_status",
        store=True,
    )

    @api.depends("check_in", "check_out")
    def _compute_worked_hours(self):
        for rec in self:
            if rec.check_in and rec.check_out:
                delta = rec.check_out - rec.check_in
                rec.worked_hours = max(0.0, round(delta.total_seconds() / 3600.0, 2))
            else:
                rec.worked_hours = 0.0

    @api.depends("check_in", "check_out")
    def _compute_status(self):
        for rec in self:
            if rec.check_in and not rec.check_out:
                rec.status = "checked_in"
            else:
                rec.status = "checked_out"

    @api.constrains("check_in", "check_out")
    def _check_validity(self):
        for rec in self:
            if rec.check_in and rec.check_out and rec.check_out < rec.check_in:
                raise ValidationError("Check Out time cannot be earlier than Check In time.")

    def action_check_out(self):
        for rec in self:
            if not rec.check_out:
                rec.check_out = fields.Datetime.now()
