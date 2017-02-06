import requests
import logging
from requests.packages.urllib3.exceptions import SubjectAltNameWarning

requests.packages.urllib3.disable_warnings(SubjectAltNameWarning)


class HTTP:
	def __init__(self, session=requests.Session()):
		self.session = session
		self.history = []

	def add_to_history(self, response):
		self.history.extend(response.history)
		self.history.append(response)

	def get(self, url):
		logging.info('GET ' + url)
		response = self.session.get(url)
		self.add_to_history(response)
		return response

	def post(self, url, body=None, headers=None):
		logging.info('POST ' + url)
		response = self.session.post(url, data=body, headers=headers)
		self.add_to_history(response)
		return response
