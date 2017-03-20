#!/usr/bin/env python

"""


"""
import os
from nltk.tokenize import word_tokenize

def collect_NetStats():
    myList=[]    
    newList=[]
    saveDataList=[]
    
    try:
        fileobj = open('/proc/net/dev','r')
        fileReader = fileobj.readlines()
	#print fileReader
	#print ""
        fileobj.close()
        #reading /proc/meminfo file
    except IOError:
        print "File does not Exist"

    v = [s.replace(':','') for s in fileReader]
    #print v
    #print " "

    k =[ x.strip(' ') for x in v]
    #print k
  
    for i in k:
        myList.append(i.split())
	
    print myList	    

    print "system.interface.",myList[2][0],".rxbytes ",myList[2][1]
    print "system.interface.",myList[2][0],".rxpackets ",myList[2][2]
    print "system.interface.",myList[2][0],".txbytes ",myList[2][9]
    print "system.interface.",myList[2][0],".rxpackets ",myList[2][10]
    
"""
    
    #removing spaces from list elements and creating a newList so that
    #it is converted further into tokens
    for i in myList:
        i = i.split()
        newList.append(i)
    #newList = [['MemTotal:', '1017564', 'kB'], ['MemFree:', '108396', 'kB'], ['Buffers:', '58764', 'kB'], ['Cached:', '219060', 'kB']]
    #calculations of memmory: free_cached, free_unused, used
    memTotal = newList[0][1]
    free_cached = int(newList[2][1] + newList[3][1])
    free_unused = int(newList[1][1])
    used = int(newList[0][1]) - free_cached - free_cached

    saveDataList.append(['system.mem.free_cached ',' ', free_cached , ' ',memTotal])
    saveDataList.append(['system.mem.free_unused ' ,newList[0][1], ' ',memTotal ])
    saveDataList.append(['system.mem.used  ', used, ' ' ,memTotal ])
    #print saveDataList
    #print ""

    #for data_stored in range(0, len(saveDataList)-1):
    #    print saveDataList[data_stored]

    print 'system.mem.free_cached ',' ', free_cached , ' ',memTotal
    print 'system.mem.free_unused ' ,newList[0][1], ' ',memTotal
    print 'system.mem.used  ', used, ' ' ,memTotal
"""

"""
$ ./vmstat.py
system.mem.free_cached    62756208932   1017564
system.mem.free_unused  1017564   1017564
system.mem.used   -125511400300   1017564 

"""

def main():
    v = collect_NetStats()
    #Number_of_lines = myList[2]
    #v = vmstat(path_of_file,Number_of_lines)


if __name__ == "__main__":
    main()

