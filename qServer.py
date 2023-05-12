#!/usr/bin/env python3
import azAuth
import inspect
import logging
import json

from flask import Flask, render_template, request

logging.basicConfig(filename="log_qserver.txt", level=logging.DEBUG,
	format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%d.%m.%Y %I:%M:%S')

logging.info("startup server")

myAuth = azAuth.AzAuth()
api = Flask(__name__)

@api.route('/vmstatus', methods=['GET'])
def vmstatus():
	return json.dumps("{}")
