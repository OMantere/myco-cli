import responses
import requests
from test.test_helpers import assert_items_equal
from lib.http import HTTP


@responses.activate
def test_get_basic():
	responses.add(responses.GET, 'http://test.com', body='whatever', status=200)
	http = HTTP()
	r = http.get('http://test.com')

	assert r.text == 'whatever'
	assert r.status_code == 200
	assert http.history == [r]


@responses.activate
def test_get_redirect():
	responses.add(responses.GET, 'http://another.com', body='yay', status=200)
	responses.add(responses.GET, 'http://test.com/redirect', body='redirecting', status=302,
				  adding_headers={
					  'Location': 'http://another.com/'
				  })
	http = HTTP()
	r = http.get('http://test.com/redirect')

	assert len(r.history) == 1
	assert r.history[0].status_code == 302
	assert r.history[0].text == 'redirecting'
	assert r.status_code == 200
	assert r.text == 'yay'
	assert http.history == [http.history[0], r]
	assert assert_items_equal(http.cache.keys(), ['http://test.com/redirect', 'http://another.com/'])
