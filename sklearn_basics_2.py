import pandas as pd
import os 
import time
from datetime import datetime

path = "D:\python_sklearn\intraQuarter"

def key_stats(gather = "Total Debt/Equity (mrq)"):
	statspath = path+'\\_KeyStats'
	stock_list = [x[0] for x in os.walk(statspath)]
	df = pd.DataFrame(columns =['Date','Unix','Ticker','DE Ratio','Price','stock_p_change','SP500','SP500_p_change'])

	sp500_df = pd.DataFrame.from_csv("YAHOO-INDEX_GSPC.csv")
	ticker_list = []

	for each_dir in stock_list[1:25]:
		each_file = os.listdir(each_dir)
		ticker = each_dir.split("\\")[4]
		ticker_list.append(ticker)

		starting_stock_value = False
		starting_sp500_value = False

		if len(each_file) > 0:
			for file in each_file:
				date_statmp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
				
				unix_time = time.mktime(date_statmp.timetuple())
				full_file_path = each_dir+ '\\'+ file
				source = open(full_file_path,'r').read()
				try :
					value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
					stock_Price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
					try:
						sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
						row =sp500_df[(sp500_df.index == sp500_date)]
						sp500_value = float(row["Adjusted Close"])
					except Exception as error:
						sp500_date = datetime.fromtimestamp(unix_time - 259200).strftime('%Y-%m-%d')
						row =sp500_df[(sp500_df.index == sp500_date)]
						sp500_value = float(row["Adjusted Close"])
					
					if not starting_stock_value:
						starting_stock_value = stock_Price
					if not starting_sp500_value:
						starting_sp500_value = sp500_value
					
					stock_p_change = ((stock_Price -starting_sp500_value) /starting_stock_value )* 100
					SP500_p_change = ((sp500_value -starting_sp500_value) /starting_sp500_value) * 100

					df = df.append({'Date':date_statmp,
						'Unix':unix_time,
						'Ticker':ticker,
						'DE Ratio':value,
						'Price':stock_Price,
						'stock_p_change':stock_p_change,
						'SP500':sp500_value,
						'SP500_p_change':SP500_p_change},ignore_index =True)

				except :
					pass

	save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
	
	df.to_csv(save)
				

				

	
key_stats()

