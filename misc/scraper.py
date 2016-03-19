import requests
import json
import time


def Scraper(url, params, filename):
    fw = open(filename, 'a')
    try:
        response = requests.get(url, params, timeout=(0.001, 10))
    except requests.exceptions.ConnectionError as e:  # connection error
        print e
        fw.write('/n')
        time.sleep(30)
    except requests.exceptions.ConnectTimeout as e:  # ConnectTimeout error
        print e
        fw.write('/n')
        time.sleep(30)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:  # http error
        print e
        fw.write('/n')
        time.sleep(30)
    except requests.exceptions.RequestException as e:  # RequestException error
        print e
        time.sleep(300)
    finally:
        data = response.json()
        json.dump(data, fw)
        json.dump('\n', fw)
        fw.close()
        print 'data dumped'
