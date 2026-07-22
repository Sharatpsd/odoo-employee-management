from odoo import api, fields, models


class EmployeeAsset(models.Model):
    _name = "employee.management.asset"
    _description = "Employee Asset"
    _order = "assigned_date desc, id desc"

    name = fields.Char(
        string="Asset Name",
        required=True,
    )

    asset_code = fields.Char(
        string="Asset Code",
        required=True,
        copy=False,
    )

    employee_id = fields.Many2one(
        "employee.management.employee",
        string="Employee",
        required=True,
        ondelete="restrict",
        index=True,
    )

    category = fields.Selection(
        [
            ("laptop", "Laptop"),
            ("desktop", "Desktop"),
            ("phone", "Mobile Phone"),
            ("tablet", "Tablet"),
            ("vehicle", "Vehicle"),
            ("furniture", "Furniture"),
            ("accessory", "Accessory"),
            ("other", "Other"),
        ],
        string="Asset Category",
        required=True,
        default="other",
    )

    serial_number = fields.Char(string="Serial Number")

    purchase_date = fields.Date(string="Purchase Date")

    assigned_date = fields.Date(
        string="Assigned Date",
        default=fields.Date.context_today,
    )

    return_date = fields.Date(string="Return Date")

    status = fields.Selection(
        [
            ("available", "Available"),
            ("assigned", "Assigned"),
            ("returned", "Returned"),
            ("damaged", "Damaged"),
            ("disposed", "Disposed"),
        ],
        string="Status",
        default="assigned",
        required=True,
    )

    notes = fields.Text(string="Notes")

    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            "asset_code_unique",
            "unique(asset_code)",
            "Asset Code must be unique!",
        ),
    ]

    @api.onchange("return_date")
    def _onchange_return_date(self):
        if self.return_date:
            self.status = "returned"
