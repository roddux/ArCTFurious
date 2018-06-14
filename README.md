# Installation
Setup a python3 virtualenv and activate it

    $ virtualenv --prompt='[ArCTFurious] ' -p $(which python3) ./ARCTF_env
    $ source ARCTF_env/activate

Use pip3 to install the requirements 

    $ pip --no-cache-dir install -r requirements.txt

# Setup
Use sqlite3 to setup the database

    $ sqlite3 ctf.db <setup.sql

# Running
For devleopment, either run:

    $ hug -f src/main.py

Or,

    $ uwsgi --http 0.0.0.0:8000 --wsgi-file arctfurious/main.py --callable __hug_wsgi__
