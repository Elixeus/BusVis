import requests
import json
import time


def Scraper(filename, url, params=None):
    '''
    Scraper is a generic function that can be used to scrape data from any API.
    filename: create a file on the harddrive where the data can be stored.
    url: the url of the API.
    params: the parameters required by the API e.g. API KEY, consumer secret...
    '''
    fw = open(filename, 'a')
    '''
    there are 3 major HTTP request failures: Client, Server, and Caller.
    TODO: 1. study these failures more carefully 2. tweak the timeout range
    '''
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
