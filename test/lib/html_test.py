from bs4 import BeautifulSoup

from lib import html
from test.test_helpers import read_fixture, read_json_fixture, mock_session

landing_page = read_fixture('landing_page.html')
course_list = read_json_fixture('course_list')
course_page = read_fixture('course_page.html')
course_sections = read_json_fixture('course_sections')
section_page = read_fixture('section_page.html')
section_files = read_json_fixture('section_files')


def test_parse_course_list():
	assert course_list == html.parse_course_list(landing_page)


def test_parse_course_sections():
	assert course_sections == html.parse_course_sections(course_page)


def test_scrape_page_files():
	assert section_files == html.scrape_page_files(section_page, mock_session)


def test_parse_mc_list_item():
	assert html.parse_mc_list_item(BeautifulSoup('nonsense')) is None
