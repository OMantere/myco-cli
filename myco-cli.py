#!venv/bin/python

import logging
from lib.credentials import get_credentials, erase_credentials
from lib.args import args
from lib.session import Session


def init_logging():
	if args.verbose:
		logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
	else:
		logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARN)


def handle_credentials():
	if args.erase_login and not erase_credentials():
		print('\nFailed to erase login.')
	return get_credentials(args.save_login)


if __name__ == '__main__':
	print('\nWelcome to the MyCourses command line client!')
	init_logging()
	user, password = handle_credentials()
	session = Session(user, password)
