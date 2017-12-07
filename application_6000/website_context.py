# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
import jinja2

def update_website_context(context):

    from frappe.utils.jinja import get_jenv

    if not frappe.form_dict._lang:
        frappe.local.flags.redirect_location = (frappe.local.request.path + (not frappe.local.request.path.endswith("?") and "?" or "") +
                                                (frappe.form_dict and
                                                 ("&".join("{0}={1}".format(key, value) for key, value in frappe.form_dict.items()) + "&") or "")
                                                + "_lang=ar")
        raise frappe.Redirect
    jenv = get_jenv()

    frappe.local.jenv.globals["get_context"] = get_context

    return

    if frappe.local.flags.in_context_update:
        return context

    frappe.local.flags.in_context_update = True

    from frappe.website.doctype.website_settings.website_settings import get_website_settings

    cookie_manager = frappe.request.cookies

    frappe.local.lang =  cookie_manager and cookie_manager.get("lang", "en")

    context.update(get_website_settings())

    frappe.local.flags.in_context_update = False

@jinja2.contextfunction
def get_context(c):
    return c

def callx():
    return callable