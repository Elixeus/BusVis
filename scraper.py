import sys
import json
import requests
import datetime as dt
import time

'''
This script is for scraping data from the MTA.
It scrapes the data every five minutes and zip it every hour.

sys.argv[1]: the api key of the user.
'''

'''
pull down the data every 30 seconds,
append the data to the existing file,
print an empty line,
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
			# check if the url works
			response.raise_for_status()
			# retrieve the json file
			try:
				data_raw = response.json()
			# name the file with the access time
			filename = 'BusData_%s.json' %(sts_init.strftime(
						'%y_%m_%d_%H_%M_%S'))
			# deal
			fw = open(filename, 'a')
			json.dump(data_raw, fw)
			json.dump('\n', fw)
			fw.close()
			print 'data dumped'
			time.sleep(30)
			sts = dt.datetime.now()
			# update the sts if the time delta is larger than 1 hour
			if (sts - sts_init) >= dt.timedelta(seconds = 3600):
				sts_init = sts
	except KeyboardInterrupt:
		print 'interrupted!'