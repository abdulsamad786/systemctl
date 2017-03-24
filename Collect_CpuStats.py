#!/usr/bin/env python

"""
This function collects:

CPUSTATS

"""
import os
import re
from tms import *

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
            print "system.",myList[m][0],".user.",myList[m][1],tms()
	    print""
            print "system.",myList[m][0],".sys.",myList[m][2],tms()
	    print""
    	    print "system.",myList[m][0],".idle.",(myList[m][3] + myList[m][4]),tms()
	    print""
	    print "system.",myList[m][0],".intr.",myList[m][5],tms()
	    print""
	    print "system.",myList[m][0],".softirq.",myList[m][6],tms()
	    print""
	

"""
$ ./Collect_CpuStats.py
system. cpu .user. 11078562 1490371341143

system. cpu .sys. 2642 1490371341143

system. cpu .idle. 20391554105078880 1490371341143

system. cpu .intr. 17339 1490371341143

system. cpu .softirq. 78409 1490371341143

system. cpu0 .user. 2827132 1490371341143

system. cpu0 .sys. 429 1490371341143

system. cpu0 .idle. 520651226093089 1490371341143

system. cpu0 .intr. 4717 1490371341143

system. cpu0 .softirq. 20975 1490371341143

system. cpu1 .user. 2754282 1490371341143

system. cpu1 .sys. 591 1490371341143

system. cpu1 .idle. 508646926288465 1490371341144

system. cpu1 .intr. 4896 1490371341144

system. cpu1 .softirq. 26005 1490371341144

system. cpu2 .user. 2752701 1490371341144

system. cpu2 .sys. 869 1490371341144

system. cpu2 .idle. 504900426338462 1490371341144

system. cpu2 .intr. 3808 1490371341144

system. cpu2 .softirq. 17148 1490371341144

system. cpu3 .user. 2744445 1490371341144

system. cpu3 .sys. 752 1490371341144

system. cpu3 .idle. 504956726358862 1490371341144

system. cpu3 .intr. 3916 1490371341144
                                                

"""
    

def main():
    v = collect_CPUStats()


if __name__ == "__main__":
    main()

"""

"""

