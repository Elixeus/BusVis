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
Start working on the one hour zipper,
TODO: familiarize with CRON, which is very good at expection handling
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
			data_raw = response.json()
			# name the file with the access time
			filename = 'data_%s.json' %(sts_init.strftime('%y_%m_%d_%H_%M_%S'))
			try:
				# load the old json file
				with open(filename, 'r') as fr:
					jload = json.load(fr)
					# append the new data to the old json file
					jload.update(data_raw)
				# write the new content into the json file
				with open(filename, 'w') as fw:
					jwrite = json.dump(data_raw, fw)
					jwrite(fw)
			except IOError:
				with open(filename, 'w') as fw:
					jwrite = json.dump(data_raw, fw)
					jwrite(fw)
			# compare the time delta
			time.sleep(30)
			# update the sts if the time delta is larger than 1 hour
			if (sts - sts_init) >= dt.timedelta(seconds = 3600):
				sts_init = sts
			else:
				pass

	except KeyboardInterrupt:
		print 'interrupted!'