#!/usr/bin/env python

"""
This function collects:

CPUSTATS

"""
import os
import re

def collect_CPUStats():
    myList=[]    
    myDict={}
    
    try:
        fileobj = open('/proc/stat','r')
        fileReader = fileobj.readlines()
	#print fileReader
	#print ""
        fileobj.close()
    except IOError:
        print "File does not Exist"

    #print fileReader
    #print ""

    k =[ x.strip(' ') for x in fileReader]
    #print k
  
    for i in k:
        myList.append(i.split())
	
    #print myList	   
    #print ""
   
    for m in range(0,len(myList)-1):
	if re.match('cpu',myList[m][0]):
            print "system.",myList[m][0],".user.",myList[m][1]
            print "system.",myList[m][0],".sys.",myList[m][2]
    	    print "system.",myList[m][0],".idle.",(myList[m][3] + myList[m][4])
	    print "system.",myList[m][0],".intr.",myList[m][5]
	    print "system.",myList[m][0],".softirq.",myList[m][6]
	

"""
$ ./Collect_CpuStats.py
system. cpu .user. 10734288
system. cpu .sys. 1363
system. cpu .idle. 1947788648303163
system. cpu .intr. 11566
system. cpu .softirq. 63453
system. cpu0 .user. 2737065
system. cpu0 .sys. 196
system. cpu0 .idle. 496371711920897
system. cpu0 .intr. 3081
system. cpu0 .softirq. 18019
system. cpu1 .user. 2668375
system. cpu1 .sys. 525
system. cpu1 .idle. 485847312101568
system. cpu1 .intr. 3149
system. cpu1 .softirq. 17072
system. cpu2 .user. 2668331
system. cpu2 .sys. 287
system. cpu2 .idle. 482210512139590
system. cpu2 .intr. 2727
system. cpu2 .softirq. 15149
system. cpu3 .user. 2660516
system. cpu3 .sys. 353
system. cpu3 .idle. 483359012141106
system. cpu3 .intr. 2608
system. cpu3 .softirq. 13211                   

"""
    

def main():
    v = collect_CPUStats()


if __name__ == "__main__":
    main()

"""

"""

