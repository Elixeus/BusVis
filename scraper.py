import sys
import json
import requests
import datetime as dt
import time

'''
This script can be used to scrape real-time bus data feed from the MTA.
It pulls the data every 30 seconds, save it to the local file,
prints an empty space. After every hour, the local file is zipped,
and a new file is created to hold the data again. This way we can avoid
having data with very large volume.

The program takes 1 system argument: sys.argv[1] -- the API key from MTA.
'''

if __name__ == '__main__':
	# record the start time stamp
	sts_init = dt.datetime.now()
	url = ('http://api.prod.obanyc.com/api/siri/'
					   'vehicle-monitoring.json')
	params = {'key':sys.argv[1], # input api key as an sys argv
			  'version':1, # choose the version of the api, choose 2 here
			  'VehicleMonitoringDetailLevel': ''} # nothing here
	try:
		while True:
			sts = dt.datetime.now()
			# use the requests module to pull down the data
			response = requests.get(url, params)
			try:
				# sanity check
				response.raise_for_status()
				# retrieve the json file
				data_raw = response.json()
			except requests.exceptions.RequestException:
				print 'an error occurred!'
				time.sleep(30)
			# name the file with the access time
			filename = 'BusData_%s.json' %(sts_init.strftime(
						'%y_%m_%d_%H_%M_%S'))
			# deal
			fw = open(filename, 'a')
			json.dump(data_raw, fw)
			json.dump(' ', fw)
			fw.close()
			print 'data dumped'
			time.sleep(30)
			sts = dt.datetime.now()
			# update the sts if the time delta is larger than 1 hour
			if (sts - sts_init) >= dt.timedelta(seconds = 3600):
				sts_init = sts
	except KeyboardInterrupt:
		print 'interrupted!'