# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "application_6000"
app_title = "Application 6000"
app_publisher = "Syed Abdul Qadeer"
app_description = "Form for National Assembly of Kuwait"
app_icon = "octicon octicon-browser"
app_color = "#2091de"
app_email = "sdqadeer44@gmail.com"
app_license = "Proprietary"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/application_6000.app.min.css"
# app_include_js = "/assets/application_6000/js/application_6000.js"

# include js, css files in header of web template
web_include_css = "/assets/css/application_6000.web.min.css"
web_include_js = "/assets/js/application_6000.web.min.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "application_6000.utils.get_home_page"

# Fixtures
# -------
fixtures = [
    {
        "doctype": "Web Form",
        "filters": {
            "name": [
                "in", [
                    "6000"
                ]
            ]
        }
    },
    {
        "doctype": "Web Page",
        "filters": {
            "name": [
                "in", [
                    "home-page"
                ]
            ]
        }
    },
    {
        "doctype": "Website Theme",
        "filters": {
            "name": [
                "in", [
                    "KNA-Theme"
                ]
            ]
        }
    },
    "Website Settings",
	"About Us Settings",
	"Contact Us Settings",
    {
        "doctype": "Email Account",
        "filters": {
            "name": [
                "in", [
                    "Notifications"
                ]
            ]
        }
    },
	"Desktop Icon"

]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

website_context = {
	"favicon": 	"/assets/application_6000/images/logokw.png",
	"splash_image": "/assets/application_6000/images/logokw.png"
}

update_website_context = "application_6000.website_context.update_website_context"

brand_html = "<img src='/assets/application_6000/images/logokw.png' style='max-width: 150px;'>"


# Installation
# ------------

# before_install = "application_6000.install.before_install"
# after_install = "application_6000.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "application_6000.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"application_6000.tasks.all"
# 	],
# 	"daily": [
# 		"application_6000.tasks.daily"
# 	],
# 	"hourly": [
# 		"application_6000.tasks.hourly"
# 	],
# 	"weekly": [
# 		"application_6000.tasks.weekly"
# 	]
# 	"monthly": [
# 		"application_6000.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "application_6000.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "application_6000.event.get_events"
# }

