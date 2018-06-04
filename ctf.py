# ctf.py
# The endpoint for checking a valid QR code
import db

# These codes are Very Important(tm) and must not change
# TODO: Change this structure (and the logic handling it at the end of code())
#       to allow for different victory pages per code       
VALID_CODES = {
	"OPEN_THE_POD_BAY_DOORS_HAL": 1,
	"ELVEN_WORD_FOR_FRIEND": 2,
	"NCC_ARE_TRASH": 3,
	"DR_STEEL_WILL_TAKE_OVER_THE_WORLD": 100,
	"THE_LAST_JEDI_IS_A_TERRIBLE_MOVIE": 95,
}

# Maybe we can make this something fun
COOKIENAME="NEVER-GONNA-GIVE-YOU-UP"

# Helper function to get the userid from a sessionid cookie
def getUserFromCookie(request):
	# Get session id from cookie
	if COOKIENAME in request.cookies:
		SIDToCheck = request.cookies[COOKIENAME]
	else:
		return None 
	
	# Grab the user id for the session, if it exists 
	user = db.getUserForSession(SIDToCheck)

	# If it exists, we assume the user is valid
	return user 

# Check the user and their code then give them points
# TODO: Implement redirection / signup logic
def code(request=None, response=None, **kwargs):
	if "code" not in kwargs:
		return "No code mate" 

	user = getUserFromCookie(request)

	if user is None:
		# response.status = "307 OVER HERE MATE"
		# response.append_header("Location","/register")
		response.set_cookie(COOKIENAME,"SESHIDINIT",secure=False)
		return "Uh you ain't logged in bro but it's ok here have a cookie"
	
	if code not in VALID_CODES:
		return "Get outta here with your shit code fam" 
	
	# If we got here, they good
	score = VALID_CODES[code]
	db.addScoreForUser(user, score)
	return "You win the special prize!"
