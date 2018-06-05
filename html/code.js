// Wrap everything in an IFFE
( function doCode() {

// Process the JSON result of checking code
function processResult(data) {
	let statusBanner = document.querySelector("#status");
	console.log(data);
	// If we have an error
	if("error" in data) {
		// add class 'error' or something to the status div
		statusBanner.innerHTML = "Error: "+data.error;
	}
	// If we succeeded 
	if("success" in data) {
		// add class 'success'
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
	function codeOkay(data) {
		return data.json();
	};

	function codeFail(data) {
		console.log(data);
	};

	// Cleaner new AJAX API that replaces XMLHttpRequest
	let codeResp = fetch(
		"/code?code="+getCodeFromHash(),
		{credentials: "same-origin"},
	)
		.then(codeOkay, codeFail)
		.catch(codeFail)
	;
	
	let data = codeResp 
		.then(processResult, codeFail)
		.catch(codeFail)
	;
}

document.addEventListener("DOMContentLoaded", checkCode);
} )();
