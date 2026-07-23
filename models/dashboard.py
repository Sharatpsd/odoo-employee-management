# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.fields import Date


class EmployeeDashboard(models.TransientModel):
    """Transient model powering the Employee Management Enterprise Dashboard.

    All KPI values are computed live inside ``default_get`` so the
    dashboard always reflects the current state of the database the
    moment it is opened, without requiring any manual refresh action.

    New KPIs can be added by:
        1. Adding a new ``fields.Integer`` below in the relevant section.
        2. Populating it inside the matching ``_get_*_stats`` helper.
        3. Merging its dict into ``default_get``.
    """

    _name = "employee.management.dashboard"
    _description = "Employee Management Enterprise Dashboard"

    # ------------------------------------------------------------------
    # Employee Statistics
    # ------------------------------------------------------------------
    total_employee = fields.Integer(string="Total Employees", readonly=True)
    active_employee = fields.Integer(string="Active Employees", readonly=True)
    draft_employee = fields.Integer(string="Draft Employees", readonly=True)
    confirmed_employee = fields.Integer(string="Confirmed Employees", readonly=True)
    leave_employee = fields.Integer(string="Employees On Leave", readonly=True)
    resigned_employee = fields.Integer(string="Resigned Employees", readonly=True)

    # ------------------------------------------------------------------
    # Department Statistics
    # ------------------------------------------------------------------
    total_department = fields.Integer(string="Total Departments", readonly=True)

    # ------------------------------------------------------------------
    # Asset Statistics
    # ------------------------------------------------------------------
    total_asset = fields.Integer(string="Total Assets", readonly=True)
    assigned_asset = fields.Integer(string="Assigned Assets", readonly=True)
    available_asset = fields.Integer(string="Available Assets", readonly=True)
    lost_asset = fields.Integer(string="Lost Assets", readonly=True)
    damaged_asset = fields.Integer(string="Damaged Assets", readonly=True)

    # ------------------------------------------------------------------
    # Document Statistics
    # ------------------------------------------------------------------
    total_document = fields.Integer(string="Total Documents", readonly=True)
    verified_document = fields.Integer(string="Verified Documents", readonly=True)
    pending_document = fields.Integer(string="Pending Documents", readonly=True)
    expired_document = fields.Integer(string="Expired Documents", readonly=True)

    # ------------------------------------------------------------------
    # Attendance Statistics
    # ------------------------------------------------------------------
    total_attendance = fields.Integer(string="Total Attendance", readonly=True)
    present_today = fields.Integer(string="Present Today", readonly=True)
    absent_today = fields.Integer(string="Absent Today", readonly=True)
    late_today = fields.Integer(string="Late Today", readonly=True)

    # ------------------------------------------------------------------
    # Extra KPIs
    # ------------------------------------------------------------------
    joined_this_month = fields.Integer(string="Employees Joined This Month", readonly=True)
    joined_this_year = fields.Integer(string="Employees Joined This Year", readonly=True)
    new_employees_today = fields.Integer(string="New Employees Today", readonly=True)

    # ------------------------------------------------------------------
    # Section helpers - each helper issues the minimum number of ORM
    # calls required for its section (grouped counts via _read_group
    # instead of one search_count() per status).
    # ------------------------------------------------------------------
    def _get_employee_stats(self):
        """Compute all employee-related KPIs using a single grouped query.

        :return: dict of employee KPI values.
        :rtype: dict
        """
        employee_model = self.env["employee.management.employee"]

        # Single query grouped by status avoids one search_count() call
        # per status value.
        status_groups = employee_model._read_group(
            domain=[],
            groupby=["status"],
            aggregates=["__count"],
        )
        status_counts = {status: count for status, count in status_groups if status}
        total_employee = sum(status_counts.values())

        today = Date.context_today(self)
        month_start = today.replace(day=1)
        year_start = today.replace(month=1, day=1)

        # Employee model is expected to expose a "joining_date" field.
        # If it does not exist, joined_* KPIs safely fall back to 0.
        joined_stats = {
            "joined_this_month": 0,
            "joined_this_year": 0,
            "new_employees_today": 0,
        }
        if "joining_date" in employee_model._fields:
            joined_stats["joined_this_month"] = employee_model.search_count(
                [("joining_date", ">=", month_start)]
            )
            joined_stats["joined_this_year"] = employee_model.search_count(
                [("joining_date", ">=", year_start)]
            )
            joined_stats["new_employees_today"] = employee_model.search_count(
                [("joining_date", "=", today)]
            )

        return {
            "total_employee": total_employee,
            "active_employee": status_counts.get("active", 0),
            "draft_employee": status_counts.get("draft", 0),
            "confirmed_employee": status_counts.get("confirmed", 0),
            "leave_employee": status_counts.get("leave", 0),
            "resigned_employee": status_counts.get("resigned", 0),
            "joined_this_month": joined_stats["joined_this_month"],
            "joined_this_year": joined_stats["joined_this_year"],
            "new_employees_today": joined_stats["new_employees_today"],
        }

    def _get_department_stats(self):
        """Compute department-related KPIs.

        :return: dict of department KPI values.
        :rtype: dict
        """
        department_model = self.env["employee.management.department"]
        return {
            "total_department": department_model.search_count([]),
        }

    def _get_asset_stats(self):
        """Compute all asset-related KPIs using a single grouped query.

        :return: dict of asset KPI values.
        :rtype: dict
        """
        asset_model = self.env["employee.management.asset"]

        status_groups = asset_model._read_group(
            domain=[],
            groupby=["status"],
            aggregates=["__count"],
        )
        status_counts = {status: count for status, count in status_groups if status}

        return {
            "total_asset": sum(status_counts.values()),
            "assigned_asset": status_counts.get("assigned", 0),
            "available_asset": status_counts.get("available", 0),
            "lost_asset": status_counts.get("lost", 0),
            "damaged_asset": status_counts.get("damaged", 0),
        }

    def _get_document_stats(self):
        """Compute all document-related KPIs using a single grouped query.

        :return: dict of document KPI values.
        :rtype: dict
        """
        document_model = self.env["employee.management.document"]

        status_groups = document_model._read_group(
            domain=[],
            groupby=["status"],
            aggregates=["__count"],
        )
        status_counts = {status: count for status, count in status_groups if status}

        return {
            "total_document": sum(status_counts.values()),
            "verified_document": status_counts.get("verified", 0),
            "pending_document": status_counts.get("pending", 0),
            "expired_document": status_counts.get("expired", 0),
        }

    def _get_attendance_stats(self):
        """Compute today's attendance-related KPIs.

        Safely returns all zeros if the attendance model is not
        installed or contains no records for today.

        :return: dict of attendance KPI values.
        :rtype: dict
        """
        attendance_stats = {
            "total_attendance": 0,
            "present_today": 0,
            "absent_today": 0,
            "late_today": 0,
        }

        if "employee.management.attendance" not in self.env:
            return attendance_stats

        attendance_model = self.env["employee.management.attendance"]
        today = Date.context_today(self)

        attendance_stats["total_attendance"] = attendance_model.search_count([])

        today_status_groups = attendance_model._read_group(
            domain=[("attendance_date", "=", today)],
            groupby=["status"],
            aggregates=["__count"],
        )
        today_status_counts = {
            status: count for status, count in today_status_groups if status
        }

        attendance_stats["present_today"] = today_status_counts.get("present", 0)
        attendance_stats["absent_today"] = today_status_counts.get("absent", 0)
        attendance_stats["late_today"] = today_status_counts.get("late", 0)

        return attendance_stats

    # ------------------------------------------------------------------
    # Default values
    # ------------------------------------------------------------------
    @api.model
    def default_get(self, fields_list):
        """Populate the dashboard with live statistics on every open.

        Delegates each KPI group to its dedicated helper method so that
        related logic stays grouped, readable, and easy to extend with
        new KPIs in the future without touching unrelated sections.

        :param list fields_list: fields requested by the view.
        :return: default values dictionary.
        :rtype: dict
        """
        res = super().default_get(fields_list)

        res.update(self._get_employee_stats())
        res.update(self._get_department_stats())
        res.update(self._get_asset_stats())
        res.update(self._get_document_stats())
        res.update(self._get_attendance_stats())

        return res