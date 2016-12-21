#sklerarn leanier svm next level of sklearn_linearsvm3
import urllib.request
import pandas as pd
import os 
import time
from datetime import datetime
import math
from time import mktime

path = "D:\python_sklearn\intraQuarter"

def Check_Yahoo():
    statspath = path+'\\_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in stock_list[1:]:
        try:
            e = e.replace("D:\python_sklearn\intraQuarter\_KeyStats\\","")
            link = "http://in.finance.yahoo.com/q/ks?s="+e.upper()
            # link ="http://finance.yahoo.com/quote/"+e.upper()+"/key-statistics?p="+e.upper()
            # link = "http://finance.yahoo.com/q/ks?s="+e.upper()+"+Key+Statistics"
            resp = urllib.request.urlopen(link).read()

            save = "D:\\python_Data_Analysis\\forward\\"+str(e)+".html"
            store = open(save,"w")
            store.write(str(resp))
            store.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)


Check_Yahoo()   