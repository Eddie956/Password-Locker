#!/usr/bin/env python3.6
from user import User

def create_user(first_name,last_name,email,password):
	'''
	Function to create a new user
	'''
	new_user = User(first_name,last_name,email,password)
	return new_user

def save_user(user):
	'''
	function to save a new user
	'''
	user.save_user()

def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	generate_password = Credential.generate_password()
	return generate_password

from user import Credential

def create_credential(user_name,email, acc, password):
	'''
	Function to ḷogin existing user
	'''
	new_credential = Credential(user_name,email,password)
	return new_credential

def save_credential(credential):
	'''
	function to save new credential
	'''
	credential.save_credential()

def find_credential(user_name):
	''' 
	function that finds a credential by username and returns the credential
	'''
	return Credential.find_by_user_name(user_name)

def check_existing_credential(user_name):
	'''
	function that check if a credential exists with that username and return a Boolean
	'''
	return Credential.credential_exist(user_name)
	
def display_credential(user_name):
	'''
	functions that returns all the saved credentials
	'''
	return Credential.display_credential(user_name)

def del_credential(credential):
	'''
	function to delete a credential
	'''
	credential.delete_credential()


# def copy_email():
# 	'''
# 	functions that returns all the email copied to the clipboard
# 	'''
# 	return Credential.copy_email()


# def main():
# 	print("Hello welcome to my app. What is your name?")
# 	user_name = input()

# 	print(f"Hello {user_name}. what would you like to do?")
# 	print('\n')

# 	while True:
# 		print("Use this short codes : su - sign up, lg - login to your account, ex - exit the app")

# 		short_code = input().lower()

# 		if short_code == 'su':
# 			print("New Account")
# 			print("-"*10)

# 			print("Enter your first_name ....")
# 			first_name = input()

# 			print("Enter your last name....")
# 			last_name = input()

# 			print("Enter your email....")
# 			email = input()

# 			print("Enter you password....")
# 			password = input ()
				
# 			save_account(create_user(first_name,last_name,email,password))
# 			print('\n')
# 			print(f"New User {first_name, last_name} account has been created")
# 			print('\n')

# 		elif short_code == 'lg':
# 				print("Please enter your details to login")
# 				print("\n")

# 				print("Enter your user name....")
# 				user_name = input()
# 				print('\n')

# 				print("Enter your email....")
# 				email = input()

# 				print("Enter your password....")
# 				password = input()
# 				user_exists = verify_user(user_name,password)
# 				if user_exists == user_name:
# 				# while (username != "username" and password != "password")

# 					print (" Sorry username and password incorrect please re-enter for validation ")
# 					print("Enter your user name....")
# 					user_name = input()
# 					print('\n')

# 					print("Enter your email....")
# 					email = input()

# 					print("Enter your password....")
# 					password = input()

# 				else:
# 					print ("Greetings," , {username}, "you are now logged in now with your password")
				
# 					again = input("Do you want to try again ?(y/n):")
# 					print("Use this short codes : su - sign up, dc - display your account, ex - exit the app")
# 					if again.lower() == 'n':
# 						print('Goodbye')
# 			# elif short_code == 'dc':
# 			# 	print('\n')

				
# 		elif short_code == "ex":
# 			print("Bye......")
# 			break

# 		else:
# 			print("Ireally didn't get that. Please use the short codes")




# if __name__ == '__main__':
#     main()