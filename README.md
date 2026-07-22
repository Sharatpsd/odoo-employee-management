<h1 align="center">Employee Management System</h1>

<p align="center">
    A Custom Employee Management Module Built with Odoo 19 Community Edition
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Odoo-19-purple?style=for-the-badge" alt="Odoo 19">
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge" alt="Python">
    <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge" alt="PostgreSQL">
    <img src="https://img.shields.io/badge/License-LGPL--3-green?style=for-the-badge" alt="License">
</p>

---

## 📖 Overview

**Employee Management System** is a comprehensive custom Odoo 19 module designed to streamline employee administration within any organization.

The module brings together employee information, department & designation management, attendance tracking, document management, and company asset management into a single, well-integrated ERP solution.

---

## 📸 Screenshots

### 👥 Employee Management
Employee Kanban View with profile cards.

<p align="center">
    <img src="screenshots/employee.png" width="900" alt="Employee Kanban View">
</p>

### 🏢 Department Management
Department list and form view.

<p align="center">
    <img src="screenshots/Department.png" width="900" alt="Department Management">
</p>

### 🕒 Attendance Management
Check-in / Check-out with attendance records.

<p align="center">
    <img src="screenshots/attendence.png" width="900" alt="Attendance Management">
</p>

### 📄 Employee Documents
Document management with attachments and expiry tracking.

<p align="center">
    <img src="screenshots/info.png" width="900" alt="Employee Documents">
</p>

---

## 🏗 Module Architecture

```bash
employee_management/
├── data/
│   ├── department_data.xml
│   └── employee_sequence.xml
├── models/
│   ├── employee.py
│   ├── department.py
│   ├── designation.py
│   ├── attendance.py
│   ├── employee_document.py
│   └── employee_asset.py
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
├── screenshots/
│   ├── employee.png
│   ├── Department.png
│   ├── attendence.png
│   └── info.png
├── views/
│   ├── employee_views.xml
│   ├── employee_kanban_views.xml
│   ├── department_views.xml
│   ├── designation_views.xml
│   ├── attendance_views.xml
│   ├── employee_document_views.xml
│   ├── employee_asset_views.xml
│   └── menu_views.xml
├── __manifest__.py
├── __init__.py
└── README.md

## 🚀 Key Features

### 👤 Employee Management
- Employee Profile with Photo
- Auto-generated Employee Code (Sequence)
- Personal Information (Email, Phone, Date of Birth, Joining Date)
- Department & Designation
- Notes and Active Status

### 🏢 Department Management
- Create and manage departments
- Department Code & Manager assignment
- Active/Inactive status

### 💼 Designation Management
- Manage job positions/designations

### 🕒 Attendance Management
- Check-In & Check-Out
- Automatic worked hours calculation
- Attendance history and records

### 📄 Employee Document Management
- Upload and manage documents
- Document type, expiry date, and status
- Attachment support with notes

### 💻 Employee Asset Management
- Assign company assets to employees
- Track asset details and status

### 🔘 Smart Buttons
- **Documents** and **Assets** smart buttons on employee form
- Shows related record count with one-click navigation

### 🔄 Employee Workflow
**Draft → Confirmed → Active → On Leave → Resigned**

### 🔐 Security
- Role-based access control
- Security Groups, Access Rights & Record Rules
