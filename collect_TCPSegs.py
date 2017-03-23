#!/usr/bin/env python

"""
This function collects:

# Tcp: RtoAlgorithm RtoMin RtoMax MaxConn ActiveOpens PassiveOpens AttemptFails EstabResets CurrEstab InSegs OutSegs RetransSegs 
# Tcp: 1 200 120000 -1 4828 4261 5 5 380 515264340 1324251168 2482 0 25 0


"""
import os
from tms import *

def collect_TCPSegs():
    myList=[]    
    
    try:
        fileobj = open('/proc/net/snmp','r')
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

    print "system.tcp.ActiveOpens ",myList[7][5],tms()
    print "system.tcp.PassiveOpens",myList[7][6],tms()
    print "system.tcp.EstabRsts",myList[7][8],tms()
    print "system.tcp.InSegs",myList[7][10],tms()
    print "system.tcp.OutSegs",myList[7][11],tms()
    print "system.tcp.ReTransSegs",myList[7][12],tms()
    print "system.tcp.OutRst", myList[7][14],tms()

    

def main():
    v = collect_TCPSegs()


if __name__ == "__main__":
    main()

"""
$ ./collect_TCPSegs.py
system.tcp.ActiveOpens  32
system.tcp.PassiveOpens 17
system.tcp.EstabRsts 13
system.tcp.InSegs 115318
system.tcp.OutSegs 98301
system.tcp.ReTransSegs 7
system.tcp.OutRst 50                 
"""

