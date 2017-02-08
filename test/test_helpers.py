import os
import const
import json

fixture_dir = os.path.join(const.project_root, 'test/fixtures/')


def read_fixture(filename):
	return open(os.path.join(fixture_dir, filename), 'r').read().decode('utf-8')


def read_json_fixture(name):
	return json.loads(read_fixture(name + '.json'))


def write_fixture(filename, content):
	print('Writing fixture ' + filename + '...')
	return open(os.path.join(fixture_dir, filename), 'w').write(content.encode('utf-8'))


def write_json_fixture(name, content):
	return write_fixture(name + '.json', json.dumps(content, ensure_ascii=False))


def write_html_fixture(name, content):
	return write_fixture(name + '.html', content)


def assert_items_equal(L1, L2):
	return len(L1) == len(L2) and sorted(L1) == sorted(L2)
