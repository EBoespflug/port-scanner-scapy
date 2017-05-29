# Etienne BOESPFLUG - 2017
#
# scan.py - https://github.com/EBoespflug/port-scanner-scapy
#
# This project is part of the public domain.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE.

from scapy.all import *
import ScanResult

def TCP_SYN_scan(**args):
    """Performs a TCP SYN scan for the specified destination port ('dport') and destination ip ('dest_ip'). The source port is random."""
    dport = args['dport']
    sport = RandShort()
    dest_ip = args['dest_ip']
    timeout = args['timeout']
    if 'sport' in args:
        sport = args['sport']
    # Send Syn Scan.
    ss_res = sr1( IP(dst=dest_ip) /TCP(sport=sport,dport=dport,flags="S"),timeout=timeout)
    # Handle response.
    if(str(type(ss_res))=="<type 'NoneType'>"):
        return ScanResult.Filtered
    elif(ss_res.haslayer(TCP)):
        if(ss_res.getlayer(TCP).flags == 0x12):
            # Send RST.
            i = send(IP(dst=dest_ip)/TCP(sport=sport,dport=dport,flags="R"))
            return ScanResult.Open
        elif (ss_res.getlayer(TCP).flags == 0x14):
            return ScanResult.Closed
    # Control ICMP response.
    elif(ss_res.haslayer(ICMP)):
        if(int(ss_res.getlayer(ICMP).type)==3 and int(ss_res.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            return ScanResult.Filtered
    return ScanResult.Unknown

def launch_scans(config):
    """Launch a TCP SYN scan for each destination port ('dport') with the passed options."""
    port_results = []
    for port in config['dports']:
        port_results.append(TCP_SYN_scan(dport=port, dest_ip=config['dest_ip'], timeout=config['timeout']))

    return port_results

def print_results(config, port_results):
    '''Print the scan result.'''
    for i in range(len(port_results)):
        report_str = "port " + str(config['dports'][i])
        report_str += " : [" + ScanResult.get_result_str(port_results[i]) + "]."
        print report_str
    print "Scan done."
