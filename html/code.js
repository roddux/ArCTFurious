// Wrap everything in an IFFE
( function doCode() {

// Process the JSON result of checking code
function processResult(data) {
	let statusBanner = document.querySelector("#status");
	// If we have an error
	if("error" in data) {
		statusBanner.innerHTML = "Error: "+data.error;
	}
	// If we succeeded 
	if("success" in data) {
		statusBanner.innerHTML = "Success: "+data.success;
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

// Grab the code from URL hash parameter
function getCodeFromHash() {
	let codeInput = document.querySelector("#code");
	let passedCode = window.location.hash.split("=")[1];
	return passedCode;	
}

// Fucking asynchronous Promise() 'thenable' .callback NOSNENSE 
function checkCode() {
	let fd = new FormData();
	let passedCode = getCodeFromHash();
	if(typeof passedCode == "undefined") {
		let statusBanner = document.querySelector("#status");
		statusBanner.innerHTML = "Error: You don't have a code!";
		window.setTimeout(
			function redirect() {
				window.location = "/";
			}
		, 2500);
		return false;
	}
	else {
		fd.append("code", getCodeFromHash());
	}
	fetch(
		"/code",
		{
			method: "POST",
			body: fd,
			credentials: "same-origin"
		},
	).then(resp=>resp.json()).then(processResult);
}

document.addEventListener("DOMContentLoaded", checkCode);
} )();
