from bs4 import BeautifulSoup

mycourses_saml_url = 'https://mycourses.aalto.fi/Shibboleth.sso/SAML2/POST'


class IncorrectLoginException(Exception):
	pass


class SAMLLogin:
	def __init__(self, http):
		self.http = http

	def sso_auth(self, user, password):
		body = {'j_username': user, 'j_password': password, '_eventId_proceed': ''}
		headers = {'Referer': self.sso_url, 'Origin': 'https://idp.aalto.fi', 'Host': 'idp.aalto.fi'}
		return self.http.post(self.sso_url, body, headers)

	def mycourses_post(self, sso_response):
		soup = BeautifulSoup(sso_response.text, 'html.parser')
		if 'The password you entered was incorrect.' in soup.text:
			raise IncorrectLoginException
		saml_response = soup.find('input', {'name': 'SAMLResponse'}).get('value')
		relay_state = soup.find('input', {'name': 'RelayState'}).get('value')
		body = {'RelayState': relay_state, 'SAMLResponse': saml_response}
		headers = {'Referer': self.sso_url, 'Origin': 'https://idp.aalto.fi', 'Host': 'mycourses.aalto.fi'}
		return self.http.post(mycourses_saml_url, body, headers)

	def login(self, user, password):
		sso_redirect = self.http.get('https://mycourses.aalto.fi/auth/shibboleth/index.php')
		self.sso_url = sso_redirect.history[-1].headers['Location']
		sso_response = self.sso_auth(user, password)
		mycourses_response = self.mycourses_post(sso_response)
		if not mycourses_response.status_code == 200:
			raise Exception('Unknown error')
		return
