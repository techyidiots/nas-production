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
})