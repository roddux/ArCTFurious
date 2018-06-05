# register.py
# Register a new user in the CTF game, give them a cookie and redirect back
# to the code endpoint with whichever code brought them here
import re

# Check arguments for the register function
def checkArguments(argDict):
	# We want Email, Name, Handle
	for _ in ("email", "name", "handle"):
		if _ not in argDict:
			return (False, "Incorrect arguments")

	# Ensure the email doesn't start with @, contains one @ before
	# the dot, contains one dot and doesn't have an @ after the dot
	if not re.match("[^@]+@[^@]+\.[^@]+", kwargs["email"]):
		return (False, "Bad email")

	# Handles are alphanumeric with underscore and hyphens
	if not re.match("^[a-zA-Z0-9_\-]*$", kwargs["handle"]):
		return (False, "Bad handle")

	# Names are alphanumeric with space, underscores, hyphens and quotes
	if not re.match("^[a-zA-Z0-9_\-\ \']*$", kwargs["handle"]):
		return (False, "Bad name")

# TODO: Finish implementing this method
def register(request=None, response=None, **kwargs):
	# Check our arguments
	res = checkArguments(kwargs)
	if res[0] == False:
		return res[1]

	# insert into db
	# db.addNewUser(etc)

	# redirect user back to the code page, with their cookie
	# response.status = "307 OVER HERE MATE"
	# response.append_header("Location","/register")
	# response.set_cookie(COOKIENAME,"SESHIDINIT",secure=False)
	return False
