from bs4 import BeautifulSoup
import const


def get_course_list(session):
	bs = BeautifulSoup(session.landing_page_response.content, 'html.parser')
	course_list_a = bs.find('a', title=const.my_own_courses)
	courses = []
	for li in course_list_a.parent.find('ul').children:
		courses.append(li.find('a').text.encode('UTF-8'))
	return courses

