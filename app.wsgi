#!/usr/bin/python
#Said added this
activate_this = '/opt/flask/cs373-idb/py3venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))


import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/cs373-idb/")
sys.path.insert(0,"/opt/flask/cs373-idb/")

from app.app import app
app.secret_key = '42 secret keys here'
