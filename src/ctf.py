# ctf.py
# The endpoint for checking a valid QR code
import time
import db
import globals

def getUserFromCookie(request):
	"""Helper function to get the userid from a sessionid cookie"""
	# Check we have the cookie, first 
	if globals.COOKIENAME not in request.cookies:
		return None

	# Get session id from cookie
	SIDToCheck = request.cookies[globals.COOKIENAME]

	# db.getUserForSession returns either None or the user id
	user = db.getUserForSession(SIDToCheck)
	return user

def code(request=None, response=None, **kwargs):
	"""Check the user and their code then give them points"""
	# Ensure we have a code parameter to check
	if "code" not in kwargs:
		return {"error":"No code mate", "url":"/"} 

	# UTF-8 strings only pls
	globals.sanitise(kwargs)

	userCode = kwargs["code"]

	# Grab the userid
	user = getUserFromCookie(request)

	# Check for a valid code (see globals.checkCode)
	if globals.checkCode(userCode) is False:
		return {"error":"Not accepting illegal code", "url":"/"}

	# Ensure we have a user
	if user is None:
		passCode=userCode
		return {"error":"Go get registered", "url":"/register.html#code="+passCode}

	# Check their last attempt
	checkTime = db.checkLastAttemptForUser(user)
	if checkTime is not None:
		# 10 attempts per min is 1 every 6 seconds
		timeNow = int(time.strftime('%s'))
		if timeNow - checkTime < 6:
			return {"error":"Slow down there, buddy", "url":"/"}

	# Add an attempt for this user
	db.addAttemptForUser(user)

	# If the code isn't valid, tell the uer 
	if userCode not in globals.VALID_CODES:
		return {"error":"Get outta here with your shit code fam", "url":"/"} 

	# Check the user hasn't claimed this code already
	if db.hasUserClaimedCode(user, userCode) == True:
		return {"error":"You've already claimed this code", "url":"/"}

	# If we reach this point, we have a valid user with a valid code
	# We credit them with the points and redirect them to the victory page for that code
	score = globals.VALID_CODES[userCode]["points"]
	# TODO: DB exception handling
	db.addScoreForUser(user, score)
	db.setUserClaimedCode(user, userCode)
	return {"success":"You win the special prize!", "url":globals.VALID_CODES[userCode]["url"]}
