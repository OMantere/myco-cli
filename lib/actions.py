from lib import html


def get_course_list(session):
	return html.parse_course_list(session.landing_page_response.text)


def get_course_files(session, course):
	url = course['href']
	course_sections = html.parse_course_sections(session.http.get(url))
	files = []
	for section in course_sections:
		section_files = html.scrape_page_files(section.http.get(section.url).text)
		for f in section_files:
			f['path'].insert(0, section.name)
		files.extend(section_files)
	for f in files:
		f['path'].insert(0, course.name)
	return files



