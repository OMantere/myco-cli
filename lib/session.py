from http import HTTP
from saml import SAMLLogin, IncorrectLoginException


class Session:
	def __init__(self, user, password):
		self.http = HTTP()
		self.saml = SAMLLogin(self.http)
		try:
			self.saml.login(user, password)
		except IncorrectLoginException:
			print('Incorrect username or password.')
			exit()
		except:
			print('Unknown login error.')
			exit()
		self.landing_page_response = self.http.history[-1]
		print('Login successful!')
