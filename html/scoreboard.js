// Wrap everything in an IFFE
( function doMain() {

// Take the JSON and display it in a table
function displayScores(scoreJSON) {
	// Add a score to the scoreboard table by cloning the template row
	function displayScore(score) {
		let tpl = document.querySelector('#scoretpl');
    		let clone = document.importNode(tpl.content, true);
    		td = clone.querySelectorAll("td");
    		td[0].textContent = score.handle;
    		td[1].textContent = score.score;
		let tb = document.querySelector("#scoretable>tbody");
    		tb.appendChild(clone);
	}

	// Loop over the score list we receive and display each score
	scoreJSON.forEach(displayScore);
}

// Fucking asynchronous Promise() 'thenable' .callback NOSNENSE 
function getScores() {
	function scoresOkay(data) {
		return data.json();
	};

	function scoresFail(data) {
		console.log(data);
	};

	// Cleaner new AJAX API that replaces XMLHttpRequest
	scores = fetch("/scoreboard")
		.then(scoresOkay, scoresFail)
		.catch(scoresFail)
	;
	
	data = scores
		.then(displayScores, scoresFail)
		.catch(scoresFail)
	;
}

document.addEventListener("DOMContentLoaded", getScores);
} )();
