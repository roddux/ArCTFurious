# Installation
- Setup a python3 virtualenv and activate it
	$ virtualenv -p `which python3` ./ARCTF_env
	$ source ARCTF_env/activate
- Use pip3 to install the 'hug' package
	$ pip install hug

# Setup
- Use sqlite3 to setup the database
	$ sqlite3 ctf.db <setup.sql

# Running
- For devleopment, just run:
	$ hug -f main.py
In production this will switch to uwsgi and nginx.
