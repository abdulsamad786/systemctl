#!/usr/bin/env python

"""


"""
import os
import sys
import itertools
from tms import *

def collect_VMStat():
    myList=[] 	      #list will used to store N lines from a fileReader
    newList=[]        #newList used to sote the tokens taken from myList
    saveDataList=[]
    
    try:
        fileobj = open('/proc/meminfo','r')
        fileReader = fileobj.readlines() 
        #print fileReader
        fileobj.close()
        #reading /proc/meminfo file
    except IOError:
        print "File does not Exist"
    
    #now printing first 4 elements of vmstat using itertools.islice function
    #It iterated over the the N line of a file, here N = 4
    myNelements = fileReader
    topNlines= itertools.islice(myNelements,4) 
    #print topNlines
    	
    #converting topNlines to a list, since itertools.islice return
    #an object.
    myList= list(topNlines)
    #print myList
    
    #removing spaces from list elements and creating a newList so that
    #it is converted further into tokens
    for i in myList:
        i = i.split()
        newList.append(i)
    """
    newList = [['MemTotal:', '1017564', 'kB'], ['MemFree:', '108396', 'kB'], ['Buffers:', '58764', 'kB'], ['Cached:', '219060', 'kB']]
    """
    #calculations of memmory: free_cached, free_unused, used
    memTotal = newList[0][1]
    free_cached = int(newList[2][1] + newList[3][1])
    free_unused = int(newList[1][1])
    used = int(newList[0][1]) - free_cached - free_cached

    """
    saveDataList.append(['system.mem.free_cached ',' ', free_cached , ' ',memTotal])
    saveDataList.append(['system.mem.free_unused ' ,newList[0][1], ' ',memTotal ])
    saveDataList.append(['system.mem.used  ', used, ' ' ,memTotal ])
    #print saveDataList
    #print """
    
    #for k in saveDataList:
    #    print k
    print 'system.mem.free_cached ', free_cached,memTotal,tms()
    print ""
    print 'system.mem.free_unused ',newList[0][1],memTotal,tms()   
    print""
    print 'system.mem.used  ', used,memTotal,tms()   
    print""



def main():
    v = collect_VMStat()


if __name__ == "__main__":
    main()
"""
$ ./Collect_VMStat.py
system.mem.free_cached    55920196720   1017564 1490372002755

system.mem.free_unused  1017564   1017564 1490372002755

system.mem.used   -111839375876   1017564 1490372002755 


"""
