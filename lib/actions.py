from lib import html


def get_course_list(session):
	return html.parse_course_list(session.landing_page_response.text)


def get_course_files(session, course):
	url = course['url']
	course_sections = html.parse_course_sections(session.http.get(url).text)
	files = []
	for section in course_sections:
		section_files = html.scrape_page_files(session.http.get(section['url']).text, session)
		for f in section_files:
			f['path'].insert(0, section['name'])
		files.extend(section_files)
	for f in files:
		f['path'].insert(0, course['name'])
	return files
