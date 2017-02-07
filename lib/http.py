import requests
import logging
from requests.packages.urllib3.exceptions import SubjectAltNameWarning

requests.packages.urllib3.disable_warnings(SubjectAltNameWarning)


class HTTP:
	def __init__(self, session=requests.Session()):
		self.session = session
		self.history = []
		self.cache = {}

	def add_to_history(self, response):
		if len(response.history) > 0:
			self.add_to_history(response.history[-1])
		self.history.append(response)
		self.cache[response.url] = response

	def get(self, url, refresh=False):
		logging.info('GET ' + url)
		if url not in self.cache or refresh:
			response = self.session.get(url)
			self.add_to_history(response)
			return response
		else:
			return self.cache[url]

	def post(self, url, body=None, headers=None):
		logging.info('POST ' + url)
		response = self.session.post(url, data=body, headers=headers)
		self.add_to_history(response)
		return response
