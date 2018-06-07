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

from user import Credential

def create_credential(user_name,email,password):
	'''
	Function to create a new user
	'''
	new_credential = Credential(user_name,email,password)
	return new_credential

def save_credential(credential):
	'''
	function to save new credential
	'''
	credential.save_credential()

def del_credential(credential):
	'''
	function to delete a credential
	'''
	credential.delete_credential()

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
	
def display_credential():
	'''
	functions that returns all the saved credentials
	'''
	return Credential.display_credential()

def copy_email():
	'''
	functions that returns all the email copied to the clipboard
	'''
	return Credential.copy_email()

def generate_password():
	'''
	functions that generates anew password
	'''
	return Credential.generate_password()


def main():
	print("Hello welcome to my app. What is your name?")
	user_name = input()

	print(f"Hello {user_name}. what would you like to do?")
	print('\n')

	while True:
		print("Use this short codes : cc - create anew account, lg - login to your account, fc - finding account by username, ex - exit the app")

		short_code = input().lower()

		if short_code == 'cc':
			print("New Account")
			print("-"*10)

			print("Enter your first_name ....")
			first_name = input()

			print("Enter your last name....")
			last_name = input()

			print("Enter your user name....")
			user_name = input ()

			print("Enter your email....")
			email = input()

			print("Enter you password....")
			password = input ()

			print("Confirm your password....")
			password = input ()

			while password !=password:
				print("Your password did not match please try again")
				print("Enter you password....")
				password = input ()

				print("Confirm your password....")
				password = input ()

			save_user(create_user(first_name,last_name,user_name,email,password))
			print('\n')
			print(f"New User {first_name, last_name} account has been created")
			print('\n')

		elif short_code == 'lg':

			if login():
				print("Please enter your details to login")
				print("\n")

				print("Enter your user name....")
				user_name = input()
				print('\n')

				print("Enter your email....")
				email = input()

				print("Enter your password....")
				password = input()

				if user_exists == user_name:
					print(f"Welcome {user_name} you have successfully logedin password locker")
					print("\n")

				else:
					print("user name or password is not recognized")
					again = input("DO you want to try again ?(y/n):")
					if again.lower() == 'n':
						print('Goodbye')
				
		elif short_code == "ex":
			print("Bye......")
			break

		else:
			print("Ireally didn't get that. Please use the short codes")




if __name__ == '__main__':
    main()