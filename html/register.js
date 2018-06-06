// Wrap everything in an IFFE
( function doRegister() {

// Process the JSON result of checking code
function processResult(data) {
	// If we have an error
	if("error" in data) {
		alert("Error: "+data.error);
	}
	// If we succeeded 
	if("success" in data) {
		alert("Success: "+data.success);
	}
	// We've been given a redirect, lets do so after 2.5s
	if("url" in data) {
		window.setTimeout(
			function redirect() {
				window.location = data.url;
			}
		, 2500);
	}
}

// Form submit function
function submitForm() {
	let passedCode = window.location.hash.split("=")[1];
	let form = document.querySelector("#regForm");
	let fd = new FormData(form);
	if(typeof passedCode != "undefined") {
		fd.append("code", passedCode);
	}
	
	fetch(
		"/register",
		{
			method: "POST",
			body: fd,
			credentials: "same-origin"
		},
	).then(resp=>resp.json()).then(processResult);

	return false;
}

function onLoad() {
	// Check if they are already registered and redirect them, for funsies
	let form = document.querySelector("#regForm");
	form.onsubmit = submitForm;
}

document.addEventListener("DOMContentLoaded", onLoad);
} )();
