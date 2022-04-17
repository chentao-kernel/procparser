#!/usr/bin/env python2.7
import sys
import time
from argparse import ArgumentParser

def proc_hex2int(str):
    first_nozero_id = 0
    i = 0
    
    for val in str:
        if str[len(str) - i - 1] != '0':
            first_nozero_id = len(str) - i -1
        i += 1

    #print("=={len} {index} {name}".format(len=len(str), index=first_nozero_id, name=str[first_nozero_id:])) 
    return int(str[first_nozero_id:], 16)

def parameter_parser(file):
    file.seek(0)
    id = 0
    lines = file.readlines()
    while (id < len(lines)):
        filed = lines[id].split()
        val = lines[id + 1].split()
        for i in range(0, len(filed)):
            tmp = "{arg1}:{arg2}".format(arg1=filed[i], arg2=val[i])
            print(tmp)
        id += 2

# https://blog.csdn.net/zgy666/article/details/104391160
def print_softnet_stat():
    print("=============/proc/net/softnet_stat=========")
    FIELDS = ["cpu", "rcv_packets", "drop_packets", "netdev_budget",
             "", "", "", "", "", "queue_locked", "rps_ipi"]
    i = 0

    f_softnet_stat = open("/proc/net/softnet_stat", "r")
    f_softnet_stat.seek(0)
    for line in f_softnet_stat:
        filed = line.split()
        print("cpu:{cpu}, rcv_packets:{rcv_packets}, drop_packets:{drop_packets}, net_budget:{net_budget},\
        queue_locked:{queue_locked}, rps_pip:{rps_pip}".format(cpu=i, rcv_packets=proc_hex2int(filed[0]), drop_packets=proc_hex2int(filed[1]),
        net_budget=proc_hex2int(filed[2]), queue_locked=proc_hex2int(filed[9]), rps_pip=proc_hex2int(filed[10])))
        i += 1
        #print ("{line}".format(line))
    f_softnet_stat.close()

def print_netstat():
    print("============/proc/net/netstat=========")
    f_netstat = open("/proc/net/netstat", "r")
    parameter_parser(f_netstat) 
    f_netstat.close()

def print_tcp():
    f_tcp = open("/proc/net/tcp", "r")
    f_tcp.close

def print_packet():
    f_packet = open("/proc/net/packet", "r")
    f_packet.close

def print_snmp():
    print("============/proc/net/snmp=========")
    f_snmp = open("/proc/net/snmp", "r")
    parameter_parser(f_snmp)
    f_snmp.close

def print_dev():
    print("=============/proc/net/dev===========")
    f_dev = open("/proc/net/dev", "r")
    print(f_dev.readlines())
    f_dev.close

def main(argv):
    print_softnet_stat() 
    print_netstat()
    print_tcp()
    print_packet()
    print_snmp()
    print_dev()

if __name__ == "__main__":
    sys.exit(main(sys.argv))