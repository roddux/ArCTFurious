// Wrap everything in an IFFE
( function doRegister() {

// Grab the code from our URL parameter and slap it in the form 
function loadCode() {
	let codeInput = document.querySelector("#code");
	let passedCode = window.location.hash.split("=")[1];
	codeInput.value = passedCode;	
}

document.addEventListener("DOMContentLoaded", loadCode);
} )();
