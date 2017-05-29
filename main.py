# Etienne BOESPFLUG - 2017
#
# main.py - https://github.com/EBoespflug/port-scanner-scapy
#
# This project is part of the public domain.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE.

import argparse
from scan import launch_scans, print_results
from scapy.all import *

banner = "Simple port scanner v1.0"

def set_configs():
    """This function uses argparse to parse command line arguments passed to the script."""
    arg_parser = argparse.ArgumentParser(description=banner)

    arg_parser.add_argument("dest_ip", help="Destination IP address.")
    arg_parser.add_argument("-p", "--dports", nargs='+', type=int, help="Destination port.")
    arg_parser.add_argument("-t", "--timeout", type=int, default=2, help="Timeout for each port scan. Default = 2.")
    arg_parser.add_argument("-v", "--verbose", action='store_true', help="Set the verbosity level to 'verbose'.")
    args = arg_parser.parse_args()

    dports = []
    if args.dports:
        dports += list(set(args.dports))

    if len(dports) == 0:
        print "error : no destination port to scan."
        return None

    timeout = 2
    if args.timeout:
        timeout = timeout

    return {
        'dest_ip'   : args.dest_ip,
        'dports'    : dports,
        'verbose'   : args.verbose,
        'timeout'   : timeout
    }

def main():
    config = set_configs()

    if config is None :
        return
    if not config['verbose']:
        conf.verb = 0

    print_results(config, launch_scans(config))

if __name__ == "__main__":
    main()
