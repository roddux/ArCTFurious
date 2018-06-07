# scoreboard.py
# Grab the scores from the DB and return them as a sorted list
import db

# TODO: Figure out how much locking (reading/writing db on different requests) 
#       is gonna to fuck things up 
def scoreboard():
	"""Return a list of users with their scores in descending order"""
	# Grab the scores from the DB, unsorted
	# TODO: DB exception handling
	scores = db.getScoreboard()

	# Parse the scores into the object form we want: a list of dicts
	# [ {'handle':'fred','score':10}, {'handle':'steve','score':20} ]
	pscores = [{"handle":SCORE["handle"], "score":SCORE["score"]} for SCORE in scores]

	# Sort the list of dicts
	# [ {'handle':'steve','score':20}, {'handle':'fred','score':10} ]
	spscores = sorted(pscores, key=lambda k: k["score"], reverse=True) 

	# Return our sorted list of dicts
	return spscores 
