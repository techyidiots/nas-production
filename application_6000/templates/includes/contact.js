// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.ready(function() {

	$('.btn-send').off("click").on("click", function() {
		var email = $('[name="email"]').val();
		var message = $('[name="message"]').val();
		var name = $('[name="name"]').val();
		var telephone = $('[name="telephone"]').val();

		if(!email || !message || !name || !telephone){
			frappe.msgprint("{{ _("Please enter all required fields!") }}");
			return false;
		}

		if(!(email && message)) {
			frappe.msgprint("{{ _("Please enter both your email and message so that we \
				can get back to you. Thanks!") }}");
			return false;
		}

		if(!validate_email(email)) {
			frappe.msgprint("{{ _("You seem to have written your name instead of your email. \
				Please enter a valid email address so that we can get back.") }}");
			$('[name="email"]').focus();
			return false;
		}

		$("#contact-alert").toggle(false);
		frappe.send_message({
			subject: $('[name="subject"]').val(),
			sender: email,
			message: message,
			name: name,
			telephone, telephone,
			callback: function(r) {
				if(r.message==="okay") {
					frappe.msgprint("{{ _("Thank you for your message") }}");
				} else {
					frappe.msgprint("{{ _("There were errors") }}");
					console.log(r.exc);
				}
				$(':input').val('');
			}
		}, this);
		return false;
	});

});

var msgprint = function(txt) {
	if(txt) $("#contact-alert").html(txt).toggle(true);
}
