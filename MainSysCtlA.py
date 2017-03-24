#!/usr/bin/env python


"""

This program is the Main program

"""
import time

from Collect_CpuStats import *
from Collect_IOStats import *
from Collect_NetStats import *
from Collect_TCPRetrans import *
from Collect_TCPSegs import *
from Collect_VMStat import *

def main():
	while(1):
	    cpu  = collect_CPUStats()
	    io   = collect_IOStats()
	    net  = collect_NetStats
	    tcpR = collect_TCPRetrans()
            tcpS = collect_TCPSegs()
	    vm   = collect_VMStat()
	
	    time.sleep(5)
            print ""
	    print "------------------------------"
            print ""
	
if __name__ == "__main__":
    main()

"""
$ ./MainSysCtlA.py
system. cpu .user. 11086278 1490392314547

system. cpu .sys. 2642 1490392314547

system. cpu .idle. 20413867113424823 1490392314547

system. cpu .intr. 17737 1490392314547

system. cpu .softirq. 81560 1490392314547

system. cpu0 .user. 2829306 1490392314547

system. cpu0 .sys. 429 1490392314547

system. cpu0 .idle. 521309128179129 1490392314547

system. cpu0 .intr. 4849 1490392314548

system. cpu0 .softirq. 21311 1490392314548

system. cpu1 .user. 2756534 1490392314548

system. cpu1 .sys. 591 1490392314548

system. cpu1 .idle. 509210828370883 1490392314548

system. cpu1 .intr. 4966 1490392314548

system. cpu1 .softirq. 28404 1490392314548

system. cpu2 .user. 2754415 1490392314548

system. cpu2 .sys. 869 1490392314549
 
.
.
.
.

"""
