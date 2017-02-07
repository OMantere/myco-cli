from test.test_helpers import read_fixture
from lib.html import *
import json

landing_page_html = read_fixture('landing_page.html')
course_list = json.loads(read_fixture('course_list.json'))


def test_parse_course_list():
	assert course_list == parse_course_list(landing_page_html)
