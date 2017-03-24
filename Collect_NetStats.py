#!/usr/bin/env python

"""


"""
import os
import re
from tms import *

def collect_NetStats():
    myList=[]    
    
    try:
        fileobj = open('/proc/net/dev','r')
        fileReader = fileobj.readlines()
	#print fileReader
	#print ""
        fileobj.close()
        #reading /proc/net/dev file
    except IOError:
        print "File does not Exist"

    Removing_chars = [s.replace(':','') for s in fileReader]
    #print Removing_chars
    #print " "

    k =[ x.strip(' ') for x in Removing_chars]
    #print k
  
    for i in k:
        myList.append(i.split())
	
    #print myList	    
    #[['Inter-|', 'Receive', '|', 'Transmit'], ['face', '|bytes', 'packets', 'errs', 'drop', 'fifo', 'frame', 'compressed', 'multicast|bytes', 'packets', 'errs', 'drop', 'fifo', 'colls', 'carrier', 'compressed'], ['eth0', '6618241', '47334', '0', '0', '0', '0', '0', '0', '8618887', '32928', '0', '0', '0', '0', '0', '0'], ['eth1', '271777', '2056', '0', '0', '0', '0', '0', '0', '1526', '17', '0', '0', '0', '0', '0', '0'], ['lo', '3631621', '17966', '0', '0', '0', '0', '0', '0', '3631621', '17966', '0', '0', '0', '0', '0', '0']] 

    for m in range(0, len(myList)):
	if re.search(r"^(eth|l)" , myList[m][0]):
	    print "system.interface.",myList[m][0],".rxbytes ",myList[m][1],tms()
            print " "
	    print "system.interface.",myList[m][0],".rxpackets ",myList[m][2],tms()
            print " "
	    print "system.interface.",myList[m][0],".txbytes ",myList[m][9],tms()
    	    print " "
	    print "system.interface.",myList[m][0],".rxpackets ",myList[m][10],tms()
            print " "
    ##regex to search for the interface card starting from 'eth' or 'l'  

def main():
    v = collect_NetStats()


if __name__ == "__main__":
    main()

"""
$ ./Collect_NetStats.py
system.interface. eth0 .rxbytes  145673281 1490392635191

system.interface. eth0 .rxpackets  2053875 1490392635192

system.interface. eth0 .txbytes  406193562 1490392635192

system.interface. eth0 .rxpackets  2008502 1490392635192

system.interface. eth1 .rxbytes  3844150 1490392635192

system.interface. eth1 .rxpackets  27638 1490392635192

system.interface. eth1 .txbytes  1526 1490392635192

system.interface. eth1 .rxpackets  17 1490392635192

system.interface. lo .rxbytes  56984777 1490392635192

system.interface. lo .rxpackets  278047 1490392635192

system.interface. lo .txbytes  56984777 1490392635192

system.interface. lo .rxpackets  278047 1490392635192
"""

