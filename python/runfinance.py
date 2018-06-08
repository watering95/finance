import os
import schedule
import time
import datetime
from subprocess import call

path = '''../db/finance.db'''

def runProgram(cmd):
	call(cmd.split())
	return

def log(data):
	f = open('log_finance.txt', 'a')
	f.write(datetime.datetime.now().isoformat())
	f.write(data)
	f.close()
	return

def job():
	runProgram('''python updatefinance.py &''')
	time.sleep(10)
	runProgram('''python updategraph.py &''')
	log(' : update finance.db, update graph\n')
	return	
		
if os.path.exists(path) == False:
	runProgram('''python initfinance.py &''')	
	log(' : init finance.db\n')

print('Start finance.py')
schedule.every().day.at("17:40").do(job)

while 1:
	schedule.run_pending()
	time.sleep(1)