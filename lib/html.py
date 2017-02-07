from bs4 import BeautifulSoup
import const


def make_soup(html):
	return BeautifulSoup(html, 'html.parser')


def get_course_list(landing_page_html):
	bs = make_soup(landing_page_html)
	course_list_a = bs.find('a', title=const.my_own_courses)
	courses = []
	for li in course_list_a.parent.find('ul').children:
		course_a = li.find('a')
		courses.append({
			'name': course_a.text,
			'href': course_a['href']
		})
		print(courses[-1])
	return courses
