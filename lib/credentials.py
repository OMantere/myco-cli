import getpass

import keyring

import const


def store_credentials(user, password):
	try:
		keyring.set_password('login', const.keyring_username, user)
		keyring.set_password('login', const.keyring_password, password)
	except:
		return False
	return True


def erase_credentials():
	if read_credentials() is None:
		return True
	try:
		keyring.delete_password('login', const.keyring_username)
		keyring.delete_password('login', const.keyring_password)
	except:
		return False
	return True


def read_credentials():
	user = keyring.get_password('login', const.keyring_username)
	password = keyring.get_password('login', const.keyring_password)
	if user is None or password is None:
		return None
	return str(user), str(password)


def ask_credentials():
	user = ""
	password = ""
	print("\nPlease login.")
	while user == "":
		user = raw_input("Username: ")
	while password == "":
		password = getpass.getpass("Password: ")
	return user, password


def get_credentials():
	credentials = read_credentials()
	if credentials is None:
		credentials = ask_credentials()
	else:
		print('Login information loaded from keyring.')
	return credentials
