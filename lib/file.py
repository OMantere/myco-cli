import os
from const import files_root


def dircheck(file):
	path = os.path.join(files_root, '/'.join(file['path']))
	try:
		os.makedirs(path)
	except:
		pass
	return path


def download(file_object, session):
	filename = dircheck(file_object)
	response = session.http.get(file_object['url'], stream=True)
	with open(filename, 'wb') as f:
		for chunk in response.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	return filename
