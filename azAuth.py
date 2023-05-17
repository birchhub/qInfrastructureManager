import json
import logging
from enum import Enum
from qExceptions import *

class VmOperations(Enum):
	READ = "READ"
	WRITE = "WRITE"

class AzAuth:
	def __init__(self):
		# read permissions
		f = open('appData/permissions.json')
		self.permissions = json.load(f)

		f = open('appData/userMapping.json')
		self.user_mapping = json.load(f)

	def check_permissions(self, ip, module, operation, instance=None):
		logging.debug(f"check permissions for {module}")
		username = self.get_username(ip)

		if module not in self.permissions:
			raise QNotAuthorizedException

		modulePermissions = self.permissions[module]
			
		if username not in modulePermissions:
			raise QNotAuthorizedException
		userPermissions = modulePermissions[username]

		# legitimate for all operations
		if operation.value + "ALL" in userPermissions and userPermissions[operation.value + "ALL"] is True:
			return

		# legitimate for this machine
		if instance in userPermissions[operation.value + "SINGLE"]:
			return

		raise QNotAuthorizedException

	def get_username(self, ip):
		logging.debug(f"check username for ip {ip}")
		if ip in self.user_mapping:
			username = self.user_mapping[ip]
			logging.debug(f"return username for ip {ip}: {username}")
			return username

		logging.debug(f"no username for ip {ip}")
		raise QNotAuthenticatedException
