from bs4 import BeautifulSoup
import const


def bs_decorator(func):
	"""Decorator to turn the html passed to the parser function to a Beautifulsoup object"""
	def wrapper(html):
		return func(BeautifulSoup(html, 'html.parser'))
	return wrapper


def parse_mc_link_list(ul):
	def parse_list_item(li):
		link = li.find('a')
		return {'name': link.text, 'url': link['href']}
	return map(parse_list_item, ul.find_all('li'))


@bs_decorator
def parse_course_list(soup):
	course_list = soup.find('a', title=const.my_own_courses).parent.find('ul')
	return parse_mc_link_list(course_list)


@bs_decorator
def parse_course_sections(soup):
	section_menu = soup.find('ul', {'id': 'menu'})
	return parse_mc_link_list(section_menu)


