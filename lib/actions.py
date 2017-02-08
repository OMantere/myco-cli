from lib import html


def get_course_list(session):
	return html.parse_course_list(session.landing_page_response.text)


def get_course_files(session, course):
	url = course['href']
	course_page_html = session.http.get(url).text
	course_sections = html.parse_course_sections(course_page_html)
