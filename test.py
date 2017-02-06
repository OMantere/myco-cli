import requests
from bs4 import BeautifulSoup

s = requests.Session()

def saml_url():
    global s
    jsessionid = s.cookies['JSESSIONID']
    return 'https://idp.aalto.fi/idp/profile/SAML2/Redirect/SSO;jsessionid=' + jsessionid + '?execution=e1s1'


def get(url):
    print('getted ' + url)
    global s
    return s.get(url)


def post(url, data={}, headers={}):
    print('posted ' + url)
    global s
    return s.post(url, data=data, headers=headers)


def login():
    user = 'mantero1'
    passwd = 'aamudata42!'
    data = {'j_username': user, 'j_password': passwd, '_eventId_proceed': ''}
    sso_request = get('https://mycourses.aalto.fi/auth/shibboleth/index.php')
    saml_url = sso_request.history[-1].headers['Location']
    return post(saml_url, data, {'Referer': saml_url, 'Origin': 'https://idp.aalto.fi', 'Host': 'idp.aalto.fi'})


# allright cool lets login
login()

# yay login works

