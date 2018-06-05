# db.py
# Abstract the databse into simple function calls for the rest of the app 
import sqlite3
import globals

# Open the database
def openDB():
	con = sqlite3.connect(globals.DBFILE)
	c = con.cursor()
	return (c,con)

# Commit changes and close the database
def closeDB(con):
	con.commit()
	con.close()

# Return the list of usernames and their scores
def getScoreboard():
	c,con = openDB()
	scores = c.execute("SELECT name,score FROM scores JOIN users on scores.userid=users.id ORDER BY score DESC")
	res = scores.fetchall()
	closeDB(con)
	return res 

# Either add to a user's score, or give them one
def addScoreForUser(userid,score):
	c,con = openDB()
	# Check if user has a score
	c.execute("SELECT score FROM scores WHERE userid=?", (userid,))
	curScore = c.fetchone()
	
	# If user already has a score 
	if curScore is not None:
		newScore = curScore[0] + score	
		c.execute("UPDATE scores SET score=? WHERE userid=?", (newScore,userid))
		closeDB(con)
		return True
	# All users should have a score of at least 0 -- unhandled error!
	else:
		return False

# Add a new user to the database
def addNewUser(name,email,handle):
	c,con = openDB()
	c.execute("INSERT INTO users (name,email,handle) VALUES (?,?,?)", (name,email,handle,))
	res = c.lastrowid
	if res is None:
		return None
	c.execute("INSERT INTO scores (userid,score) VALUES (?,0)", (res,))
	closeDB(con)
	return res

# Add a new session to the database
def addUserSession(userid,sessionid):
	c,con = openDB()
	c.execute("INSERT INTO sessions (userid,sessionid) VALUES (?,?)", (userid,sessionid))
	res = c.lastrowid
	closeDB(con)
	return res

# Gets the userid for a sessionid
def getUserForSession(sessionid):
	c,con = openDB()
	scores = c.execute("SELECT userid FROM sessions WHERE sessionid=?", (sessionid,))
	res = scores.fetchone()
	closeDB(con)
	return res
