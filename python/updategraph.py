import numpy as np
import pandas as pd
import pandas.io.sql as pds
import sqlite3 as sq3
import datetime as dt

def getDF(finance, startDay, strKind):
    init_finance = finance[finance.Date >= startDay].Close.values[0]
    select_finance = finance[finance.Date >= startDay]
    return pd.DataFrame({'Date':select_finance['Date'], strKind:select_finance['Close'].values/init_finance}) 

def makeJSFile(startDay, fileName, subTitle):  
    df_kospi = getDF(kospi, startDay, 'KOSPI')
    df_dollar = getDF(dollar, startDay, 'Dollar')
    df = pd.merge(df_kospi, df_dollar, how='inner', left_on='Date', right_on='Date')

    df_gold = getDF(gold, startDay, 'Gold')
    df = pd.merge(df, df_gold, how='inner', left_on='Date', right_on='Date')

    df_cny = getDF(cny, startDay, 'CNY')
    df = pd.merge(df, df_cny, how='inner', left_on='Date', right_on='Date')
    
    data = ""

    for i in df.index:
        data += "[new Date('{0}'), {1:.2f}, {2:.2f}, {3:.2f}, {4:.2f}],\n\t\t".format(df.Date[i].split()[0],df.KOSPI[i],df.Dollar[i],df.Gold[i],df.CNY[i])
    
    data = data.strip(",\n\t")

    txtGoogle = '''    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);'''
        
    txtData = '''var data = new google.visualization.DataTable();
        data.addColumn('date', 'Day');
        data.addColumn('number', 'KOSPI');
        data.addColumn('number', 'Dollar');
        data.addColumn('number', 'Gold');
        data.addColumn('number', 'CNY');

        data.addRows([
         ''' + data + '''
        ]);'''   

    txtOption = '''

        var options = {
            title: '지수변동 ''' + subTitle + '''\',
            legend: {
                position: 'top'
             }
        };'''

    txtFunction =  '''

    function drawChart() {

    ''' + txtData + txtOption + '''
    
    var chart = new google.visualization.LineChart(document.getElementById('chart1'));
    
    chart.draw(data, options);
}'''
   
    f = open(fileName,'w')
    f.write(txtGoogle)
    f.write(txtFunction)
    f.close()
    
    return

con = sq3.connect('../db/'+'finance.db')
kospi = pds.read_sql('SELECT * FROM kospi', con)
dollar = pds.read_sql('SELECT * FROM dollar', con)
gold = pds.read_sql('SELECT * FROM gold', con)
cny = pds.read_sql('SELECT * FROM cny', con)

dateToday = dt.date.today()
today = dateToday.strftime("%Y-%m-%d 00:00:00")
start_3year = dateToday.replace(year = dateToday.year - 3).strftime("%Y-%m-%d 00:00:00")
start_1year = dateToday.replace(year = dateToday.year - 1).strftime("%Y-%m-%d 00:00:00")
start_3month = dateToday.replace(month = dateToday.month - 3).strftime("%Y-%m-%d 00:00:00")
start_1month = dateToday.replace(month = dateToday.month - 1).strftime("%Y-%m-%d 00:00:00")

startDays = [start_3year, start_1year, start_3month, start_1month]
scriptFiles = ['../script/graph_3year.js','../script/graph_1year.js','../script/graph_3month.js','../script/graph_1month.js']
subTitles = ['3 Years','1 Years','3 months','1 months']
fileLists = pd.DataFrame({'Date':startDays, 'File':scriptFiles, 'SubTitle':subTitles}, index=[0,1,2,3])

for index_f in fileLists.index:
    makeJSFile(fileLists.Date[index_f], fileLists.File[index_f], fileLists.SubTitle[index_f])
