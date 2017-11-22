$(document).ready(function(e){
    $("li[data-label=Language]").find("a").on("click", function(e){
        e.preventDefault();
        var language = "ar";
       if($(this).parent("li").attr("data-label") == "English"){
           language = "en"
       }

       var query_params = frappe.utils.get_query_params();
       query_params["_lang"] = language;

       var query_strings = frappe.utils.make_query_string(query_params);

       var loc = window.location;

       var new_url = loc.protocol + "//" + loc.hostname + (loc.port ? ":"+loc.port : "") +
           loc.pathname + (query_strings && query_strings.trim()!=="?" ? query_strings : "") + loc.hash;

       window.location = new_url;
    });

    $("a").each(function(){

    });
});

frappe.urllib = {

	// get argument from url
	get_arg: function(url, name) {
		name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
		var regexS = "[\\?&]"+name+"=([^&#]*)";
		var regex = new RegExp( regexS );
		var results = regex.exec( url || window.location.href );
		if( results == null )
			return "";
		else
			return decodeURIComponent(results[1]);
	},

	// returns url dictionary
	get_dict: function(url) {
		var d = {}
		var t = url || window.location.href.split('?')[1];
		if(!t) return d;

		if(t.indexOf('#')!=-1) t = t.split('#')[0];
		if(!t) return d;

		t = t.split('&');
		for(var i=0; i<t.length; i++) {
			var a = t[i].split('=');
			d[decodeURIComponent(a[0])] = decodeURIComponent(a[1]);
		}
		return d;
	},

	// returns the base url with http + domain + path (-index.cgi or # or ?)
	get_base_url: function(url) {
		// var url= (frappe.base_url || window.location.href).split('#')[0].split('?')[0].split('desk')[0];
		url = (url || window.location.origin)
		if(url.substr(url.length-1, 1)=='/') url = url.substr(0, url.length-1)
		return url
	},

	// returns absolute url
	get_full_url: function(url) {
		if(url.indexOf("http://")===0 || url.indexOf("https://")===0) {
			return url;
		}
		return url.substr(0,1)==="/" ?
			(frappe.urllib.get_base_url() + url) :
			(frappe.urllib.get_base_url() + "/" + url);
	}
}