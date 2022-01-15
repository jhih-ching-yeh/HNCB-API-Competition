import csv
import requests
import json
import sys
import jsonpath

def jsonpath_id(text):
	id_list = jsonpath.jsonpath(text,expr = '$.stock_history..buy_category')
	return id_list


csv_columns = ['buy_category', 'num_of_shares', 'trans_category', 'completion_date', 'stock_code', 'channel_category', 'strike_price', 'trans_price']


uuid_url = 'https://www.fintechersapi.com/bank/huanan/getUUIDs?api_key=c72b0eb3-15e1-4d59-b99a-f8c97f4616fe'

uuid = []

for i in range(100):
	r = requests.get('https://www.fintechersapi.com/bank/huanan/getUUIDs?api_key=c72b0eb3-15e1-4d59-b99a-f8c97f4616fe')

	if r.status_code == requests.codes.ok:
		uuid = uuid + json.loads(r.text)['uuid_list']

d = []
aas = 0
for i in range(1000):
	d = []
	for j in range(2016, 2019):
		url = 'https://www.fintechersapi.com/bank/huanan/securities/history?uuid=' + str(uuid[i][0:32]) + '&year=' +str( j) +'&api_key=c72b0eb3-15e1-4d59-b99a-f8c97f4616fe'
		res = requests.get(url)
		res.encoding = 'uft-8'
		if res.status_code == 200:

			s = json.loads(res.text)
			list_id = jsonpath_id ( s )
			if list_id is False:
				aas = 0
				print("!!!")
			else:
				print (res.text)
				d = d + json.loads(res.text)['stock_history']
	
	csv_file = str(uuid[i][0:32]) + '.csv'
	try:
		with open(csv_file, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
			writer.writeheader()
			for data in d:
				writer.writerow(data)
			csvfile.close()
	except IOError:
		print("I/O error")

#csv_file = "Names.csv"


