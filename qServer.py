#!/usr/bin/env python3
import azWrapper
import logging
import json
from qExceptions import *

from flask import Flask, render_template, request

logging.basicConfig(filename="log_qserver.txt", level=logging.DEBUG,
	format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%d.%m.%Y %I:%M:%S')

logging.info("startup server")

myAzWrapper = azWrapper.AzWrapper()
api = Flask(__name__)

@api.route('/vmstatus', methods=['GET'])
def vmstatus():
	try:
		return myAzWrapper.azVmStatus(request.remote_addr)

	except QNotAuthenticatedException:
		return "Not authenticated", 401
	except QNotAuthorizedException:
		return "Not authrozied", 403

	return json.dumps("{}")
