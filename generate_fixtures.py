#!venv/bin/python

from lib.session import Session
from lib.credentials import get_credentials
from test.test_helpers import write_json_fixture, write_html_fixture
from lib import html


def generate_html_fixtures():
	landing_page = session.landing_page_response.text
	course_list = html.parse_course_list(landing_page)
	write_html_fixture('landing_page', landing_page)
	write_json_fixture('course_list', course_list)

	course_page = session.http.get(course_list[0]['url']).text
	course_sections = html.parse_course_sections(course_page)
	write_html_fixture('course_page', course_page)
	write_json_fixture('course_sections', course_sections)

	section_page = session.http.get(course_sections[1]['url']).text
	section_files = html.scrape_page_files(section_page)
	write_html_fixture('section_page', section_page)
	write_json_fixture('section_files', section_files)


if __name__ == '__main__':
	user, password = get_credentials()
	session = Session(user, password)
	generate_html_fixtures()
	print('Fixtures successfully generated')
