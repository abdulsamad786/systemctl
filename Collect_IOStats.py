#!/usr/bin/env python

"""
This function collects:

IOSTATS

"""
import os
import re 
from tms import *

def collect_IOStats():
    myList=[]    
    
    try:
        fileobj = open('/proc/diskstats','r')
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

    for m in range(0, len(myList)):
	if re.search(r"^(ram|sda|loop)" , myList[m][2]):    
    	    print "system.io.",myList[m][2],".ReadIOPS ",myList[m][3],tms()
            print ""
    	    print "system.io.",myList[m][2],".WriteIOPS",myList[m][7],tms()
            print ""
            print "system.io.",myList[m][2],".ReadSectors ",myList[m][5],tms()
            print ""
            print "system.io.",myList[m][2],".WriteSectors ",myList[m][9],tms()
            print ""
            print "system.io.",myList[m][2],".ReadTime ",myList[m][6],tms()
            print ""
            print "system.io.",myList[m][2],".WriteTime ",myList[m][10],tms()
            print ""
            print "system.io.",myList[m][2],".QueueSize ",myList[m][13],tms()
            print ""
            print "system.io.",myList[m][2],".Utilization ",myList[m][12],tms()
            print ""
   
    

def main():
    v = collect_IOStats()


if __name__ == "__main__":
    main()

"""
$ ./Collect_IOStats.py
system.io. ram0 .ReadIOPS  0
system.io. ram0 .WriteIOPS 0
system.io. ram0 .ReadSectors  0
system.io. ram0 .WriteSectors  0
system.io. ram0 .ReadTime  0
system.io. ram0 .WriteTime  0
system.io. ram0 .QueueSize  0
system.io. ram0 .Utilization  0
system.io. ram1 .ReadIOPS  0
system.io. ram1 .WriteIOPS 0
system.io. ram1 .ReadSectors  0 
.
.
.
.
"""

