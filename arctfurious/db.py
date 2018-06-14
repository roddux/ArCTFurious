# db.py
# Abstract the databse into simple function calls for the rest of the app 
import sqlite3
import arctfurious.globals as globals

#def logAuth(*args):
#	print(args)
#	return sqlite3.SQLITE_OK

def openDB():
	"""Open the database"""
	# TODO: Exception handling
	con = sqlite3.connect(globals.DBFILE)
#	con.set_authorizer(logAuth)
	con.row_factory = sqlite3.Row
	con.isolation_level = None
	c = con.cursor()
	return (c,con)

dbc = None
def getDBC():
	"""Instantiate and/or just return the database cursor"""
	global dbc
	if dbc is None:
		dbc = openDB()
	return dbc[0]

def checkLastAttemptForUser(userid):
	"""Get the time the user last attempted a code"""
	c = getDBC()
	lasttime = c.execute("SELECT lastattempt FROM attempts WHERE userid=?", (userid,))
	res = lasttime.fetchone()
	return res["lastattempt"] if res is not None else None

def addAttemptForUser(userid):
	"""Add an entry to the attempts table with the userid and current time"""
	c = getDBC()
	c.execute("DELETE FROM attempts WHERE userid=?", (userid,))
	lasttime = c.execute("INSERT INTO attempts (userid,lastattempt) VALUES (?,strftime('%s'))", (userid,))

def getScoreboard():
	"""Return the list of usernames and their scores"""
	c = getDBC()
	scores = c.execute("SELECT handle,score FROM scores JOIN users on scores.userid=users.id ORDER BY score DESC")
	res = scores.fetchall()
	return res

def addScoreForUser(userid,score):
	"""Add to a users score"""
	c = getDBC()
	# Check if user has a score
	c.execute("SELECT score FROM scores WHERE userid=?", (userid,))
	curScore = c.fetchone()
	
	# If user already has a score
	if curScore is not None:
		newScore = curScore["score"] + score
		c.execute("UPDATE scores SET score=? WHERE userid=?", (newScore,userid))
		return True
	# All users should have a score of at least 0 -- unhandled error!
	else:
		return False

def hasUserClaimedCode(userid,code):
	"""Check if a user has claimed a given code"""
	c = getDBC()
	c.execute("SELECT code FROM claimed WHERE userid=? AND code=?", (userid,code,))
	res = c.fetchone()
	if res is None:
		return False
	return True

def setUserClaimedCode(userid,code):
	"""Set the user as having claimed a given code"""
	c = getDBC()
	c.execute("INSERT INTO claimed (userid,code) VALUES (?,?)", (userid,code,))

def addNewUser(name,email,handle):
	"""Add a new user to the database"""
	c = getDBC()
	c.execute("INSERT INTO users (name,email,handle) VALUES (?,?,?)", (name,email,handle,))
	res = c.lastrowid
	if res is None:
		return None
	c.execute("INSERT INTO scores (userid,score) VALUES (?,0)", (res,))
	return res

def addUserSession(userid,sessionid):
	"""Add a new session to the database"""
	c = getDBC()
	c.execute("INSERT INTO sessions (userid,sessionid) VALUES (?,?)", (userid,sessionid))
	res = c.lastrowid
	return res

def getUserForSession(sessionid):
	"""Gets the corresponding user id for a given sessionid"""
	c = getDBC()
	scores = c.execute("SELECT userid FROM sessions WHERE sessionid=?", (sessionid,))
	res = scores.fetchone()
	return res["userid"] if res is not None else None
