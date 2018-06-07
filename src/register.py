# register.py
# Register a new user in the CTF game, give them a cookie and redirect back
# to the code endpoint with whichever code brought them here
import re
import uuid
import db
import globals

def checkArguments(argDict):
	"""Check arguments for the register function"""
	# email, name and handle are required parameters, code is optional
	for _ in ("email", "name", "handle"):
		if _ not in argDict:
			return (False, "Incorrect arguments")

	# Sanitise all our arguments to UTF-8 strings
	globals.sanitise(argDict)

	# Ensure the email doesn't start with @, contains one @ before
	# the dot, contains one dot and doesn't have an @ after the dot
	if not re.match("[^@]+@[^@]+\.[^@]+", argDict["email"]):
		return (False, "Bad email")

	# Handles are alphanumeric with underscore and hyphens
	if not re.match("^[\-\w]*$", argDict["handle"]):
		return (False, "Bad handle")

	# Names are alphanumeric with space, underscores, hyphens and quotes
	if not re.match("^[\-\w' ]*$", argDict["name"]):
		return (False, "Bad name")

	# The code check is a global, because we use it elsewhere too
	if "code" in argDict and globals.checkCode(argDict["code"]) is False:
		return (False, "Bad code")
		
	# We good
	return (True, "No error")

def register(request=None, response=None, **kwargs):
	"""Register a user and redirect them depending on their supplied code, if any"""
	# Check our arguments
	res = checkArguments(kwargs)
	if res[0] == False:
		# TODO: Implement this return {} malarkey as a global function
		return {"error":res[1]}

	# Insert new user into db
	# TODO: DB exception handling
	newUserId = db.addNewUser(kwargs["name"],kwargs["email"],kwargs["handle"])

	# Check if we were able to add the user
	if res is None:
		return {"error":"Unable to add user"}
		
	# Give the new user a session
	newSessionId = str(uuid.uuid4())
	# TODO: DB exception handling
	res = db.addUserSession(newUserId,newSessionId)
	if res is None:
		return {"error":"Could not add new user session"}

	# Give the new user a session cookie
	# TODO: Remove secure=False and http_only=False for production 
	response.set_cookie(globals.COOKIENAME, newSessionId, secure=False, http_only=False)

	# Redirect them back to the code page, if they came here with one
	if "code" in kwargs: 
		reloc = "/code.html#code=" + kwargs["code"]
	else:
		reloc = "/"

	return {"success":"You're registered!", "url":reloc}
