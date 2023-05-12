#!/usr/bin/env python3
import azAuth
import inspect
import logging

logging.basicConfig(filename="log_qserver.txt", level=logging.DEBUG,
	format='%(levelname)s: %(asctime)s %(message)s',
    datefmt='%d.%m.%Y %I:%M:%S')

logging.info("startup server")

myAuth = azAuth.AzAuth()

def destFunc():
	myAuth.check_permissions('1.2.3.4', inspect.currentframe().f_code.co_name, 'a', 'b')

destFunc()
