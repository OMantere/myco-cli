import re

from bs4 import BeautifulSoup

import const


def bs_decorator(func):
	"""Decorator to turn the html passed to the parser function to a Beautifulsoup object"""

	def wrapper(html, *args):
		return func(BeautifulSoup(html, 'html.parser'), *args)

	return wrapper


def parse_mc_list_item(item):
	link = item.find('a')
	if link is None:
		return None
	return {'name': link.text, 'url': link['href']}


def parse_mc_link_list(link_list):
	return filter(None, map(parse_mc_list_item, link_list.find_all('li')))


@bs_decorator
def parse_course_list(soup):
	course_list = soup.find('a', title=const.my_own_courses).parent.find('ul')
	return parse_mc_link_list(course_list)


@bs_decorator
def parse_course_sections(soup):
	section_menu = soup.find('ul', {'id': 'menu'})
	return parse_mc_link_list(section_menu)


@bs_decorator
def scrape_page_files(soup, session):
	folders = soup.find_all("li", {"class": "activity folder modtype_folder "})
	resources = soup.find_all("li", {"class": "activity resource modtype_resource "})
	assignments = soup.find_all("li", {"class": "activity assign modtype_assign "})
	yui_files = soup.find_all("div", {"id": re.compile("^assign_files")})

	files = filter(None, map(parse_mc_list_item, resources + yui_files))
	for f in files:
		f['path'] = []

	for nested in filter(None, map(parse_mc_list_item, folders + assignments)):
		nested_files = scrape_page_files(session.http.get(nested['url']).text, session)
		for f in nested_files:
			f['path'].insert(0, nested['name'])
		files += nested_files

	return files
