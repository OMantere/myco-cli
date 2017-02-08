import json
import os
import urllib

from const import files_root

inventory_path = os.path.join(files_root, 'inventory.json')


def dircheck(file_object):
	path = os.path.join(files_root, '/'.join(file_object['path']))
	try:
		os.makedirs(path)
	except:
		pass
	return path


def load_inventory():
	if os.path.exists(inventory_path):
		return json.loads(open(inventory_path, 'r').read())
	else:
		return {}


def download_files(files, session, refresh=False):
	inventory = load_inventory()
	for f in files:
		inventory = download(f, session, inventory, refresh)


def download(file_object, session, inventory, refresh):
	if file_object['url'] not in inventory or refresh:
		response = session.http.get(file_object['url'])
		filename = urllib.unquote(response.url.split('/')[-1].replace('?forcedownload=1', ''))
		print('Downloading ' + filename)
		path = os.path.join(dircheck(file_object), filename)
		with open(path, 'wb') as f:
			for chunk in response.iter_content(chunk_size=1024):
				if chunk:
					f.write(chunk)
			f.close()
		inventory[file_object['url']] = ''
		with open(inventory_path, 'w') as f:
			f.write(json.dumps(inventory))
			f.close()
	return inventory
