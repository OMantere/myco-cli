#!venv/bin/python

from lib.session import Session
from lib.credentials import get_credentials
from test.test_helpers import write_json_fixture, write_html_fixture
from lib import html


def generate_html_fixtures():
	landing_page_html = session.landing_page_response.text
	course_list = html.parse_course_list(landing_page_html)
	course_page_html = session.http.get(course_list[0]['url']).text
	course_sections = html.parse_course_sections(course_page_html)
	write_html_fixture('landing_page', landing_page_html)
	write_html_fixture('course_page', course_page_html)
	write_json_fixture('course_list', course_list)
	write_json_fixture('course_sections', course_sections)


if __name__ == '__main__':
	user, password = get_credentials(save_login=False)
	session = Session(user, password)
	generate_html_fixtures()
	print('Fixtures succesfully generated')
