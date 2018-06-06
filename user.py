class User:
	"""
	Class that generates new instance for the user
	"""
	user_list = [] #Empty user list


	def __init__(self,first_name,last_name,email,password):
		"""
		__init__ method that helps us define properties for our objects.
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

	def save_user(self):
		"""
		save_user method saves user objects into user_list
		"""

		User.user_list.append(self)
		
class Credential:
	credential_list = []
	user_credential_list = []

	def __init__(self,user_name,email,password):
		self.user_name = user_name
		self.email = email
		self.password = password

	def save_credential(self):
		Credential.credential_list.append(self)#function that saves the credential list

	def delete_credential(self):
		Credential.credential_list.append(self)#function that delete the credential list


	@classmethod
	def find_by_user_name(cls,user_name):

		for credential in cls.credential_list:
			if credential.user_name == user_name:
				return credential

	@classmethod
	def credential_exist(cls,user_name):
		"""
		method that checks if a username exists
		"""
		for credential in cls credential_list:
			if credential.user_name == user_name:
				return True
		return False


	@classmethod
	def display_credential(cls):
		"""
		method that returns the credential list
		"""
		return cls.credential_list