
create appData folder with:
	appData/userMapping.json
		# TODO format
	appData/permissions.json
		# TODO format

* create virtual environment and install flask via pip
	python3 -m venv venv
	source venv/bin/activate
	pip install flask

* run application
	change to directory
	source venv/bin/activate
	export FLASK_APP=qServer.py
	flask run --host [IP]
