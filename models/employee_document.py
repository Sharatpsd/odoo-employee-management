from odoo import api, fields, models


class EmployeeDocument(models.Model):
    _name = "employee.management.document"
    _description = "Employee Document"
    _order = "expiry_date desc, id desc"

    name = fields.Char(
        string="Document Name",
        required=True,
    )

    employee_id = fields.Many2one(
        "employee.management.employee",
        string="Employee",
        required=True,
        ondelete="cascade",
        index=True,
    )

    doc_type = fields.Selection(
        [
            ("nid", "National ID"),
            ("passport", "Passport"),
            ("cv", "Curriculum Vitae"),
            ("certificate", "Certificate"),
            ("contract", "Contract"),
            ("other", "Other"),
        ],
        string="Document Type",
        required=True,
        default="other",
    )

    attachment = fields.Binary(
        string="Attachment",
        required=True,
    )
    file_name = fields.Char(string="File Name")

    expiry_date = fields.Date(string="Expiry Date")

    status = fields.Selection(
        [
            ("valid", "Valid"),
            ("expired", "Expired"),
        ],
        string="Status",
        compute="_compute_status",
        store=True,
    )

    notes = fields.Text(string="Notes")

    @api.depends("expiry_date")
    def _compute_status(self):
        today = fields.Date.context_today(self)
        for rec in self:
            if rec.expiry_date and rec.expiry_date < today:
                rec.status = "expired"
            else:
                rec.status = "valid"
