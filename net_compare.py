#!/usr/bin/python -tt
# net_compare
# Claudia
# PyCharm
__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "11/20/16  6:28 AM"
__copyright__ = "Copyright (c) 2015 Claudia"
__license__ = "Python"

import sys
import csv
import argparse
import netaddr


def load_csv(filename,empty_row_key):

    csv_list = []

    try:

        with open(filename, 'rU') as csv_file:

            print("Loading CSV file " + filename + " as a List of Dictionaries")

            reader = csv.DictReader(csv_file)
            for dict_row in reader:

                if len(dict_row[empty_row_key]) == 0:
                    # Empty Row
                    pass
                else:
                    csv_list.append(dict_row)

    except IOError:
        # Problem opening the file
        print "There was a problem opening the file " + filename + "!"
        sys.exit('Aborting program Execution')

    return csv_list

def load_cidr_lookup(filename):

    cidrdict = {}

    try:

        with open(filename, 'rU') as csv_file:

            print("Loading CSV file " + filename + " CIDR Mapping ")

            reader = csv.DictReader(csv_file)
            for dict_row in reader:

                if len(dict_row['cidr_length']) == 0:
                    # Empty Row
                    pass
                else:
                    # cidr_list.append(dict_row)
                    cidrdict[dict_row['mask']] = dict_row['cidr_length']


    except IOError:
        # Problem opening the file
        print "There was a problem opening the file " + filename + "!"
        sys.exit('Aborting program Execution')

    return cidrdict


def main():

    found_network_dict = {}

    # Open CSV File of Networks
    filename = arguments.net_csv_file
    net_list = load_csv(filename, 'net')
    print "Number of Networks Loaded: " + str(len(net_list))

    # Open CSV File of IPs
    filename = arguments.ip_csv_file
    ip_list = load_csv(filename, 'ip')
    print "Number of IPs Loaded: " + str(len(ip_list))

    # Open CIDR Notation/Maks Translation Table
    filename = 'cidr.csv'
    cidr_dict = load_cidr_lookup(filename)


    print '####### IP Lookup ########'
    for ips in ip_list:
        ip_is_in_net = False
        ipaddr = ips['ip']
        for nets in net_list:

            network = nets['net']
            netmask = nets['mask']
            netbits = cidr_dict[netmask]
            cidr_notation = network + "/" + netbits
            if netaddr.IPAddress(ipaddr) in netaddr.IPNetwork(cidr_notation):
                ip_is_in_net = True
                found_network_dict[ipaddr] = cidr_notation
                pass

        if ip_is_in_net:
            print "++IP Address {} is in Network {}".format(ipaddr, found_network_dict[ipaddr])
        else:
            print "--IP Address {} is  NOT FOUND in ANY NETWORK!!!".format(ipaddr)

# Standard call to the main() function.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Load CSV Data and Compare IPs to Networks", epilog='Usage: python net_compare.py "qip-net-all.csv" "qip-bulk-all.csv"')
    parser.add_argument('net_csv_file', help='Name of the csv with the network information.')
    parser.add_argument('ip_csv_file', help='Name of the csv with the bulk ip information.')

    arguments = parser.parse_args()

    main()
