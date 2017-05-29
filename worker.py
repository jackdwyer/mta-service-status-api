import config
import datetime
import logging
from lxml import html
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
    return html.fromstring(requests.get(config.MTA_STATUS_PAGE).content)


def parse_status_page(data):
    stations = {}
    stations['last_updated'] = datetime.datetime.utcnow()
    stations['data'] = {}
    for el in data.xpath('//tr'):
        status = el.xpath('./td[@align="center"]/text()')[0]
        # ['routeIcons_22/1.gif', 'routeIcons_22/2.gif', 'routeIcons_22/3.gif']
        lines = [l.split("/")[-1].replace(".gif", "").upper()
                 for l in el.xpath('.//img/@src')]
        if len(lines) == 0:
            # must be sir
            lines = ["SIR"]
        for l in lines:
            stations['data'][l] = status

    r.set("stations", pickle.dumps(stations))


def do_mta_status():
    logger.info("Querying mta status page: {}".format(datetime.datetime.now()))
    parse_status_page(get_mta_data())


logger.info("WORKER HAS STARTED")
while True:
    do_mta_status()
    time.sleep(config.CACHE_AGE)
