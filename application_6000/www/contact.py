# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

def get_context(context):
	doc = frappe.get_doc("Contact Us Settings", "Contact Us Settings")

	if doc.query_options:
		query_options = [opt.strip() for opt in doc.query_options.replace(",", "\n").split("\n") if opt]
	else:
		query_options = ["Sales", "Support", "General"]

	out = {
		"query_options": query_options
	}
	out.update(doc.as_dict())

	return out

max_communications_per_hour = 1000

@frappe.whitelist(allow_guest=True)
def send_message(subject="Website Query", message="", sender="", telephone="", name=""):
	if not message:
		frappe.response["message"] = _('Please write something')
		return

	if not sender:
		frappe.response["message"] = _('Email Address Required')
		return

	if not name:
		frappe.response["message"] = _('Name is Required')
		return

	if not telephone:
		frappe.response["message"] = _('Telephone Required')
		return

	# guest method, cap max writes per hour
	if frappe.db.sql("""select count(*) from `tabCommunication`
		where `sent_or_received`="Received"
		and TIMEDIFF(%s, modified) < '01:00:00'""", now())[0][0] > max_communications_per_hour:
		frappe.response["message"] = "Sorry: we believe we have received an unreasonably high number of requests of this kind. Please try later"
		return

	email_message = """ 
	 Name : %(name)s <br />
	 Email : %(email)s <br />
	 Telephone : %(telephone)s <br />
	 Subject : %(subject)s <br />
	 Message : %(message)s <br />
	 """ %{
		"name": name,
		"email": sender,
		"telephone": telephone,
		"subject": subject,
		"message": message
	}

	# send email
	forward_to_email = frappe.db.get_value("Contact Us Settings", None, "forward_to_email")
	if forward_to_email:
		frappe.sendmail(recipients=forward_to_email, sender=sender, content=email_message, subject=subject)


	# add to to-do ?
	frappe.get_doc(dict(
		doctype = 'Communication',
		sender=sender,
		subject= _('New Message from Website Contact Page'),
		sent_or_received='Received',
		content=email_message,
		status='Open',
	)).insert(ignore_permissions=True)

	return "okay"
