import requests
import yaml
import pytest


@pytest.fixture(scope='session')
def conf():
    with open('conf.yml') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='session')
def cookies(conf):
    url = conf['url']
    payload = {'admin[email]': conf['email'], 'admin[password]': conf['password']}
    r = requests.post(url, data=payload)
    return r.cookies
