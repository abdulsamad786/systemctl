#!/usr/bin/env python

"""


"""
import os
import re

def collect_NetStats():
    myList=[]    
    
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
	
    #print myList	    
    #[['Inter-|', 'Receive', '|', 'Transmit'], ['face', '|bytes', 'packets', 'errs', 'drop', 'fifo', 'frame', 'compressed', 'multicast|bytes', 'packets', 'errs', 'drop', 'fifo', 'colls', 'carrier', 'compressed'], ['eth0', '6618241', '47334', '0', '0', '0', '0', '0', '0', '8618887', '32928', '0', '0', '0', '0', '0', '0'], ['eth1', '271777', '2056', '0', '0', '0', '0', '0', '0', '1526', '17', '0', '0', '0', '0', '0', '0'], ['lo', '3631621', '17966', '0', '0', '0', '0', '0', '0', '3631621', '17966', '0', '0', '0', '0', '0', '0']] 

    for m in range(0, len(myList)):
	if re.search(r"^(eth|l)" , myList[m][0]):
	    print "system.interface.",myList[m][0],".rxbytes ",myList[m][1]
	    print "system.interface.",myList[m][0],".rxpackets ",myList[m][2]
	    print "system.interface.",myList[m][0],".txbytes ",myList[m][9]
	    print "system.interface.",myList[m][0],".rxpackets ",myList[m][10]
    #regex to search for the interface card starting from 'eth' or 'l'     

def main():
    v = collect_NetStats()
    #Number_of_lines = myList[2]
    #v = vmstat(path_of_file,Number_of_lines)


if __name__ == "__main__":
    main()

"""
$ ./collect_NetStats.py
system.interface. eth0 .rxbytes  23366088
system.interface. eth0 .rxpackets  106380
system.interface. eth0 .txbytes  15206596
system.interface. eth0 .rxpackets  70560
system.interface. eth1 .rxbytes  2887061
system.interface. eth1 .rxpackets  20821
system.interface. eth1 .txbytes  1526
system.interface. eth1 .rxpackets  17
system.interface. lo .rxbytes  42528277
system.interface. lo .rxpackets  207571
system.interface. lo .txbytes  42528277
system.interface. lo .rxpackets  207571

"""

