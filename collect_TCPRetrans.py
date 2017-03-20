#!/usr/bin/env python

"""


"""
import os

def collect_TCPRetrans():
    myList=[]    
    
    try:
        fileobj = open('/proc/net/netstat','r')
        fileReader = fileobj.readlines()
	#print fileReader
	#print ""
        fileobj.close()
        #reading /proc/meminfo file
    except IOError:
        print "File does not Exist"

    #print fileReader
    print ""

    k =[ x.strip(' ') for x in fileReader]
    #print k
  
    for i in k:
        myList.append(i.split())
	
    #print myList	    


    print "system.tcp.ListenDrops ",myList[1][21]
    print "system.tcp.TCPFastRetrans",myList[1][45]
    print "system.tcp.TCPSlowStartRetrans",myList[1][47]
    print "system.tcp.TCPTimeOuts",myList[1][48]
    print "system.tcp.TCPBacklogDrop", myList[1][75]

    #print "system.interface.",myList[2][0],".rxpackets ",myList[2][2]
    #print "system.interface.",myList[2][0],".txbytes ",myList[2][9]
    #print "system.interface.",myList[2][0],".rxpackets ",myList[2][10]
    

def main():
    v = collect_TCPRetrans()
    #Number_of_lines = myList[2]
    #v = vmstat(path_of_file,Number_of_lines)


if __name__ == "__main__":
    main()

"""
$ ./collect_TCPRetrans.py

system.tcp.ListenDrops  0
system.tcp.TCPFastRetrans 0
system.tcp.TCPSlowStartRetrans 0
system.tcp.TCPTimeOuts 6
system.tcp.TCPBacklogDrop 0                   
"""

