#!/usr/bin/env python

"""


"""
import os
from tms import *

def collect_TCPRetrans():
    myList=[]    
    
    try:
        fileobj = open('/proc/net/netstat','r')
        fileReader = fileobj.readlines()
	#print fileReader
	#print ""
        fileobj.close()
        #reading /proc/net/netstat file
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


    print "system.tcp.ListenDrops ",myList[1][21],tms()
    print ""
    print "system.tcp.TCPFastRetrans",myList[1][45],tms() 
    print ""
    print "system.tcp.TCPSlowStartRetrans",myList[1][47],tms() 
    print ""
    print "system.tcp.TCPTimeOuts",myList[1][48],tms() 
    print ""
    print "system.tcp.TCPBacklogDrop", myList[1][75],tms() 
    print ""

    #print "system.interface.",myList[2][0],".rxpackets ",myList[2][2]
    #print "system.interface.",myList[2][0],".txbytes ",myList[2][9]
    #print "system.interface.",myList[2][0],".rxpackets ",myList[2][10]
    

def main():
    v = collect_TCPRetrans()


if __name__ == "__main__":
    main()

"""
$ ./Collect_TCPRetrans.py
system.tcp.ListenDrops  0 1490392903879

system.tcp.TCPFastRetrans 0 1490392903879

system.tcp.TCPSlowStartRetrans 50 1490392903879

system.tcp.TCPTimeOuts 248 1490392903879

system.tcp.TCPBacklogDrop 0 1490392903879         
"""

