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
from vmstat import *

def main():
	while(1):
	    cpu = collect_CPUStats()
	    io = collect_IOStats()
	    net = collect_NetStats
	    tcpR = collect_TCPRetrans()
            tcpS = collect_TCPSegs()
	    vm = vmstat()
	
	    time.sleep(5)
	    print "------------------------------"
	
if __name__ == "__main__":
    main()
