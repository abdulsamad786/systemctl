#!/usr/bin/env python


"""

This program is the Main program

"""
import time

from Collect_CpuStats import *
from Collect_IOStats import *
from collect_NetStats import *
from collect_TCPRetrans import *
from collect_TCPSegs import *
from Collect_VMStat import *

def main():
	while(1):
	    cpu = collect_CPUStats()
	    io = collect_IOStats()
	    net = collect_NetStats
	    tcpR = collect_TCPRetrans()
            tcpS = collect_TCPSegs()
	    vm = Collect_VMStat()
	
	    time.sleep(5)
	    print "------------------------------"
	
if __name__ == "__main__":
    main()

"""
$ ./MainSysCtlA.py
system. cpu .user. 11060705 1490313204181
None
system. cpu .sys. 2028 1490313204181
None
system. cpu .idle. 2033333881928990 1490313204181
None
system. cpu .intr. 15552 1490313204181
None
system. cpu .softirq. 70836 1490313204181
None
system. cpu0 .user. 2821592 1490313204181
None
system. cpu0 .sys. 214 1490313204181
None
system. cpu0 .idle. 518803220311138 1490313204181
None
system. cpu0 .intr. 4183 1490313204181
None
system. cpu0 .softirq. 20007 1490313204181
None
system. cpu1 .user. 2749878 1490313204181
None
system. cpu1 .sys. 590 1490313204181
None 
.
.
.
.

"""
