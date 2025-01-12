import pandas as pd
import os 
import time
from datetime import datetime
import math
from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")



import re


path = "D:\python_sklearn\intraQuarter"

def key_stats(gather=["Total Debt/Equity",
                      'Trailing P/E',
                      'Price/Sales',
                      'Price/Book',
                      'Profit Margin',
                      'Operating Margin',
                      'Return on Assets',
                      'Return on Equity',
                      'Revenue Per Share',
                      'Market Cap',
                        'Enterprise Value',
                        'Forward P/E',
                        'PEG Ratio',
                        'Enterprise Value/Revenue',
                        'Enterprise Value/EBITDA',
                        'Revenue',
                        'Gross Profit',
                        'EBITDA',
                        'Net Income Avl to Common ',
                        'Diluted EPS',
                        'Earnings Growth',
                        'Revenue Growth',
                        'Total Cash',
                        'Total Cash Per Share',
                        'Total Debt',
                        'Current Ratio',
                        'Book Value Per Share',
                        'Cash Flow',
                        'Beta',
                        'Held by Insiders',
                        'Held by Institutions',
                        'Shares Short (as of',
                        'Short Ratio',
                        'Short % of Float',
                        'Shares Short (prior ']):
    statspath = path+'\\_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'Price',
                                 'stock_p_change',
                                 'SP500',
                                 'sp500_p_change',
                                 'Difference',
                                 ##############
                                 'DE Ratio',
                                 'Trailing P/E',
                                 'Price/Sales',
                                 'Price/Book',
                                 'Profit Margin',
                                 'Operating Margin',
                                 'Return on Assets',
                                 'Return on Equity',
                                 'Revenue Per Share',
                                 'Market Cap',
                                 'Enterprise Value',
                                 'Forward P/E',
                                 'PEG Ratio',
                                 'Enterprise Value/Revenue',
                                 'Enterprise Value/EBITDA',
                                 'Revenue',
                                 'Gross Profit',
                                 'EBITDA',
                                 'Net Income Avl to Common ',
                                 'Diluted EPS',
                                 'Earnings Growth',
                                 'Revenue Growth',
                                 'Total Cash',
                                 'Total Cash Per Share',
                                 'Total Debt',
                                 'Current Ratio',
                                 'Book Value Per Share',
                                 'Cash Flow',
                                 'Beta',
                                 'Held by Insiders',
                                 'Held by Institutions',
                                 'Shares Short (as of',
                                 'Short Ratio',
                                 'Short % of Float',
                                 'Shares Short (prior ',                                
                                 ##############
                                 'Status'])

    sp500_df = pd.DataFrame.from_csv("YAHOO-INDEX_GSPC.csv")
    stock_df = pd.DataFrame.from_csv("stock_prices.csv")
    ticker_list = []

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("\\")[4]
        ticker_list.append(ticker)

        # starting_stock_value = False
        
        # starting_sp500_value = False

        if len(each_file) > 0:
            for file in each_file:
                date_statmp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
                
                unix_time = time.mktime(date_statmp.timetuple())
                full_file_path = each_dir+ '\\'+ file
                source = open(full_file_path,'r').read()
                try :
                    value_list = []

                    for each_data in gather:
                        try:
                            regex =re.escape(each_data) + r'.*?(\d{1,8}\.\d{1,8}M?B?|N/A)%?</td>'
                            value = re.search(regex,source)
                            value =(value.group(1))
                            # print(each_data,value)
                            if "B" in value:
                                value = float(value.replace("B",''))
                                value = value*1000000000

                            elif "M" in value:
                                value = float(value.replace("M",''))

                                value = value*1000000
                                # print (each_data,value)

                            value_list.append(value)

                        except Exception as e:
                            # print (ticker , each_data,file , e)
                            value = "N/A"
                            value_list.append(value)
                    
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row =sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adjusted Close"])
                    except Exception as error:
                        sp500_date = datetime.fromtimestamp(unix_time - 259200).strftime('%Y-%m-%d')
                        row =sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row["Adjusted Close"])

                    one_year_later = int(unix_time+31536000)
                    try:
                        sp500_1y = datetime.fromtimestamp(one_year_later).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_1y)]
                        sp500_1y_value = float(row["Adjusted Close"])

                    except Exception as e:
                        try:
                            sp500_1y = datetime.fromtimestamp(one_year_later -259200).strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df.index == sp500_1y)]
                            sp500_1y_value = float(row["Adjusted Close"])
                        except Exception as e:
                            print("s& p 500 exception",str(e))

                    try:
                        stock_Price_1y = datetime.fromtimestamp(one_year_later).strftime('%Y-%m-%d')
                        row = stock_df[(stock_df.index == stock_Price_1y)][ticker.upper()]
                        stock_1y_value = round(float(row),2)

                    except Exception as e:
                        try:
                            stock_Price_1y = datetime.fromtimestamp(one_year_later -259200).strftime('%Y-%m-%d')
                            row = stock_df[(stock_df.index == stock_Price_1y)][ticker.upper()]
                            stock_1y_value = round(float(row),2)
                        except Exception as e:
                            print("stock_Price_1y exception",str(e))

                    try:
                        stock_Price = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = stock_df[(stock_df.index == stock_Price)][ticker.upper()]
                        stock_Price = round(float(row),2)

                    except Exception as e:
                        try:
                            stock_Price = datetime.fromtimestamp(unix_time -259200).strftime('%Y-%m-%d')
                            row = stock_df[(stock_df.index == stock_Price)][ticker.upper()]
                            stock_Price = round(float(row),2)
                        except Exception as e:
                            print("stock_Price exception",str(e))




                    
                    
                    
                    stock_p_change = round((((stock_1y_value - stock_Price) /stock_Price )* 100),2)
                    SP500_p_change = round((((sp500_1y_value - sp500_value) /sp500_value) * 100),2)

                    Difference = stock_p_change -SP500_p_change
                    if Difference > 0 :
                        status = 1
                    else:
                        status = 0

                    if value_list.count("N/A")>0:
                        pass
                    else:
                        try:
                            df = df.append({'Date':date_statmp,
                                            'Unix':unix_time,
                                            'Ticker':ticker,
                                            'Price':stock_Price,
                                            'stock_p_change':stock_p_change,
                                            'SP500':sp500_value,
                                            'sp500_p_change':SP500_p_change,
                                            'Difference':Difference,
                                            'DE Ratio':value_list[0],
                                            #'Market Cap':value_list[1],
                                            'Trailing P/E':value_list[1],
                                            'Price/Sales':value_list[2],
                                            'Price/Book':value_list[3],
                                            'Profit Margin':value_list[4],
                                            'Operating Margin':value_list[5],
                                            'Return on Assets':value_list[6],
                                            'Return on Equity':value_list[7],
                                            'Revenue Per Share':value_list[8],
                                            'Market Cap':value_list[9],
                                             'Enterprise Value':value_list[10],
                                             'Forward P/E':value_list[11],
                                             'PEG Ratio':value_list[12],
                                             'Enterprise Value/Revenue':value_list[13],
                                             'Enterprise Value/EBITDA':value_list[14],
                                             'Revenue':value_list[15],
                                             'Gross Profit':value_list[16],
                                             'EBITDA':value_list[17],
                                             'Net Income Avl to Common ':value_list[18],
                                             'Diluted EPS':value_list[19],
                                             'Earnings Growth':value_list[20],
                                             'Revenue Growth':value_list[21],
                                             'Total Cash':value_list[22],
                                             'Total Cash Per Share':value_list[23],
                                             'Total Debt':value_list[24],
                                             'Current Ratio':value_list[25],
                                             'Book Value Per Share':value_list[26],
                                             'Cash Flow':value_list[27],
                                             'Beta':value_list[28],
                                             'Held by Insiders':value_list[29],
                                             'Held by Institutions':value_list[30],
                                             'Shares Short (as of':value_list[31],
                                             'Short Ratio':value_list[32],
                                             'Short % of Float':value_list[33],
                                             'Shares Short (prior ':value_list[34],
                                            'Status':status},
                                           ignore_index=True)
                        except Exception as ex:
                            pass

                except Exception as error:
                    # print(error)
                    # print err
                    pass

    # for each_ticker in ticker_list:
    #     try:
    #         plot_df = df[(df['Ticker']) == each_ticker]             
    #         plot_df =plot_df.set_index(['Date'])

    #         if plot_df['Status'][-1] == "Underperforms":
    #             color = 'r'
    #         else:
    #             color = 'g'

    #         plot_df['Differnce'].plot(label=each_ticker,color =color)
    #         plt.legend()
    #     except Exception as error:
    #         pass
    # plt.show()

    # save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    
    df.to_csv("key_stats_acc_perf_no_NA1.csv")
                

                

    
key_stats()

