import os
from lib.core import *
import const

fixture_dir = os.path.join(const.project_root, 'test/fixtures/')


def get_fixture(filename):
	return open(os.path.join(fixture_dir, filename), 'r').read()

landing_page_content = get_fixture('landing_page_content.html')
course_list = get_fixture('course_list.txt').split('\n')[:-1]


def test_get_course_list():
	mock_session = type('Session', (), {
		'landing_page_response': type('Response', (), {
			'content': landing_page_content
		})
	})
	assert course_list == get_course_list(mock_session)
