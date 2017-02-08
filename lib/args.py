import argparse

parser = argparse.ArgumentParser(description='MyCourses command line interface')
parser.add_argument('action', action='store', choices=['download'], help='The action to perform')
parser.add_argument('--save-login', dest='save_login', action='store_true', help='Save login information in the keyring of your operating system')
parser.add_argument('--erase-login', dest='erase_login', action='store_true', help='Erase saved login information')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Detailed output')
parser.set_defaults(save_login=False, erase_login=False, verbose=False)
args = parser.parse_args()
