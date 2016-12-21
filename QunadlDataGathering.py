import pandas as pd 
import os
import quandl
import time


api_key = '6GRG9BiEz-maqagk9H5z'

# data =quandl.get("WIKI/KO",trim_start = "2000-12-12",trim_end = "2015-12-12")
# print(data)
path = "D:\python_sklearn\intraQuarter"

def Stock_prices():
	df = pd.DataFrame()
	statspath = path+"\\_KeyStats"
	stock_list = [x[0] for x in os.walk(statspath)]
	# print (stock_list[1])

	for each_dir in stock_list[1:]:
		try:
			ticker = each_dir.split("\\")[4]
			name  = "WIKI/" + ticker.upper()
			data = quandl.get(name,trim_start = "2000-12-12",trim_end = "2015-12-12",authtoken=api_key)
			data[ticker.upper()]  = data["Adj. Close"]
			df = pd.concat([df,data[ticker.upper()]],axis =1)
		except Exception as e:
			print(str(e))
			time.sleep(10)
			try:
				ticker = each_dir.split("\\")[4]
				name  = "WIKI/" + ticker.upper()
				data = quandl.get(name,trim_start = "2000-12-12",trim_end = "2015-12-12",authtoken=api_key)
				data[ticker.upper()]  = data["Adj. Close"]
				df = pd.concat([df,data[ticker.upper()]],axis =1)
			except Exception as x:
				print(str(x))

	df.to_csv("stock_prices3.csv")


Stock_prices()