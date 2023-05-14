import logging
import azAuth
import inspect
import time
import subprocess
import json
from qExceptions import *

class AzWrapper:
	azParameter = []
	azParameter.append("/usr/bin/env")
	azParameter.append("az")

	def __init__(self):
		self.lastStatus = {}
		self.lastStatus["time"] = 0
		self.lastStatus["status"] = "unknown"

		self.lastAction = {}
		self.lastAction["time"] = 0

		self.myAuth = azAuth.AzAuth()
		

	def azVmStatus(self, ip, machine = None):
		logging.debug('requesting status')

		# throws if not authorized
		self.myAuth.check_permissions(ip, inspect.currentframe().f_code.co_name, 'READ', machine)

		# cache: only refresh in >30sec intervals
		interval = time.time() - self.lastStatus["time"]

		if (interval > 30):
			logging.info('refreshing status')
			self.lastStatus["time"] = time.time()

		# actual work here
		statusCmd = self.azParameter.copy()
		statusCmd.append("vm")
		statusCmd.append("list")
		statusCmd.append("-d")

		try:
			self.lastStatus["status"] = json.loads(subprocess.check_output(statusCmd))
		except subprocess.CalledProcessError as err:
			# non-zero return value
			logging.error(f"az process failed, {err}")
			raise QGenericServerError

		return self.lastStatus
