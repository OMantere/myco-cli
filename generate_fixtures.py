#!venv/bin/python

import json
from lib.session import Session
from lib.credentials import get_credentials
from test.test_helpers import write_fixture
from lib.html import get_course_list


def generate_html_fixtures():
	landing_page_html = session.landing_page_response.text
	write_fixture('landing_page.html', landing_page_html)
	write_fixture('course_list.json', json.dumps(get_course_list(landing_page_html), ensure_ascii=False))


if __name__ == '__main__':
	user, password = get_credentials(save_login=False)
	session = Session(user, password)
	generate_html_fixtures()
