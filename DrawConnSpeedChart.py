#!/usr/bin/python

### DrawConnSpeedChart  v0.6
### Eric Lee  (leezhenyu@gmail.com)
### Silicon Cloud International Pte Ltd.


import os
import sys
import subprocess
from time import gmtime, strftime
import matplotlib.pyplot as plt
import numpy as np


servers = [[6424,"Tokyo"],[2327,"Taipei"],[3914,"Singapore"],[5029,"New_York"],[4042,"San_Jose"],[4185,"Durham"]]

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def autolabel(speeds):
    # attach some text labels
    for speed in speeds:
        height = speed.get_height()
        ax.text(speed.get_x()+speed.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')


city = []
download = []
upload = []

counter = 0
for server in servers:
	counter += 1
	print ('Test connection speed of ' + server[1] + " [" + str(counter) + "/" + str(len(servers)) + "]" );
	filename = strftime("%Y%m%d%H", gmtime()) + str(server[1]) + ".txt";
	os.system("speedtest-cli --server " + str(server[0]) + " >" + filename);
	speedBenchmarkFile = open(filename,'r')
	text =  speedBenchmarkFile.read()
	downloadSpeed = find_between( text, "Download: ", " Mbit" )
	uploadSpeed = find_between( text, "Upload: ", " Mbit" )
	print "Download: " + str(downloadSpeed)
	print "Upload: " + str(uploadSpeed)
	city.append(server[1])
	try:
		download.append(float(downloadSpeed))
		upload.append(float(uploadSpeed))
	except:  # If speed test connection can't create, fill 0
		download.append(0)
		upload.append(0)


### Draw a bar chart

N = len(servers)

ind = np.arange(N)
width = 0.35

fig, ax = plt.subplots()
speed1 = ax.bar(ind, download, width, color='g') 

speed2 = ax.bar(ind+width, upload, width, color='y') 

ax.set_ylabel('Speed (Mbits)')
ax.set_title('Bandwidth Benchmark at ' + strftime("%Y%m%d GMT %H", gmtime()))
ax.set_xticks(ind+width)
ax.set_xticklabels(city)

ax.legend( (speed1[0], speed2[0]), ('Download', 'Upload') )



autolabel(speed1)
autolabel(speed2)


figFilename = strftime("%Y%m%d%H", gmtime()) + "Benchmark.png"

fig.savefig(figFilename)


print "Save a bar chat file: " + figFilename 



#print "data:" + data
