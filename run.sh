#!/usr/bin/env bash
set -e

DBFILE="ctf.db"

echo "Setting up database"
if [ -f $DBFILE ]; then
	echo -n "Erase existing database? [y/n] "
	read ERASE
	if [[ 'y' == $ERASE || 'Y' == $ERASE ]]; then
		rm $DBFILE
	else
		echo "Will not touch existing database. Quitting!"
		exit
	fi
fi

sqlite3 $DBFILE < arctfurious/schema.sql

echo -n "Add dummy data? [y/n] "
read DUMMY
if [[ 'y' == $DUMMY || 'Y' == $DUMMY ]]; then
	sqlite3 $DBFILE < arctfurious/dummy_data.sql
fi

echo "Starting uwsgi server"
uwsgi --http 0.0.0.0:8000 --wsgi-file arctfurious/main.py --callable __hug_wsgi__
