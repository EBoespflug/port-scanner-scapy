#!/urs/bin/python
import argparse


banner = "Simple port scanner v1.0"

# This function uses argparse to parse command line
# arguments passed to the script.
def set_configs():
    arg_parser = argparse.ArgumentParser(description=banner)

    arg_parser.add_argument("dest_ip", help="Destination IP address.")
    arg_parser.add_argument("-p", "--dports", nargs='+', type=int, help="Destination port.")
    arg_parser.add_argument("-t", "--timeout", type=int, default=2, help="Timeout for each port scan. Default = 2.")
    arg_parser.add_argument("-v", "--verbose", type=bool, default=False,        help="Set the verbosity level to 'verbose'.")
    args = arg_parser.parse_args()

    return {
        'dest_ip'   : args.dest_ip,
        'dports'    : list(set(args.dports)),
        'verbose'   : args.verbose,
        'timeout'   : args.timeout
    }

def main():

    config = set_configs()

if __name__ == "__main__":
    main()
