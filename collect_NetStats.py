#!/usr/bin/env python

"""


"""
import os

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

    print "system.interface.",myList[2][0],".rxbytes ",myList[2][1]
    print "system.interface.",myList[2][0],".rxpackets ",myList[2][2]
    print "system.interface.",myList[2][0],".txbytes ",myList[2][9]
    print "system.interface.",myList[2][0],".rxpackets ",myList[2][10]
    

def main():
    v = collect_NetStats()
    #Number_of_lines = myList[2]
    #v = vmstat(path_of_file,Number_of_lines)


if __name__ == "__main__":
    main()

"""
$ ./netstat.py
system.interface. eth0 .rxbytes  6700845
system.interface. eth0 .rxpackets  48346
system.interface. eth0 .txbytes  8710521
system.interface. eth0 .rxpackets  33479  

"""

