#!venv/bin/python

import logging

from lib import actions
from lib import file
from lib.args import args
from lib.credentials import get_credentials, erase_credentials, store_credentials
from lib.session import Session


def init_logging():
	if args.verbose:
		logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
	else:
		logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARN)


def retrieve_credentials():
	if args.erase_login and not erase_credentials():
		print('Failed to erase login.')
	return get_credentials()


def save_credentials(user, password):
	if args.save_login:
		if store_credentials(user, password):
			print('Login saved in keyring.')
		else:
			print('Failed to save login!')


if __name__ == '__main__':
	print('\nWelcome to the MyCourses command line client!')
	init_logging()
	user, password = retrieve_credentials()
	session = Session(user, password)
	save_credentials(user, password)

	# download yo
	if args.action == 'download':
		course_list = actions.get_course_list(session)
		for course in course_list:
			print('\nDownloading files for course ' + course['name'])
			files = actions.get_course_files(session, course)
			file.download_files(files, session)
