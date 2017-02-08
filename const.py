import re
import os

project_root = os.path.dirname(os.path.abspath(__file__))
files_root = os.path.join(project_root, 'files')
keyring_username = '___myco-cli_user'
keyring_password = '___myco-cli_password'
my_own_courses = re.compile(r'My own courses|Omat kurssini|Mina kurser')
