#!/usr/bin/env python3
import azAuth
import inspect

myAuth = azAuth.AzAuth()

def destFunc():
	myAuth.check_permissions('1.2.3.4', inspect.currentframe().f_code.co_name, 'a', 'b')

destFunc()
