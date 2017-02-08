from test.test_helpers import read_fixture, read_json_fixture
from lib import html

landing_page_html = read_fixture('landing_page.html')
course_list = read_json_fixture('course_list')
course_page_html = read_fixture('course_page.html')
course_sections = read_json_fixture('course_sections')


def test_parse_course_list():
	assert course_list == html.parse_course_list(landing_page_html)


def test_parse_course_sections():
	assert course_sections == html.parse_course_sections(course_page_html)