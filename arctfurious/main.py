# main.py
# The main router for the web app
import hug
import arctfurious.scoreboard as scoreboard
import arctfurious.ctf as ctf
import arctfurious.register as register
import arctfurious.globals as globals

api = hug.API(__name__)

# Static files
hug.get("/register.html",   api=api, output=hug.output_format.file)(lambda:"arctfurious/html/register.html")
hug.get("/register.js",     api=api, output=hug.output_format.file)(lambda:"arctfurious/html/register.js")
hug.get("/scoreboard.html", api=api, output=hug.output_format.file)(lambda:"arctfurious/html/scoreboard.html")
hug.get("/scoreboard.js",   api=api, output=hug.output_format.file)(lambda:"arctfurious/html/scoreboard.js")
hug.get("/code.html",       api=api, output=hug.output_format.file)(lambda:"arctfurious/html/code.html")
hug.get("/code.js",         api=api, output=hug.output_format.file)(lambda:"arctfurious/html/code.js")
hug.get("/styles.css",      api=api, output=hug.output_format.file)(lambda:"arctfurious/html/styles.css")
hug.get("/promeo.woff2",    api=api, output=hug.output_format.file)(lambda:"arctfurious/html/promeo.woff2")

# Prize endpoints will be obscured
hug.get("/prize1", api=api, output=hug.output_format.file)(lambda:"arctfurious/html/prize1.html")
hug.get("/prize2", api=api, output=hug.output_format.file)(lambda:"arctfurious/html/prize2.html")
hug.get("/prize3", api=api, output=hug.output_format.file)(lambda:"arctfurious/html/prize3.html")
hug.get("/prize4", api=api, output=hug.output_format.file)(lambda:"arctfurious/html/prize4.html")
hug.get("/prize5", api=api, output=hug.output_format.file)(lambda:"arctfurious/html/prize5.html")

# Endpoints for the API functions
hug.get("/",            api=api, output=hug.output_format.file)(lambda:"arctfurious/html/scoreboard.html")
hug.get("/scoreboard",  api=api)(scoreboard.scoreboard)
hug.post("/code",       api=api)(ctf.code)
hug.post("/register",   api=api)(register.register)

# Temporary debug endpoint
def deleteCookies(response=None):
	response.unset_cookie(globals.COOKIENAME)
	return True	
hug.get("/dc", api=api)(deleteCookies)

# Redirect all other requests to the scoreboard screen
# TODO: This hack just uses the scoreboard page for 404 errors, figure out how to do this properly
hug.not_found(api=api, output=hug.output_format.file)(lambda:"arctfurious/html/scoreboard.html")
