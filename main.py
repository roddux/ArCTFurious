# main.py
# The main router for the web app
import scoreboard
import ctf 
import register 
import hug

api = hug.API(__name__)
hug.get('/scoreboard', api=api)(scoreboard.scoreboard)
hug.get('/code', api=api)(ctf.code)
hug.get('/register', api=api)(register.register)
