import json
import logging
from qExceptions import *

class AzAuth:
	def __init__(self):
		# read permissions
		f = open('appData/permissions.json')
		self.permissions = json.load(f)

		f = open('appData/userMapping.json')
		self.user_mapping = json.load(f)
		pass

	def check_permissions(self, ip, module, operation, instance=None):
		logging.debug(f"check permissions for {module}")
		username = self.get_username(ip)

		modulePermissions = self.permissions[module]
		userPermissions = modulePermissions[username]

		# legitimate for all operations
		if userPermissions[operation + "ALL"] is True:
			return

		if instance in userPermissions[operation + "SINGLE"]:
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
