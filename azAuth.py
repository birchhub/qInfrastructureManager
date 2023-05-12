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
		return ""
