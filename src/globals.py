# globals.py
# A space for all global variables (sue me)

# Check if a supplied CTF code is valid
def checkCode(code):
	import re
	# Codes are alphanumeric with underscores and hyphens
	if not re.match("^[a-zA-Z0-9_\-]*$", code):
		return False
	return True

# Global database filename for SQLite
DBFILE = "ctf.db"

# These codes are Very Important(tm) and must not change
VALID_CODES = {
	"OPEN_THE_POD_BAY_DOORS_HAL": {"points":1, "url":"/prize1"},
	"ELVEN_WORD_FOR_FRIEND": {"points":2, "url":"/prize2"},
	"NCC_ARE_TRASH": {"points":3, "url":"/prize3"},
	"DR_STEEL_WILL_TAKE_OVER_THE_WORLD": {"points":100, "url":"/prize4"},
	"THE_LAST_JEDI_IS_A_TERRIBLE_MOVIE": {"points":95, "url":"/prize5"},
}

# Make this something fun
COOKIENAME="NEVER-GONNA-GIVE-YOU-UP"

# Sanitise all inputs to UTF-8
def sanitise(argDict):
	for ARG in argDict.items():
		KEY=ARG[0]
		VAL=argDict[KEY]
		DEC=VAL.decode("UTF-8")
		argDict[KEY] = DEC
