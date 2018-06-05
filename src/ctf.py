# ctf.py
# The endpoint for checking a valid QR code
import db
import globals

# Helper function to get the userid from a sessionid cookie
def getUserFromCookie(request):
	# Get session id from cookie
	if globals.COOKIENAME in request.cookies:
		SIDToCheck = request.cookies[globals.COOKIENAME]
	else:
		return None 
	
	# Grab the user id for the session, if it exists 
	user = db.getUserForSession(SIDToCheck)

	# If it exists, we assume the user is valid
	return None if user is None else user[0]

# Check the user and their code then give them points
# TODO: Implement redirection / signup logic
def code(request=None, response=None, **kwargs):
	if "code" not in kwargs:
		return {"error":"No code mate"} 

	user = getUserFromCookie(request)
	
	if globals.checkCode(kwargs["code"]) is False:
		return {"error":"Not accepting illegal code", "url":"/"}

	if user is None:
		passCode=kwargs["code"]
		return {"error":"Go get registered", "url":"/register.html#code="+passCode} 

	# print("Checking {} for user with ID {}".format(kwargs["code"],user))
	if kwargs["code"] not in globals.VALID_CODES:
		return {"error":"Get outta here with your shit code fam", "url":"/"} 
	
	# If we got here, they good
	score = globals.VALID_CODES[kwargs["code"]][0]
	db.addScoreForUser(user, score)
	return {"success":"You win the special prize!", "url":globals.VALID_CODES[kwargs["code"]][1]}
