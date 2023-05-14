import logging
import azAuth
import inspect
import time

class AzWrapper:

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
		return self.lastStatus
