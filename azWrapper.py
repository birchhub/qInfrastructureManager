import logging
import azAuth
#import inspect
import time
import subprocess
import json
from azAuth import *
from qExceptions import *

class VmAction(Enum):
	START = "start"
	STOP = "deallocate"

class AzWrapper:
	mockMode = True

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
		
	def azVmChange(self, ip, method, resGroup, machine):
		logging.debug(f'{ip}: triggering action {method} for {resGroup}/{machine} ')

		# throws if not authorized
		self.myAuth.check_permissions(ip, 'STATUS', VmOperations.WRITE, machine)

		azCmd = self.azParameter.copy()
		azCmd.append("vm")
		azCmd.append(method.value)
		azCmd.append("--resource-group")
		azCmd.append(resGroup)
		azCmd.append("--name")
		azCmd.append(machine)

		logging.debug(azCmd)
		raise QGenericServerError


	def azVmStatus(self, ip, machine = None):
		# machine == None ==> report all
		logging.debug('requesting status')

		# throws if not authorized
		self.myAuth.check_permissions(ip, 'STATUS', VmOperations.READ, machine)

		# cache: only refresh in >60sec intervals
		interval = time.time() - self.lastStatus["time"]
		if (interval > 60):
			logging.info('refreshing status')
			self.lastStatus["time"] = time.time()

		# actual work here
		statusCmd = self.azParameter.copy()
		statusCmd.append("vm")
		statusCmd.append("list")
		statusCmd.append("-d")

		try:
			rawData = None
			if not self.mockMode:
				rawData = json.loads(subprocess.check_output(statusCmd))
			else:
				f = open('appData/mockData.json')
				rawData = json.load(f)

			vmList = []
			for vm in rawData["status"]:
				if machine is not None and vm["name"] != machine:
					continue

				curVm = {}
				curVm["name"] = vm["name"]
				curVm["status"] = vm["powerState"]
				curVm["extIp"] = vm["publicIps"]
				curVm["resourceGroup"] = vm["resourceGroup"]
				vmList.append(curVm)

			self.lastStatus["status"] = vmList

		except subprocess.CalledProcessError as err:
			# non-zero return value
			logging.error(f"az process failed, {err}")
			raise QGenericServerError

		return self.lastStatus
