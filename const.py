import re
import os

project_root = os.path.dirname(os.path.abspath(__file__))
keyring_username = '___myco-cli_user'
keyring_password = '___myco-cli_passworpasswordd'
my_own_courses = re.compile(r'My own courses|Omat kurssini|Mina kurser')
