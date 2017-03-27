#!/usr/bin/env python

"""
This function collects:

# Tcp: RtoAlgorithm RtoMin RtoMax MaxConn ActiveOpens PassiveOpens AttemptFails EstabResets CurrEstab InSegs OutSegs RetransSegs 
# Tcp: 1 200 120000 -1 4828 4261 5 5 380 515264340 1324251168 2482 0 25 0


"""
import os
import re
from tms import *
import itertools

def collect_TCPSegs():
    myList=[]    
    mydict= {}
    g = []
    keys = []
    values = []

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
    #print ""
    
    print "system.tcp.AciveOpens",myList[7][5],tms()
    print ""
    print "system.tcp.PassiveOpens",myList[7][6],tms()
    print ""
    print "system.tcp.EstabRsts",myList[7][8],tms()
    print ""
    print "system.tcp.InSegs",myList[7][10],tms()
    print ""
    print "system.tcp.OutSegs",myList[7][11],tms()
    print ""
    print "system.tcp.ReTransSegs",myList[7][12],tms()
    print ""
    print "system.tcp.OutRst", myList[7][14],tms()   
    print ""
    
 
    """ 
    for m in (0,len(myList)):
        if re.match("Tcp",myList[m][0]):
    	    print "system.tcp." ,myList[m][5] ,".", myList[n][5],tms()
    	    print "system.tcp." ,myList[m][6] ,".", myList[n][6],tms()
    	    print "system.tcp." ,myList[m][8] ,".", myList[n][8],tms()
    	    print "system.tcp." ,myList[m][10] ,".", myList[n][10],tms()
    	    print "system.tcp." ,myList[m][11] ,".", myList[n][11],tms()
    	    print "system.tcp." ,myList[m][12] ,".", myList[n][12],tms()
    	    print "system.tcp." ,myList[m][14] ,".", myList[n][14],tms()
    #print "system.tcp.PassiveOpens",myList[7][6],tms()
    #print "system.tcp.EstabRsts",myList[7][8],tms()
    #print "system.tcp.InSegs",myList[7][10],tms()
    #print "system.tcp.OutSegs",myList[7][11],tms()
    #print "system.tcp.ReTransSegs",myList[7][12],tms()
    #print "system.tcp.OutRst", myList[7][14],tms()
    """
    

def main():
    v = collect_TCPSegs()


if __name__ == "__main__":
    main()

"""
$ ./Collect_TCPSegs.py
system.tcp.AciveOpens 112 1490393063437

system.tcp.PassiveOpens 26 1490393063437

system.tcp.EstabRsts 25 1490393063438

system.tcp.InSegs 2282365 1490393063438

system.tcp.OutSegs 2248560 1490393063438

system.tcp.ReTransSegs 335 1490393063438

system.tcp.OutRst 148 1490393063438                
"""

