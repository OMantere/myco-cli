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
		self.history.extend(response.history)
		self.history.append(response)
		for r in response.history + [response]:
			self.cache[r.url] = r

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
