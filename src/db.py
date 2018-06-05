# db.py
# Abstract the databse into simple function calls for the rest of the app 
import sqlite3

# Global database filename for SQLite
DBFILE = "ctf.db"

# Open the database
def openDB():
	con = sqlite3.connect(DBFILE)
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
	val = (userid,score,)
	# If user has no score
	c.execute("INSERT INTO scores (userid,score) VALUES (?,?)", (userid,score))
	# If user has a score
	c.execute("SELECT score FROM scores WHERE userid=?", (userid,))
	curScore = c.fetchOne()
	newScore = curScore + score
	c.execute("UPDATE scores SET score=? WHERE userid=?", (newScore,userid))
	closeDB(con)
	return True 

# Gets the userid for a sessionid
def getUserForSession(sessionid):
	c,con = openDB()
	scores = c.execute("SELECT userid FROM sessions WHERE sessionid=?", (sessionid,))
	res = scores.fetchone()
	closeDB(con)
	return res 
