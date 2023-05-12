import json
import logging

class AzAuth:
	def __init__(self):
		# read permissions
		f = open('appData/permissions.json')
		self.permissions = json.load(f)

		f = open('appData/userMapping.json')
		self.user_mapping = json.load(f)
		pass

	def check_permissions(self, ip, module, operation, instance):
		logging.debug("check permissions for...")
		print(module)
		return False

	def get_username(self, ip):
		logging.debug(f"check username for ip {ip}")
		print(self.user_mapping);
		if ip in self.user_mapping:
			username = self.user_mapping[ip]
			logging.debug(f"return username for ip {ip}: {username}")
			return username

		logging.debug(f"no username for ip {ip}")
		return ""
