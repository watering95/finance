import os
import datetime
from subprocess import call

path = '''../db/finance.db'''
if os.path.exists(path) == False:
	cmd = '''python initfinance.py'''
	cmd_args = cmd.split()
	call(cmd_args)
	f = open('log_finance.txt', 'w')
	f.write(datetime.datetime.now().isoformat())
	f.write(' : init finance.db₩n')
	f.close()
set_time = datetime.time(16, 0, 0)

print('Start finance.py')

while 1:
	now_datetime = datetime.datetime.now()
	now_time = now_datetime.time()
	cmd = '''python updatefinance.py'''
	cmd_args = cmd.split() 

	if now_time == set_time: 
		call(cmd_args)
		f = open('log_finance.txt', 'w')
		f.write(now_time.isoformat())
		f.write(' : update finance.db₩n')
		f.close()
