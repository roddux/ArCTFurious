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
	"OPEN_THE_POD_BAY_DOORS_HAL": (1, "/prize1"),
	"ELVEN_WORD_FOR_FRIEND": (2, "/prize2"),
	"NCC_ARE_TRASH": (3, "/prize3"),
	"DR_STEEL_WILL_TAKE_OVER_THE_WORLD": (100, "/prize4"),
	"THE_LAST_JEDI_IS_A_TERRIBLE_MOVIE": (95, "/prize5"),
}

# Maybe we can make this something fun
COOKIENAME="NEVER-GONNA-GIVE-YOU-UP"

# Sanitise all inputs to UTF-8
def sanitise(argDict):
	print("Sanitising arguments ...")
	for _ in argDict.items():
		KEY=_[0]
		VAL=argDict[KEY]
		print("Key: '{}', Value: ".format(KEY), end="")
		print(VAL)
		print("Value type: {}".format(type(VAL)))
		DEC=VAL.decode("UTF-8")
		print("Value type decoded: {}".format(type(DEC)))
		print("Value decoded: {}".format(DEC))
		argDict[KEY] = DEC
