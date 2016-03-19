from misc.scraper import Scraper
from misc.zipper import Zipper
import datetime as dt
import time
import sys


url = ('http://api.prod.obanyc.com/api/siri/'
       'vehicle-monitoring.json')
params = {'key': sys.argv[1],  # input api key as an sys argv
          'version': 1,  # choose the version of the api, choose 2 here
          'VehicleMonitoringDetailLevel': ''}  # nothing here

if __name__ == '__main__':
    while True:
        ts = dt.datetime.now()
        filename = 'MTABusData_%s.txt' % (ts.strftime(
            '%y_%m_%d_%H_%M_%S'))
        Scraper(url, params, filename)  # where scraping happens
        time.sleep(30)
        ts_one = dt.datetime.now()
        if (ts_one - ts) >= dt.timedelta(s=3600):
            Zipper(filename)  # dump the data into a local file and zip it
            ts = ts_one
