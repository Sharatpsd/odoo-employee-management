from datetime import date, datetime
from dateutil.relativedelta import relativedelta

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

    manager_id = fields.Many2one(
        "employee.management.employee",
        string="Manager",
        related="department_id.manager_id",
        store=True,
        readonly=True,
    )

    designation_id = fields.Many2one(
        "employee.management.designation",
        string="Designation",
    )

    email = fields.Char(string="Email")

    phone = fields.Char(string="Phone")

    joining_date = fields.Date(string="Joining Date")

    probation_end_date = fields.Date(
        string="Probation End Date",
        compute="_compute_probation_end_date",
        store=True,
    )

    years_of_service = fields.Integer(
        string="Years of Service",
        compute="_compute_experience",
        store=True,
    )

    experience = fields.Char(
        string="Experience",
        compute="_compute_experience",
        store=True,
    )

    last_status_update = fields.Datetime(
        string="Last Status Update",
        readonly=True,
        default=fields.Datetime.now,
    )

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

    # --- Document Management ---
    document_ids = fields.One2many(
        "employee.management.document",
        "employee_id",
        string="Documents",
    )

    document_count = fields.Integer(
        string="Documents",
        compute="_compute_document_count",
    )

    def _compute_document_count(self):
        for rec in self:
            rec.document_count = self.env["employee.management.document"].search_count(
                [("employee_id", "=", rec.id)]
            )

    def action_view_documents(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Documents",
            "res_model": "employee.management.document",
            "view_mode": "list,form",
            "domain": [("employee_id", "=", self.id)],
            "context": {"default_employee_id": self.id},
        }

    # --- Asset Management ---
    asset_ids = fields.One2many(
        "employee.management.asset",
        "employee_id",
        string="Assets",
    )

    asset_count = fields.Integer(
        string="Assets",
        compute="_compute_asset_count",
    )

    def _compute_asset_count(self):
        for rec in self:
            rec.asset_count = self.env["employee.management.asset"].search_count(
                [("employee_id", "=", rec.id)]
            )

    def action_view_assets(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Assets",
            "res_model": "employee.management.asset",
            "view_mode": "list,form",
            "domain": [("employee_id", "=", self.id)],
            "context": {"default_employee_id": self.id},
        }

    _sql_constraints = [
        (
            "employee_code_unique",
            "unique(employee_code)",
            "Employee Code must be unique!",
        ),
    ]

    @api.depends("joining_date")
    def _compute_probation_end_date(self):
        for rec in self:
            if rec.joining_date:
                rec.probation_end_date = rec.joining_date + relativedelta(months=3)
            else:
                rec.probation_end_date = False

    @api.depends("joining_date")
    def _compute_experience(self):
        today = date.today()
        for rec in self:
            if rec.joining_date:
                delta = relativedelta(today, rec.joining_date)
                rec.years_of_service = max(0, delta.years)
                years_str = f"{delta.years} Year{'s' if delta.years != 1 else ''}"
                months_str = f"{delta.months} Month{'s' if delta.months != 1 else ''}"
                rec.experience = f"{years_str} {months_str}"
            else:
                rec.years_of_service = 0
                rec.experience = "0 Years 0 Months"

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
        invalid_email_recs = self.filtered(
            lambda r: r.email and "@" not in r.email
        )
        if invalid_email_recs:
            raise ValidationError(
                "Please enter a valid email address."
            )
    @api.model_create_multi
    def create(self, vals_list):
        
        for vals in vals_list:
            if vals.get("employee_code", "New") == "New":
                vals["employee_code"] = (
                    self.env["ir.sequence"].next_by_code(
                        "employee.management.employee"
                    ) or "New"
                )

        return super().create(vals_list)

    def action_confirm(self):
        self.filtered(lambda r: r.status == "draft").write({
            "status": "confirmed",
            "last_status_update": fields.Datetime.now(),
        })

    def action_activate(self):
        self.filtered(lambda r: r.status == "confirmed").write({
            "status": "active",
            "last_status_update": fields.Datetime.now(),
        })

    def action_leave(self):
        self.filtered(lambda r: r.status == "active").write({
            "status": "leave",
            "last_status_update": fields.Datetime.now(),
        })

    def action_resign(self):
        self.write({
            "status": "resigned",
            "last_status_update": fields.Datetime.now(),
        })

    def action_reset_draft(self):
        self.write({
            "status": "draft",
            "last_status_update": fields.Datetime.now(),
        })

    def get_employee_summary_stats(self):
        """Returns statistical metrics for the recordset.
        Uses list, tuple, set, dict, and list comprehension for real record analytics.
        """
        # Set comprehension for unique department names
        unique_departments = {
            emp.department_id.name for emp in self if emp.department_id
        }

        # List comprehension for active employee names
        active_employee_names = [
            emp.name for emp in self.filtered(lambda e: e.status == "active")
        ]

        # Tuple for summary metrics (total, active_count, dept_count)
        metrics_tuple = (len(self), len(active_employee_names), len(unique_departments))

        # Dictionary comprehension mapping department names to employee counts
        department_distribution = {
            dept_name: len([e for e in self if e.department_id.name == dept_name])
            for dept_name in unique_departments
        }

        return {
            "metrics_tuple": metrics_tuple,
            "unique_departments": list(unique_departments),
            "active_employees": active_employee_names,
            "department_distribution": department_distribution,
        }

    def action_bulk_activate_with_savepoint(self):
        """Bulk activates employees using PostgreSQL savepoints.
        If an individual employee fails validation (e.g. resigned status or missing department),
        the savepoint rolls back only that employee's changes without rolling back successful ones.
        """
        success_count = 0
        failed_employees = []

        for rec in self:
            try:
                with self.env.cr.savepoint():
                    if rec.status == "resigned":
                        raise ValidationError(
                            f"Resigned employee '{rec.name}' cannot be reactivated directly."
                        )
                    if not rec.department_id:
                        raise ValidationError(
                            f"Employee '{rec.name}' must belong to a department before activation."
                        )

                    rec.write({
                        "status": "active",
                        "last_status_update": fields.Datetime.now(),
                    })
                    success_count += 1
            except Exception as err:
                failed_employees.append((rec.name, str(err)))

        message = f"Successfully activated {success_count} employee(s)."
        if failed_employees:
            failures_str = ", ".join([f"{name}: {reason}" for name, reason in failed_employees])
            message += f" Failures ({len(failed_employees)}): {failures_str}"

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": "Bulk Activation Result",
                "message": message,
                "type": "warning" if failed_employees else "success",
                "sticky": bool(failed_employees),
            },
        }