# -*- coding: utf-8 -*-
# Copyright (c) 2017, Syed Abdul Qadeer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.user import get_system_managers
from frappe.translate import get_user_lang
from frappe import _

class Application6000(Document):
	def before_insert(self):
		self.flags.in_insert = True

	def on_update(self):
		users = get_system_managers(True)

		if self.flags.in_insert:

			if users:
				for user in users:
					user_lang = get_user_lang(user)
					email_subject = _("A New Application : %(name)s is created", user_lang)%{
				"name": self.name,
				"status": self.status
			}
					email_content = _(""" 
					A new application is created
					""", user_lang)%{
				"name": self.name,
				"status": self.status
			}

					frappe.sendmail(recipients=user, subject=email_subject, content=email_content)

			if self.email:
				email_subject = _("We have received your Application : " + self.name)
				email_content = _("""
					Your application was received!
				""") % {
					"name": self.name,
					"status": self.status
				}

				frappe.sendmail(recipients=self.email, subject=email_subject, content=email_content)

			return


		if users:
			for user in users:
				user_lang = get_user_lang(user)
				email_subject = _(self.name + " have new updates", user_lang)
				email_content = _(""" 
				%(name)s status was changed to : %(status)s
				""", user_lang)%{
				"name": self.name,
				"status": self.status
			}

				frappe.sendmail(recipients=user, subject=email_subject, content=email_content)

		if self.email:
			email_subject = _(self.name + " have new updates")
			email_content = _("""
				%(name)s status was changed to : %(status)s
			""")%{
				"name": self.name,
				"status": self.status
			}

			frappe.sendmail(recipients=self.email, subject=email_subject, content=email_content)

		return
