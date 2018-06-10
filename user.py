import pyperclip
import string
import random 
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

	def save_account(self):
		"""
		save_user method saves user objects into user_list
		"""

		User.user_list.append(self)
		
# class Credential:
# 	credential_list = []
# 	user_credential_list = []

# 	@classmethod
# 	def check_user(cls,first_name,password):
# 		'''
# 		Method that checks if the name and password entered match entries in the users_list
# 		'''
# 		current_user = ''
# 		for user in User.users_list:
# 			if (user.first_name == first_name and user.password == password):
# 				current_user = user.first_name
# 		return current_user


# 	def __init__(self,user_name,email, acc, password):
# 		self.user_name = user_name
# 		self.email = email
# 		self.password = password

# 	def save_credential(self):
# 		Credential.credential_list.append(self)#function that saves the credential list

# 	def generate_password():
# 		generate_password=  "".join(choice(characters) for x in range(randint(8, 16)))
# 		return generate_password

# 	def delete_credential(self):
# 		Credential.credential_list.append(self)#function that delete the credential list



# 	@classmethod
# 	def find_by_user_name(cls,user_name):

# 		for credential in cls.credential_list:
# 			if credential.user_name == user_name:
# 				return credential

# 	@classmethod
# 	def credential_exists(cls,user_name):
# 		"""
# 		method that checks if a username exists
# 		"""
# 		for credential in cls.credential_list:
# 			if credential.user_name == user_name:
# 				return True

# 		return False


# 	@classmethod
# 	def display_credential(cls):
# 		"""
# 		method that returns the credential list
# 		"""
# 		return cls.credential_list

# 	@classmethod
# 	def copy_email(cls,user_name):
# 		credential_found = Credential.find_by_user_name(user_name)
# 		return pyperclip.copy(credential_found.email)