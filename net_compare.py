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
import time


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
    mia_report = []

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

    # Create a Log file
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    filename_base = "net_compare_run"
    timestr = time.strftime("%Y%m%d-%H%M%S")
    log_filename = filename_base + "-" + timestr + ".log"
    log_file = open(log_filename, 'w')

    log_file.write("Timestamp: " + str(start_time) + "\n")
    log_file.write("\nProcessing Network CSV file: " + arguments.net_csv_file + "\n")
    log_file.write("Number of Networks Loaded: " + str(len(net_list)) + "\n\n")
    log_file.write("Processing IP Address CSV file: " + arguments.ip_csv_file + "\n")
    log_file.write("Number of IP Addresses Loaded: " + str(len(ip_list)) + "\n\n")

    # Lookup up each IP in the IP list and see if there is a match in the subnet list
    print '####### IP Lookup for Matching Subnet ########'
    log_file.write('\n####### IP Lookup for Matching Subnet ########\n')
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
            msg = "++IP Address " + ipaddr + " is in Network " + found_network_dict[ipaddr]
            print msg
            log_file.write(msg + "\n")
        else:
            msg = "ERROR: No Network: --IP Address " + ipaddr + " is  NOT FOUND in ANY NETWORK!!!"
            print msg
            log_file.write(msg + "\n")
            mia_report.append(msg)


    # Lookup each subnet and see if there is at least one object
    print '\n\n####### At least one Object per Subnet ########'
    log_file.write('\n\n####### At least one Object per Subnet ########\n')
    foundobj_innet = {}
    for nets in net_list:
        list_of_ips = []
        obj_in_net = False
        network = nets['net']
        netmask = nets['mask']
        netbits = cidr_dict[netmask]
        cidr_notation = network + "/" + netbits

        for ips in ip_list:

            ipaddr = ips['ip']

            if netaddr.IPAddress(ipaddr) in netaddr.IPNetwork(cidr_notation):
                obj_in_net = True
                list_of_ips.append(ipaddr)
                foundobj_innet[cidr_notation] = list_of_ips

        if not obj_in_net:
            foundobj_innet[cidr_notation] = []


    for k,v in foundobj_innet.items():
        if len(v) > 0:
            msg = "Network " + k + " has " + str(len(v)) + " IP Address objects"
            print msg
            log_file.write(msg + "\n")
        else:
            msg = "ERROR: No Objects: Network " + k + " has **NO** (" + str(len(v)) + ") IP Address objects!"
            print msg
            log_file.write(msg + "\n")
            mia_report.append(msg)

    print "\n\n############### ERROR Report Summary ###############"
    log_file.write("\n\n############### ERROR Report Summary ###############\n")
    for line in mia_report:
        print line
        log_file.write(line + "\n")

    total_errors = "\nTotal Number of Errors: " + str(len(mia_report))
    print total_errors
    log_file.write(total_errors + "\n")

    log_file.close()

# Standard call to the main() function.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Load CSV Data and Compare IPs to Networks", epilog='Usage: python net_compare.py "qip-net-all.csv" "qip-bulk-all.csv"')
    parser.add_argument('net_csv_file', help='Name of the csv with the network information.')
    parser.add_argument('ip_csv_file', help='Name of the csv with the bulk ip information.')

    arguments = parser.parse_args()

    main()
