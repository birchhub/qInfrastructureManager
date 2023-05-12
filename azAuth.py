import json

class AzAuth:
	def __init__(self):
		# read permissions
		f = open('appData/permissions.json')
		self.permissions = json.load(f)

		f = open('appData/userMapping.json')
		self.user_mapping = json.load(f)
		pass

	def check_permissions(self, ip, module, operation, instance):
		return false

	def get_username(self, ip):
		return ""
