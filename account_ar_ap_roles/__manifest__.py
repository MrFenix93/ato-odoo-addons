{
    "name": "AR & AP Accounting Roles",
    "version": "19.0.1.0.0",
    "category": "Accounting",
    "summary": "Separate Accounts Receivable and Accounts Payable access for Odoo Community",

    "description": """
AR & AP Accounting Roles for Odoo 19 Community.

Provides separate accounting roles for Accounts Receivable (AR)
and Accounts Payable (AP).

Features:
- AR Accountant security group
- AP Accountant security group
- Separate Receivable and Payable menu access
- Restrict accounting entries according to AR/AP role
- Restrict Partner Ledger options according to AR/AP role

Requires the accounting_pdf_reports module from OM Accounting.
    """,

    "author": "ATO Solution",
    "website": "https://ato-solution.com",
    "license": "LGPL-3",

    "depends": [
        "account",
        "accounting_pdf_reports",
    ],

    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/account_menu_views.xml",
    ],

    "images": [
        "static/description/banner.png",
    ],

    "installable": True,
    "application": False,
    "auto_install": False,
}