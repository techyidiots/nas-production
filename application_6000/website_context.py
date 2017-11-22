# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe

def update_website_context(context):
    if frappe.local.flags.in_context_update:
        return context

    frappe.local.flags.in_context_update = True

    from frappe.website.doctype.website_settings.website_settings import get_website_settings

    query_strings = frappe.local.request.args

    frappe.local.lang =  query_strings and query_strings.get("lang", "en")

    context.update(get_website_settings())

    frappe.local.flags.in_context_update = False
