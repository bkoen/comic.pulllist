/*
Matt Sheppard (GIS-ATT)
Last updated 02/25/13

A collection of functions for quickly building AJAX-style
web interfaces based on a front-end form and back-end CGI
script.

The only function that will be called manually is xmlhttpPost, 
the remaining functions are called from within this as
required.
*/

/* xmlhttpPost(<URL for post request>,<name of form>,<name of results div>);

	e.g.
	xmlhttpPost('/cgi-bin/script.cgi','myForm','resultsDiv');
	
	form name and name of results div MUST match the values in the front-end
*/
function xmlhttpPost(strURL,formName,tarDiv) {
	var xmlHttpReq = false;
	var self = this;
	// Mozilla/Safari
	if (window.XMLHttpRequest) {
		self.xmlHttpReq = new XMLHttpRequest();
	}
	// IE
	else if (window.ActiveXObject) {
		self.xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
	}
	self.xmlHttpReq.open('POST', strURL, true);
	self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	self.xmlHttpReq.onreadystatechange = function() {
		if (self.xmlHttpReq.readyState == 4) {
			updatepage(tarDiv,self.xmlHttpReq.responseText);
		}
	}
	self.xmlHttpReq.send(getquerystring(formName));
}

/* used by xmlhttpPost to retrieve a list of
	form elements and values, then build a query
	string out of all of these.
*/
function getquerystring(specifiedForm) {
	var form     = document.forms[specifiedForm];
	var word = form.word.value;
	qstr = 'w=' + escape(word);  // NOTE: no '?' before querystring
	return qstr;
}

/* updates the target div with the given string;
	used by xmlhttpPost to update the "results"
	area with the response from the post.
*/
function updatepage(div,str){
	document.getElementById(div).innerHTML = str;
}