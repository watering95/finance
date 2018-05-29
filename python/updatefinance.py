import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import fix_yahoo_finance as yf
import sqlite3 as sq3

yf.pdr_override()
dateToday = dt.date.today()
today = dateToday.strftime("%Y-%m-%d")

kospi = web.get_data_yahoo("122630.KS", today)
gold = web.get_data_yahoo("GC=F", today)
dollar = web.get_data_yahoo("KRW=X", today)
cny = web.get_data_yahoo("CNY=X", today)

con = sq3.connect('../db/finance.db')

kospi.to_sql('kospi', con, if_exists='append')
gold.to_sql('gold', con, if_exists='append')
dollar.to_sql('dollar', con, if_exists='append')
cny.to_sql('cny', con, if_exists='append')
