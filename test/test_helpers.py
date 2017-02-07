import os
import const

fixture_dir = os.path.join(const.project_root, 'test/fixtures/')


def read_fixture(filename):
	return open(os.path.join(fixture_dir, filename), 'r').read().decode('utf-8')


def write_fixture(filename, content):
	return open(os.path.join(fixture_dir, filename), 'w').write(content.encode('utf-8'))
