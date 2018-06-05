# register.py
# Register a new user in the CTF game, give them a cookie and redirect back
# to the code endpoint with whichever code brought them here
import re
import uuid
import db
import globals

# Check arguments for the register function
def checkArguments(argDict):
	# email, name and handle are required parameters, code is optional
	for _ in ("email", "name", "handle"):
		if _ not in argDict:
			return (False, "Incorrect arguments")

	# Ensure the email doesn't start with @, contains one @ before
	# the dot, contains one dot and doesn't have an @ after the dot
	if not re.match("[^@]+@[^@]+\.[^@]+", argDict["email"]):
		return (False, "Bad email")

	# Handles are alphanumeric with underscore and hyphens
	if not re.match("^[a-zA-Z0-9_\-]*$", argDict["handle"]):
		return (False, "Bad handle")

	# Names are alphanumeric with space, underscores, hyphens and quotes
	if not re.match("^[a-zA-Z0-9_\-\ \']*$", argDict["handle"]):
		return (False, "Bad name")
	
	# Codes are alphanumeric with underscore and hyphens
	if "code" in argDict and not re.match("^[a-zA-Z0-9_\-]*$", argDict["code"]):
		return (False, "Bad code")

	# We good
	return (True, "No error")

# Register a user and redirect them back to the code page 
def register(request=None, response=None, **kwargs):
	# Check our arguments
	res = checkArguments(kwargs)
	if res[0] == False:
		return {"error":res[1]}

	# Insert new user into db
	newUserId = db.addNewUser(kwargs["name"],kwargs["email"],kwargs["handle"])

	# Check if we were able to add the user
	if res is None:
		return {"error":"Unable to add user"}
		
	# Give the new user a session
	newSessionId= str(uuid.uuid4())
	res = db.addUserSession(newUserId,newSessionId)
	if res is None:
		return {"error":"Could not add new user session"}

	# Give the new user a session cookie
	# TODO: Remove secure=False for production 
	response.set_cookie(globals.COOKIENAME, newSessionId, secure=False)

	# Redirect them back to the code page, if they came here with one
	if "code" in kwargs: 
		reloc = "/code?code=" + kwargs["code"]
	else:
		reloc = "/"
	
	return {"success":"You're registered!", "url":reloc}
