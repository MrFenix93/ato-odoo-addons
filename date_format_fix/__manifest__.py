{
    "name": "Date Format Fix",
    "version": "19.0.1.0.0",
    "summary": "Force dd/MM/yyyy date format display in Odoo 19",
    "author": "Ato Solution",
    "website": "https://ato-solution.com",
    "license": "LGPL-3",

    "depends": ["web"],

    "images": [
        "static/description/banner.png",
    ],

    "assets": {
        "web.assets_backend": [
            "date_format_fix/static/src/js/date_format_patch.js",
        ],
    },

    "installable": True,
    "application": False,
    "post_init_hook": "post_init_hook",
}
