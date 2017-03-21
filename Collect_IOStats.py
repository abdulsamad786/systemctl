#!/usr/bin/env python

"""
This function collects:

IOSTATS

"""
import os

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

    print "system.io.",myList[0][2],".ReadIOPS ",myList[0][3]
    print "system.io.",myList[1][2],".WriteIOPS",myList[1][7]
    print "system.io.",myList[2][2],".ReadIOPS ",myList[2][5]
    print "system.io.",myList[3][2],".ReadIOPS ",myList[3][9]
    print "system.io.",myList[4][2],".ReadIOPS ",myList[4][6]
    print "system.io.",myList[5][2],".ReadIOPS ",myList[5][10]
    print "system.io.",myList[6][2],".ReadIOPS ",myList[6][13]
    print "system.io.",myList[7][2],".ReadIOPS ",myList[7][12]
   
    

def main():
    v = collect_IOStats()


if __name__ == "__main__":
    main()

"""
$ ./Collect_IOStats.py
system.io. ram0 .ReadIOPS  0
system.io. ram1 .WriteIOPS 0
system.io. ram2 .ReadIOPS  0
system.io. ram3 .ReadIOPS  0
system.io. ram4 .ReadIOPS  0
system.io. ram5 .ReadIOPS  0
system.io. ram6 .ReadIOPS  0
system.io. ram7 .ReadIOPS  0              

"""

