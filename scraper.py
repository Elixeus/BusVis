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

# if __name__ == '__main__':
try:
	while True:
			url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json'
			params = {'key':sys.argv[1], # input api key as an sys argv
		  			  'version':1, # choose the version of the api, choose 2 here
		  			  'VehicleMonitoringDetailLevel': ''} # nothing here
			# use the requests module to pull down the data
			response = requests.get(url, params)
			# check if the url works
			response.raise_for_status()

			print response.content
			# retrieve the json file
			data_raw = response.json()
			# nanme the file with the access time
			filename = 'data_%s.json' %(
				dt.datetime.now().strftime('%y_%m_%d_%H_%M_%S'))
			# save the data to a json file
			with open(filename, 'w') as fh:
				json.dump(data_raw, fh)
			# rest for 3 minutes
			time.sleep(5*60)
			# notify the new start
			print 'Start again'

except KeyboardInterrupt:
	print 'interrupted!'