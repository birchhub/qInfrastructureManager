# QInfrastructure Manager

simple wrapper for our cloud-hosted virtual machines. managing includes querying and changing status.
work in progress of course.

as we use it in our (virtual) network only, authentication via IP is sufficient, mapping to username done via json file (userMapping.json)
authorization is done via json file (permissons.json)

disclaimer: do not use for production systems!!

## implementation details
in order to avoid users to trigger actions multiple times, locking mechanism are implemented:
* status: can only be retrieved from azure once per minute
* changeStatus: can only be triggered for a single machine once per minute


## how to get it running

### setup
create appData folder with:
kind of sensitive data data
* appData/userMapping.json
	+ TODO format
* appData/permissions.json
	+ TODO format

install python environemnt:
* create virtual environment and install flask via pip
	+ python3 -m venv venv
	+ source venv/bin/activate
	+ pip install flask

* install azure-cli (will be called via subprocess)
* login (az login)

### run application
* change to directory
* source venv/bin/activate
* export FLASK_APP=qServer.py
* flask run --host [IP]
