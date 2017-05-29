from bs4 import BeautifulSoup
import config
import datetime
import logging
import pickle
import redis
import requests
import time

logger = logging.getLogger('worker')
fmt_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(fmt_str)
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

r = redis.StrictRedis(host='redis')


def get_mta_data():
    return requests.get(config.MTA_STATUS_PAGE).text


def parse_onclick(text):
    return text.split(',')[1].replace('"', '').strip(")")


def parse_status_page(data):
    stations = {}
    stations['data'] = {
        "123": config.DEFAULT_STATUS,
        "456": config.DEFAULT_STATUS,
        "7": config.DEFAULT_STATUS,
        "ACE": config.DEFAULT_STATUS,
        "BDFM": config.DEFAULT_STATUS,
        "G": config.DEFAULT_STATUS,
        "JZ": config.DEFAULT_STATUS,
        "L": config.DEFAULT_STATUS,
        "NQR": config.DEFAULT_STATUS,
        "S": config.DEFAULT_STATUS,
        "SIR": config.DEFAULT_STATUS,
    }
    stations['last_updated'] = datetime.datetime.utcnow()
    soup = BeautifulSoup(data, 'html.parser')
    for el in soup.find_all('td', {'onclick': True}):
        stations['data'][parse_onclick(el.attrs['onclick'])] = el.text
    stations['data']['SIR'] = soup.find_all('td')[-1].text
    r.set("stations", pickle.dumps(stations))


def do_mta_status():
    logger.info("Querying mta status page: {}".format(datetime.datetime.now()))
    parse_status_page(get_mta_data())


logger.info("WORKER HAS STARTED")
while True:
    do_mta_status()
    time.sleep(config.CACHE_AGE)
