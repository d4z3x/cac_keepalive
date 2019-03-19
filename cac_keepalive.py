#!/usr/bin/env python3

import pickle, os, logging, requests, json
from requests import session, cookies
from time import sleep
from random import randint
from pprint import pprint

def save_cookies(session, filename):
	with open(filename, 'wb') as f:
		f.truncate()
		pickle.dump(session.cookies._cookies, f)


def load_cookies(session, filename):
	with open(filename, 'rb') as f:
		cookies = pickle.load(f)
	if cookies:
		jar = requests.cookies.RequestsCookieJar()
		jar._cookies = cookies
		session.cookies = jar
	else:
		return False

settings = {}

with open('settings.json') as f:
    settings = json.load(f)

#print("Logging to {}".format(settings['logfile']))

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=settings['logfile'], level=logging.INFO)

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

logging.info("Attempting to log on to {}...".format(settings['base_url']))

with session() as s:
	loaded_cookies = False
	cookie_name = '/tmp/.cloudatcost.cookiejar'

	if os.path.isfile(cookie_name):
		logging.info("Loading cookies...")
		load_cookies(s, cookie_name)
		loaded_cookies = True

	s.headers.update({'User-Agent': user_agent})

	r = s.post(settings['base_url'] + settings['post_uri'], data=settings['payload'])

	if r.status_code == 200:
		logging.info("Logged in...")

	if not loaded_cookies:
		logging.info("Saving cookies...")
		save_cookies(s, cookie_name)

	dur = randint(5, 30)
	logging.info("Sleeping for {}s...".format(dur))
	sleep(dur)

	r = s.get(settings['base_url'] + settings['logout_uri'], allow_redirects=False)
	if r.status_code == 302:
		logging.info("Logged out...")

