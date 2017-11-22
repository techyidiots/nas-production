# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

def get_context(context):
    context.main_section = "Coolest"
    context.doc.main_section = "wowx"