# scoreboard.py
# Grab the scores from the DB and return them as a sorted list
import db

# TODO: Figure out how much locking (reading/writing db on different requests) 
#       is gonna to fuck things up 
def scoreboard():
	# Grab the scores from the DB, unparsed, unsorted
	# ('fred',10), ('steve',20)
	scores = db.getScoreboard()

	# Parse the scores into the object form we want: a list of dicts
	# [ {'name':'fred','score':10}, {'name':'steve','score':20} ]
	pscores = [{"name":SCORE[0], "score":SCORE[1]} for SCORE in scores]

	# Sort the list of dicts
	# [ {'name':'steve','score':20}, {'name':'fred','score':10} ]
	spscores = sorted(pscores, key=lambda k: k["score"], reverse=True) 
	
	# Return our sorted list of dicts
	return spscores 
