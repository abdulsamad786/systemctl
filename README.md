# systemctl
-------------------------System Stats project with python---------------------------------

The task is to implement all agents listed below in Python. 
Implement them as a separate python program. Once all agents are
 implemented and output meets the requirements, combine them into one python
 program (similar to perl script provided). Implement them as python functions.
 Call functions to collect statistics from these agents in a while loop and store
 stats in a single array. Print the array and then sleep for 5 seconds before starting 
 a new iteration. Make sure at every iteration, initialize the array to store new statistics.

1- vmstat.py
input: head -4 /proc/meminfo 

output:

system.mem.free_cached 482556364 1488944342

system.mem.free_unused 482083088 1488944342

system.mem.used -461029828 1488944342

-----

2 - iostat.py

input: cat /proc/diskstats

output: 

system.io.xvda.WriteIOPS 2061821 1488944524

system.io.xvda.ReadSectors  874842  1488944524

..

..

NOTE: Disk name may be different on your computer

----

3 - netstat.py

input: cat /proc/net/dev 

output: 

system.interface.lo.rxbytes 232894241 1488944676

system.interface.lo.rxpackets 3276724 148894467

system.interface.lo.txbytes 232894241 1488944676

system.interface.lo.txpackets 3276724 1488944676

..system.interface.eth0.rxbytes 569189611 1488944676

..system.interface.eth0.rxpackets 1841181 1488944676

..system.interface.eth0.txbytes 4230680713 1488944676

..system.interface.eth0.txpackets 1788859 1488944676

-----

4 - tcpRetrans.py

input: cat /proc/net/netstat

output:

system.tcp.ListenDrops 326751 1488944900

system.tcp.TCPFastRetrans 195 1488944900

system.tcp.TCPSlowStartRetrans 73 1488944900

system.tcp.TCPTimeOuts 3 1488944900

system.tcp.TCPBacklogDrop 0 1488944900

----

5- tcpSegs.py

input: cat /proc/net/snmp

output

..system.tcp.ActiveOpens 409824 1488945017

system.tcp.PassiveOpens 328021 1488945017

system.tcp.EstabRsts 15 1488945017

system.tcp.InSegs 4809078 1488945017

system.tcp.OutSegs 7002371 1488945017

system.tcp.RetransSegs 524 1488945017

system.tcp.OutRst 70303 1488945017

---

6 - mpstat.py

input: cat /proc/stat

output:

..system.CPU.ctxt 1320830232 1488945299

..system.CPU.procs_running 2 1488945299

..system.CPU.procs_blocked 0 1488945299

..system.CPU.cpu0.user 249005 1488945299

..system.CPU.cpu0.sys 111729 1488945299

..system.CPU.cpu0.idle 33222395 1488945299

..system.CPU.cpu0.intr 0 1488945299

..system.CPU.cpu0.softirq 46 1488945299

..system.CPU.cpu1.user 142096 1488945299

..system.CPU.cpu1.sys 100893 1488945299

..system.CPU.cpu1.idle 33351741 1488945299

..system.CPU.cpu1.intr 0 1488945299

..system.CPU.cpu1.softirq 10 1488945299

..

..

-------------


