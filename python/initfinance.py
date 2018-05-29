import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import fix_yahoo_finance as yf
import sqlite3 as sq3

yf.pdr_override()
dateToday = dt.date.today()
today = dateToday.strftime("%Y-%m-%d")
startDay = dateToday.replace(year=dateToday.year - 3).strftime("%Y-%m-%d")

kospi = web.get_data_yahoo("122630.KS", startDay, today)
gold = web.get_data_yahoo("GC=F", startDay, today)
dollar = web.get_data_yahoo("KRW=X", startDay, today)
cny = web.get_data_yahoo("CNY=X", startDay, today)

con = sq3.connect('../db/finance.db')

kospi.to_sql('kospi', con)
gold.to_sql('gold', con)
dollar.to_sql('dollar', con)
cny.to_sql('cny', con)
