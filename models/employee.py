from datetime import date

from odoo import api, fields, models
from odoo.exceptions import ValidationError



class EmployeeManagementEmployee(models.Model):
    _name = "employee.management.employee"
    _description = "Managed Employee"
    _order = "name"

    employee_code = fields.Char(
        string="Employee Code",
        required=True,
        copy=False,
        readonly=True,
        default="New",
    )

    name = fields.Char(
        string="Employee Name",
        required=True,
        index=True,
    )

    image_1920 = fields.Image(
        string="Employee Photo",
        max_width=1920,
        max_height=1920,
    )

    department_id = fields.Many2one(
        "employee.management.department",
        string="Department",
    )

    designation_id = fields.Many2one(
        "employee.management.designation",
        string="Designation",
    )

    email = fields.Char(string="Email")

    phone = fields.Char(string="Phone")

    joining_date = fields.Date(string="Joining Date")

    date_of_birth = fields.Date(string="Date of Birth")

    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True,
    )

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("active", "Active"),
            ("leave", "On Leave"),
            ("resigned", "Resigned"),
        ],
        string="Status",
        default="draft",
    )

    active = fields.Boolean(default=True)

    notes = fields.Text(string="Notes")

    _sql_constraints = [
        (
            "employee_code_unique",
            "unique(employee_code)",
            "Employee Code must be unique!",
        ),
    ]

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()

        for rec in self:
            if rec.date_of_birth:
                rec.age = (
                    today.year
                    - rec.date_of_birth.year
                    - (
                        (today.month, today.day)
                        < (
                            rec.date_of_birth.month,
                            rec.date_of_birth.day,
                        )
                    )
                )
            else:
                rec.age = 0

    @api.constrains("email")
    def _check_email(self):
        for rec in self:
            if rec.email and "@" not in rec.email:
                raise ValidationError(
                    "Please enter a valid email address."
                )

    @api.model
    def create(self, vals):
        if vals.get("employee_code", "New") == "New":
            vals["employee_code"] = (
                self.env["ir.sequence"].next_by_code(
                    "employee.management.employee"
                )
                or "New"
            )

        return super().create(vals)

    def action_confirm(self):
        self.status = "confirmed"

    def action_activate(self):
        self.status = "active"

    def action_leave(self):
        self.status = "leave"

    def action_resign(self):
        self.status = "resigned"

    def action_reset_draft(self):
        self.status = "draft"