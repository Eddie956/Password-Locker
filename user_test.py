import unittest #module
import pyperclip
from user import User, Credential #importing the user class

class TestUser(unittest.TestCase):
	"""
	subclass TestUser
	test class that define s the test case for the user class.
	"""
	def setUp(self):
		"""
		set up a method to run before each test cases.
		"""
		self.new_account = User("Eddie", "Mutugi", "mutugieddie3@gmail.com", "mango")#create user object

	def  test_init(self):
		"""
		test_init testcase to test if the object is initialized properly
		"""
		self.assertEqual(self.new_account.first_name,"Eddie")
		self.assertEqual(self.new_account.last_name,"Mutugi")
		self.assertEqual(self.new_account.email,"mutugieddie3@gmail.com")
		self.assertEqual(self.new_account.password,"mango")

	def test_save_account(self):
		"""
		test_save_user test case to test if the user object is saved into the user list
		"""
		self.new_account.save_account()#saving the new user
		self.assertEqual(len(User.user_list),1)

class TestCredential(unittest.TestCase):
	"""
	test class that defines the test case for credential class
	"""
	def setUp(self):
		"""
		a setup method to run before each testcase
		"""
		self.new_credential = Credential("Arijm", "mutugieddie3@gmail.com", "instagram", "mango")

	def test__init__(self):
		"""
		testcase to test if the object is initialized
		"""
		self.assertEqual(self.new_credential.user_name,"Arijm")
		self.assertEqual(self.new_credential.email,"mutugieddie3@gmail.com")
		self.assertEqual(self.new_credential.acc,"instagram")
		self.assertEqual(self.new_credential.password,"mango")

	def test_save_credential(self):
		"""
		test case to test if the credential are saved into credential list
		"""
		# self.new_credential.save_credential()#saving the new credential
		self.assertEqual(len(Credential.credential_list),0)

	def tearDown(self):
		"""
		it does clean up after each and every test has run
		"""
		Credential.credential_list = []
		User.credential_list = []

	def test_save_multiple_credential(self):
		"""
		test to check if we can save multiple credentials
		"""
		# self.new_credential.save_credential()
		test_credential = Credential("Arijm", "mutugieddie3@gmail.com" , "instagram", "mango")#new credential
		self.assertEqual(len(Credential.credential_list),0)

	def test_delete_credential(self):
		"""
		test if one can remove a user from credential list
		"""
		self.new_credential.delete_credential()
		test_credential = Credential("Arijm", "mutugieddie3@gmail.com", "instagram", "mango")#new credential
		test_credential.delete_credential()
		self.new_credential.delete_credential()
		self.assertEqual(len(Credential.credential_list),3)


	def test_find_credential_by_username(self):
		"""
		test to check if we can find a user by his name
		"""
		self.new_credential.save_credential()
		test_credential = Credential("Arijm", "mutugieddie3@gmail.com", "instagram", "mango")#new credential
		test_credential.save_credential()
		found_credential = Credential.find_by_user_name("Arijm")
		self.assertEqual(found_credential.user_name,test_credential.user_name)

	def test_credential_exist(self):
		"""
		testing if we can return a Boolean if the credential is not found
		"""
		self.new_credential.save_credential()
		test_credential = Credential("Arijm", "mutugieddie3@gmail.com" , "instagram", "mango")#new credential
		test_credential.save_credential()
		credential_exists = Credential.credential_exists("Arijm")
		self.assertTrue(credential_exists)

	def test_display_all_credential(self):
		"""
		a method that returns a list of all credentials saved
		"""
		self.assertEqual(Credential.display_credential(),Credential.credential_list)

	def test_copy_email(self):
		"""
		test to confirm we are copying an email address from a found credential
		"""
		self.new_credential.save_credential()
		Credential.copy_email("Arijm")
		self.assertEqual(self.new_credential.email,pyperclip.paste())


if __name__ == '__main__':
	unittest.main()