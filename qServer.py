#!/usr/bin/env python3
import azWrapper
import logging
import json
from qExceptions import *

from flask import Flask, render_template, request
import flask

logging.basicConfig(filename="log_qserver.txt", level=logging.DEBUG,
	format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%d.%m.%Y %I:%M:%S')

logging.info("startup server")

myAzWrapper = azWrapper.AzWrapper()
api = Flask(__name__)

def executeOperation(lambdaFunc):
	try:
		return lambdaFunc()

	except QNotAuthenticatedException as e:
		logging.debug(e)
		return "" "401 Not authenticated"
	except QNotAuthorizedException as e:
		logging.debug(e)
		return "", "403 Not authrozied"
	except Exception as e:
		logging.critical(e)
		return "", "500 Ui, that should not happen.."


@api.route('/vmstatus', methods=['GET'])
def vmstatus():
	try:
		return executeOperation(lambda: myAzWrapper.azVmStatus(request.remote_addr))

	except QNotAuthenticatedException:
		return "Not authenticated", 401
	except QNotAuthorizedException:
		return "Not authrozied", 403
	except QGenericServerError:
		return "Ui, that shoul not happen.", 500

@api.route('/STOP', methods=['POST'])
def	stop_machine():
	rg = request.args.get('rg')
	vm = request.args.get('vm')
	logging.info(f"request to stop {rg}/{vm}")

	return executeOperation(lambda: myAzWrapper.azVmAction(request.remote_addr, 'STOP', rg, vm))

@api.route('/START', methods=['POST'])
def	start_machine():
	rg = request.args.get('rg')
	vm = request.args.get('vm')
	logging.info(f"request to start {rg}/{vm}")

	return executeOperation(lambda: myAzWrapper.azVmAction(request.remote_addr, 'START', rg, vm))

@api.route('/', methods=['GET'])
def	get_index():
	return executeOperation(lambda: flask.current_app.send_static_file('azStatus.html'))
