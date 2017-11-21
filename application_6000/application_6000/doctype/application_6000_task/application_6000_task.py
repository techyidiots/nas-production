# -*- coding: utf-8 -*-
# Copyright (c) 2017, Syed Abdul Qadeer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.translate import get_user_lang
from frappe import _

class Application6000Task(Document):
	def before_insert(self):
		self.flags.in_insert = True

	def on_update(self):
		if self.flags.in_insert:
			if self.user:
				user_lang = get_user_lang(self.user)
				email_subject = _(self.name + " was assigned to you")
				email_content = _("""
				    		%(name)s status was changed to : %(status)s
				    	""", user_lang) % {
					"name": self.name,
					"status": self.status
				}

				frappe.sendmail(recipients=self.user, subject=email_subject, content=email_content)
			return

		if not self.user == self.modified_by:
			user_lang = get_user_lang(self.user)
			email_subject = _(self.name + " have new updates")
			email_content = _("""
	    		%(name)s status was changed to : %(status)s
	    	""", user_lang) % {
				"name": self.name,
				"status": self.status
			}

			frappe.sendmail(recipients=self.user, subject=email_subject, content=email_content)
	pass
