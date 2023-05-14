
create appData folder with:
	appData/userMapping.json
		# TODO format
	appData/permissions.json
		# TODO format

initially:
	* create virtual environment and install flask via pip
		python3 -m venv venv
		source venv/bin/activate
		pip install flask

	* install azure-cli (will be called via subprocess)
	* login (az login)

* run application
	change to directory
	source venv/bin/activate
	export FLASK_APP=qServer.py
	flask run --host [IP]
