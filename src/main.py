# main.py
# The main router for the web app
import hug
import scoreboard
import ctf 
import register 

api = hug.API(__name__)

# Static files
hug.get("/register.html",   api=api, output=hug.output_format.file)(lambda:"html/register.html")
hug.get("/scoreboard.html", api=api, output=hug.output_format.file)(lambda:"html/scoreboard.html")
hug.get("/code.html",       api=api, output=hug.output_format.file)(lambda:"html/code.html")
hug.get("/main.js",         api=api, output=hug.output_format.file)(lambda:"html/main.js")
hug.get("/register.js",     api=api, output=hug.output_format.file)(lambda:"html/register.js")
hug.get("/styles.css",      api=api, output=hug.output_format.file)(lambda:"html/styles.css")

# Prize endpoints will be obscured
hug.get("/prize1", api=api, output=hug.output_format.file)(lambda:"html/prize1.html")
hug.get("/prize2", api=api, output=hug.output_format.file)(lambda:"html/prize2.html")
hug.get("/prize3", api=api, output=hug.output_format.file)(lambda:"html/prize3.html")
hug.get("/prize4", api=api, output=hug.output_format.file)(lambda:"html/prize4.html")
hug.get("/prize5", api=api, output=hug.output_format.file)(lambda:"html/prize5.html")

# Endpoints for the API functions
hug.get("/",           api=api, output=hug.output_format.file)(lambda:"html/scoreboard.html")
hug.get("/scoreboard", api=api)(scoreboard.scoreboard)
hug.get("/code",       api=api)(ctf.code)
hug.get("/register",   api=api)(register.register)

# Redirect all other requests to the scoreboard screen
hug.not_found(api=api, output=hug.output_format.file)(lambda:"html/scoreboard.html")
