# 👨‍💼 Employee Management System

A complete custom **Employee Management System** developed using **Odoo 19 Community Edition**.

This project was built to understand the complete Odoo development workflow, including custom models, XML views, ORM, business logic, security, workflows, smart buttons, computed fields, and module architecture.

---

# 📌 Overview

The Employee Management module helps organizations manage employees and their daily information from a single place.

It allows administrators to:

- Manage Employees
- Manage Departments
- Manage Designations
- Record Attendance
- Manage Employee Documents
- Track Company Assets
- Handle Employee Lifecycle
- Control User Permissions

The project follows Odoo's modular architecture and uses Python for business logic, XML for UI, PostgreSQL for data storage, and Odoo ORM for database operations.

---

# ✨ Key Features

## 👤 Employee Management

Complete employee profile management including:

- Employee Name
- Employee Code (Auto Generated)
- Employee Photo
- Date of Birth
- Age Calculation
- Email
- Phone Number
- Department
- Designation
- Joining Date
- Probation End Date
- Experience
- Years of Service
- Active Status
- Internal Notes

---

## 🔢 Employee Sequence

Every employee receives a unique Employee ID automatically.

Example:

```
EMP00001
EMP00002
EMP00003
```

Implemented using:

- ir.sequence
- create() override

---

## 🏢 Department Management

Create and manage departments.

Example:

- HR
- Accounts
- ERP
- IT
- Marketing

Department can be assigned to multiple employees.

---

## 💼 Designation Management

Manage employee job titles.

Examples:

- Software Engineer
- ERP Executive
- HR Officer
- Accounts Executive
- Manager

---

## 🕒 Attendance Management

Track employee attendance.

Features:

- Check In
- Check Out
- Working Hours
- Attendance Date

Attendance records are linked with employees.

---

## 📄 Employee Documents

Manage important employee files.

Examples:

- CV
- National ID
- Passport
- Offer Letter
- Appointment Letter

Features:

- Document Type
- Upload File
- Description

Integrated using Smart Button.

---

## 💻 Employee Assets

Track company assets assigned to employees.

Examples:

- Laptop
- Desktop
- Mobile
- Keyboard
- Mouse

Features:

- Asset Name
- Asset Code
- Assigned Employee
- Issue Date

Integrated using Smart Button.

---

# 🔘 Smart Buttons

Employee form contains Smart Buttons for:

- Documents
- Assets

Displays:

- Total Documents
- Total Assets

Uses:

- Computed Fields
- Action Windows

---

# 🔄 Employee Workflow

Employee lifecycle is managed using custom states.

```
Draft
   ↓
Confirmed
   ↓
Active
   ↓
On Leave
   ↓
Resigned
```

Workflow is implemented using:

- Selection Field
- Header Statusbar
- Python Methods
- Object Buttons

---

# 🔍 Search View

Custom search functionality includes:

- Employee Name
- Employee Code
- Department
- Designation
- Status

Provides faster record filtering.

---

# 📋 List View

Displays employee records in table format.

Supports:

- Sorting
- Searching
- Filtering
- Multi-record Operations

---

# 🧩 Form View

Complete employee details with organized sections.

Includes:

- Personal Information
- Employee Information
- Notes
- Image Upload
- Workflow
- Smart Buttons

---

# 🗂 Kanban View

Modern employee cards displaying:

- Employee Photo
- Employee Name
- Employee Code
- Department
- Designation
- Status Badge

---

# 🔐 Security

Implemented role-based security.

## Employee Management User

Can:

- View Employees
- Create Records
- Update Records

---

## Employee Management Manager

Has full control.

Can:

- Create
- Update
- Delete
- Manage All Records

---

# 🛠 Business Logic

Implemented using Python.

Includes:

- Employee Code Generation
- Age Calculation
- Experience Calculation
- Years of Service
- Probation End Date
- Smart Button Count
- Workflow Actions

---

# 🗄 Database Models

This project contains the following models:

- employee.management.employee
- employee.management.department
- employee.management.designation
- employee.management.attendance
- employee.management.document
- employee.management.asset

---

# 📂 Module Structure

```
employee_management/
│
├── data/
│   ├── department_data.xml
│   └── employee_sequence.xml
│
├── models/
│   ├── employee.py
│   ├── department.py
│   ├── designation.py
│   ├── attendance.py
│   ├── employee_document.py
│   └── employee_asset.py
│
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
│
├── views/
│   ├── employee_views.xml
│   ├── employee_kanban_views.xml
│   ├── department_views.xml
│   ├── designation_views.xml
│   ├── attendance_views.xml
│   ├── employee_document_views.xml
│   ├── employee_asset_views.xml
│   └── menu_views.xml
│
├── __init__.py
├── __manifest__.py
└── README.md
```

---

# ⚙ Technologies Used

- Odoo 19 Community
- Python
- PostgreSQL
- XML
- Odoo ORM
- Git
- GitHub
- Ubuntu (WSL)
- VS Code

---

# 📚 What I Learned

During this project I explored:

- Odoo Module Development
- Module Structure
- Manifest File
- Odoo ORM
- Models
- Fields
- Relationships
- Computed Fields
- XML Views
- Form View
- List View
- Kanban View
- Search View
- Menus
- Actions
- Smart Buttons
- State Workflow
- Python Business Logic
- Security Groups
- Record Rules
- Access Rights
- Sequences
- PostgreSQL
- Odoo Shell
- Debugging
- Module Upgrade Process

---

# 🚀 Future Improvements

Planned features:

- Leave Management
- Payroll
- Recruitment
- Performance Evaluation
- Dashboard
- Charts & Reports
- Employee Contracts
- Email Notifications
- QR Attendance
- Barcode Support
- Multi-company Support

---

# 👨‍💻 Author

**Sharat Acharja**

Backend Developer | Odoo Developer | Python Developer

GitHub:
https://github.com/Sharatpsd

LinkedIn:
https://www.linkedin.com/in/sharat-acharja/

---

# 📄 License

LGPL-3
