# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:07:44 2019

@author: Nagasudhir
Using Popen to communicate with exe file
https://docs.python.org/3.4/library/subprocess.html#subprocess.Popen.communicate

use shlex to parse command string if required
shlex.split(/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'")
will give
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
"""

from subprocess import Popen, PIPE, TimeoutExpired
# using communicate method to read data from Popen -- this is the preferred method
command = "./DummyPmuNodeAdapter.exe"
proc = Popen([command, "--from_time", "2019_09_01_00_00_00", "--to_time", "2019_09_01_00_01_00"], stdout=PIPE)
try:
    outs, errs = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
resp = outs.decode("utf-8")


# using loop to fetch all chunks from Popen
command = "./DummyPmuNodeAdapter.exe"
process = Popen([command, "--from_time", "2019_09_01_00_00_00", "--to_time", "2019_09_01_00_01_00"], stdout=PIPE)
resp = ""
while True:
    output = process.stdout.read()
    if process.poll() is not None:
        break
    if output:
        resp = resp + output.decode("utf-8")        
rc = process.poll()

# convert epoch milliseconds to datetime
import datetime as dt
epochMs = 1567276200040
timeObj = dt.datetime.fromtimestamp(epochMs/1000)
timeObj.strftime('%d-%m-%Y %H:%M:%S.%f')
