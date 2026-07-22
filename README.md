# 👨‍💼 Employee Management System

A complete custom **Employee Management System** built with **Odoo 19 Community Edition**. This project demonstrates end-to-end Odoo module development, including employee lifecycle management, business logic, custom workflows, security, smart buttons, and multiple UI views.

> This project was developed as part of my Odoo learning journey to gain hands-on experience with custom module development and ERP business workflows.

---

## 📌 Table of Contents

- Overview
- Features
- Module Workflow
- Technologies Used
- Module Structure
- Installation
- Learning Outcomes
- Future Improvements
- Author
- License

---

# 📖 Overview

The Employee Management System is a custom Odoo module that centralizes employee-related operations in a single application.

It enables organizations to:

- Manage employee information
- Organize departments and designations
- Record attendance
- Manage employee documents
- Track company assets
- Control employee workflow
- Apply role-based security

The project follows Odoo's MVC architecture and uses Python for business logic, XML for views, PostgreSQL for data storage, and Odoo ORM for database operations.

---

# ✨ Features

## 👤 Employee Management

- Employee Profile
- Employee Photo
- Auto Generated Employee Code
- Email & Phone
- Date of Birth
- Joining Date
- Department
- Designation
- Notes
- Active/Inactive Status

### Auto Employee Sequence

Every employee receives a unique ID automatically.

Example:

```
EMP00001
EMP00002
EMP00003
```

---

## 🏢 Department Management

Manage company departments.

Examples:

- HR
- IT
- ERP
- Accounts
- Marketing

---

## 💼 Designation Management

Manage employee job positions.

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

- Attendance Date
- Check In
- Check Out
- Employee Reference

---

## 📄 Employee Documents

Store employee-related documents.

Examples:

- CV
- National ID
- Passport
- Offer Letter
- Appointment Letter

Features:

- Document Type
- File Upload
- Description

---

## 💻 Employee Assets

Manage company assets assigned to employees.

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

---

# 🔘 Smart Buttons

Employee Form includes Smart Buttons for:

- Documents
- Assets

These buttons display record counts and provide quick navigation.

---

# 🔄 Employee Workflow

Employee lifecycle is managed using custom workflow states.

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

---

# 🔍 Views

The module includes multiple Odoo views.

- Form View
- List View
- Kanban View
- Search View

Kanban cards display:

- Employee Photo
- Employee Name
- Employee Code
- Department
- Designation
- Status

---

# 🔐 Security

Implemented role-based access control.

### Employee Management User

- Read Records
- Create Records
- Update Records

### Employee Management Manager

- Full CRUD Access
- Manage All Records
- Administrative Permissions

Security includes:

- Groups
- Access Rights
- Record Rules

---

# ⚙ Business Logic

Implemented using Python and Odoo ORM.

Includes:

- Auto Employee Sequence
- Computed Fields
- Related Fields
- Smart Button Count
- Workflow Actions
- Custom Business Methods
- Validations

---

# 🗄 Database Models

The project contains the following models:

- employee.management.employee
- employee.management.department
- employee.management.designation
- employee.management.attendance
- employee.management.document
- employee.management.asset

---

# 📂 Project Structure

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

# 🛠 Technologies Used

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

# 📚 Learning Outcomes

During this project I learned and practiced:

- Odoo Module Development
- Odoo ORM
- Python Business Logic
- XML View Development
- Form/List/Kanban/Search Views
- Models & Relationships
- Actions & Menus
- Smart Buttons
- Computed Fields
- Related Fields
- Workflow Management
- Security Groups
- Access Rights
- Record Rules
- Sequences
- PostgreSQL Integration
- Module Installation & Upgrade
- Debugging and Error Resolution

---

# 🚀 Future Improvements

Planned features:

- Leave Management
- Payroll
- Recruitment
- Employee Contracts
- Performance Evaluation
- Dashboard & Analytics
- Calendar View
- Graph & Pivot Views
- PDF Reports
- Excel Export
- Email Notifications
- QR/Barcode Support
- Multi-company Support

---

# 👨‍💻 Author

## Sharat Acharja

**Backend Developer | Odoo Developer | Python Developer**

🌐 **Portfolio**  
https://sharatpsd.netlify.app/

💻 **GitHub**  
https://github.com/Sharatpsd

💼 **LinkedIn**  
https://www.linkedin.com/in/sharat-acharjya/

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

---

# 📄 License

This project is licensed under the **LGPL-3 License**.
