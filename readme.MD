# net_compare

##Synopsis
Network utility script to 
- compare a list of IP addresses to a list of networks and determine matches and misses
- compare a list of networks to a list of IP addresses and determine matches and misses

The script will log to stdout as well as to a time stamped file.  The log contains a line for each comparison and will conclude with an "Error Report Summary" listing IPs without subnets and subnets without IP objects.

	>python net_compare.py -h
	usage: net_compare.py [-h] net_csv_file ip_csv_file

	Load CSV Data and Compare IPs to Networks

	positional arguments:
	  net_csv_file  Name of the csv with the network information.
	  ip_csv_file   Name of the csv with the bulk ip information.

	optional arguments:
	  -h, --help    show this help message and exit

	Usage: python net_compare.py "qip-net-all.csv" "qip-bulk-all.csv"



##CSV File Structure Requirements

###net_csv_file requires:
- a header row
- a "net" column that holds the network id
- a "mask" column that holds the network mask in dotted notation

all other columns are optional

blank lines (emtpy net field) are ignored


	
	net	mask	network	name	site_code	use_typ	logical_data	-	VL	vlan	region
	10.72.253.16	255.255.255.248	10.0.0.0	AUP-SLAN-Firewall_HSRP_VIP-VL21	AUP	SLAN	Firewall_HSRP_VIP	-	VL	21	APAC
	10.72.254.0	255.255.255.192	10.0.0.0	AUP-SLAN-Mgmt_VLAN-VL99	AUP	SLAN	Mgmt_VLAN	-	VL	99	APAC
	10.72.128.0	255.255.255.0	10.0.0.0	AUP-SLAN-HS_WL_User_VDC_1-VL1128	AUP	SLAN	HS_WL_User_VDC_1	-	VL	1128	APAC
	10.72.129.0	255.255.255.0	10.0.0.0	AUP-SLAN-HS_WL_User2_VDC_1-VL1129	AUP	SLAN	HS_WL_User2_VDC_1	-	VL	1129	APAC
	10.72.130.0	255.255.255.0	10.0.0.0	AUP-SLAN-HS_WL_Guest_VDC_1-VL1130	AUP	SLAN	HS_WL_Guest_VDC_1	-	VL	1130	APAC
								-	VL		
	10.72.253.8	255.255.255.252	10.0.0.0	AUP-SLAN-Connected_To_VPN_Router_Gi0_2-VL0	AUP	SLAN	Connected_To_VPN_Router_Gi0_2	-	VL	0	APAC


###ip_csv_file requires:
- a header row
- an "ip" column that holds the ip address

all other columns are optional

blank lines (emtpy ip field) are ignored


	
	ip
	10.72.253.19
	10.72.254.2
	10.72.128.251
	10.72.129.251

	10.72.130.251



##Installation

This script requires python 2.7 the following modules:
- sys
- csv
- argparse
- netaddr
- time


##Output

The script will log to stdout as well as to a time stamped file named "net_compare_run-<timestamp>.log" in the local directory.  The log contains a line for each comparison and will conclude with an "Error Report Summary" listing IPs without subnets and subnets without IP objects.


	Timestamp: 2016-11-22 04:07:22

	Processing Network CSV file: qip-net-all.csv
	Processing IP Address CSV file: qip-bulk-all.csv

	####### IP Lookup for Matching Subnet ########
	++IP Address 10.72.253.19 is in Network 10.72.253.16/29
	++IP Address 10.72.254.2 is in Network 10.72.254.0/26
	++IP Address 10.72.128.251 is in Network 10.72.128.0/24
	++IP Address 10.72.129.251 is in Network 10.72.129.0/24
	++IP Address 10.72.130.251 is in Network 10.72.130.0/24
	++IP Address 10.72.255.254 is in Network 10.72.255.0/24
	++IP Address 10.72.253.10 is in Network 10.72.253.8/30
	++IP Address 10.72.253.49 is in Network 10.72.253.48/30
	++IP Address 10.72.253.33 is in Network 10.72.253.32/30
	++IP Address 10.72.253.66 is in Network 10.72.253.64/30
	++IP Address 10.72.253.2 is in Network 10.72.253.0/30
	++IP Address 10.72.253.53 is in Network 10.72.253.52/30
	++IP Address 10.72.253.37 is in Network 10.72.253.36/30
	++IP Address 10.72.253.74 is in Network 10.72.253.72/30
	++IP Address 10.72.253.20 is in Network 10.72.253.16/29
	++IP Address 10.72.254.3 is in Network 10.72.254.0/26
	++IP Address 10.72.128.252 is in Network 10.72.128.0/24
	++IP Address 10.72.129.252 is in Network 10.72.129.0/24
	++IP Address 10.72.130.252 is in Network 10.72.130.0/24
	++IP Address 10.72.255.253 is in Network 10.72.255.0/24
	++IP Address 10.72.253.14 is in Network 10.72.253.12/30
	++IP Address 10.72.253.57 is in Network 10.72.253.56/30
	++IP Address 10.72.253.45 is in Network 10.72.253.44/30
	++IP Address 10.72.253.70 is in Network 10.72.253.68/30
	++IP Address 10.72.253.6 is in Network 10.72.253.4/30
	++IP Address 10.72.253.62 is in Network 10.72.253.60/30
	++IP Address 10.72.253.41 is in Network 10.72.253.40/30
	++IP Address 10.72.253.78 is in Network 10.72.253.76/30
	ERROR: No Network: --IP Address 202.191.223.123 is  NOT FOUND in ANY NETWORK!!!
	++IP Address 10.72.253.13 is in Network 10.72.253.12/30
	++IP Address 10.72.253.9 is in Network 10.72.253.8/30
	++IP Address 10.72.255.250 is in Network 10.72.255.0/24
	++IP Address 10.26.50.202 is in Network 10.26.50.200/30
	++IP Address 10.72.253.27 is in Network 10.72.253.24/29
	++IP Address 172.22.128.251 is in Network 172.22.128.0/24
	++IP Address 172.22.129.251 is in Network 172.22.129.0/24
	++IP Address 172.22.130.251 is in Network 172.22.130.0/24
	++IP Address 172.22.131.251 is in Network 172.22.131.0/24
	++IP Address 172.22.132.251 is in Network 172.22.132.0/24
	++IP Address 172.22.133.251 is in Network 172.22.133.0/24
	++IP Address 172.22.134.251 is in Network 172.22.134.0/24
	++IP Address 10.72.255.252 is in Network 10.72.255.0/24
	ERROR: No Network: --IP Address 4.4.4.1 is  NOT FOUND in ANY NETWORK!!!
	++IP Address 10.72.253.28 is in Network 10.72.253.24/29
	++IP Address 172.22.128.252 is in Network 172.22.128.0/24
	++IP Address 172.22.129.252 is in Network 172.22.129.0/24
	++IP Address 172.22.130.252 is in Network 172.22.130.0/24
	++IP Address 172.22.131.252 is in Network 172.22.131.0/24
	++IP Address 172.22.132.252 is in Network 172.22.132.0/24
	++IP Address 172.22.133.252 is in Network 172.22.133.0/24
	++IP Address 172.22.134.252 is in Network 172.22.134.0/24
	++IP Address 10.72.255.251 is in Network 10.72.255.0/24
	ERROR: No Network: --IP Address 4.4.4.2 is  NOT FOUND in ANY NETWORK!!!
	++IP Address 10.72.254.101 is in Network 10.72.254.64/26
	++IP Address 10.72.0.251 is in Network 10.72.0.0/24
	++IP Address 10.72.1.251 is in Network 10.72.1.0/24
	++IP Address 10.72.2.251 is in Network 10.72.2.0/24
	++IP Address 10.72.3.251 is in Network 10.72.3.0/24
	++IP Address 10.72.4.251 is in Network 10.72.4.0/24
	++IP Address 10.72.5.251 is in Network 10.72.5.0/24
	++IP Address 10.72.6.251 is in Network 10.72.6.0/24
	++IP Address 10.72.7.251 is in Network 10.72.7.0/24
	++IP Address 10.72.8.251 is in Network 10.72.8.0/24
	++IP Address 10.72.9.251 is in Network 10.72.9.0/24
	++IP Address 10.72.10.251 is in Network 10.72.10.0/24
	++IP Address 10.72.11.251 is in Network 10.72.11.0/24
	++IP Address 10.72.56.251 is in Network 10.72.56.0/24
	++IP Address 10.72.64.251 is in Network 10.72.64.0/24
	++IP Address 10.72.65.251 is in Network 10.72.65.0/24
	++IP Address 10.72.66.251 is in Network 10.72.66.0/24
	++IP Address 10.72.67.251 is in Network 10.72.67.0/24
	++IP Address 10.72.68.251 is in Network 10.72.68.0/24
	++IP Address 10.72.69.251 is in Network 10.72.69.0/24
	++IP Address 10.72.70.251 is in Network 10.72.70.0/24
	++IP Address 10.72.71.251 is in Network 10.72.71.0/24
	++IP Address 10.72.72.251 is in Network 10.72.72.0/24
	++IP Address 10.72.73.251 is in Network 10.72.73.0/24
	++IP Address 10.72.74.251 is in Network 10.72.74.0/24
	++IP Address 10.72.75.251 is in Network 10.72.75.0/24
	++IP Address 10.72.76.251 is in Network 10.72.76.0/24
	++IP Address 10.72.77.251 is in Network 10.72.77.0/24
	++IP Address 10.72.96.251 is in Network 10.72.96.0/24
	++IP Address 10.72.97.251 is in Network 10.72.97.0/24
	++IP Address 10.72.98.251 is in Network 10.72.98.0/24
	++IP Address 10.72.99.251 is in Network 10.72.99.0/24
	++IP Address 10.72.100.251 is in Network 10.72.100.0/24
	++IP Address 10.72.101.251 is in Network 10.72.101.0/24
	++IP Address 10.72.102.251 is in Network 10.72.102.0/24
	++IP Address 10.72.103.251 is in Network 10.72.103.0/24
	++IP Address 10.72.104.251 is in Network 10.72.104.0/24
	++IP Address 10.72.105.251 is in Network 10.72.105.0/24
	++IP Address 10.72.106.251 is in Network 10.72.106.0/24
	++IP Address 10.72.107.251 is in Network 10.72.107.0/24
	++IP Address 10.72.108.251 is in Network 10.72.108.0/24
	++IP Address 10.72.109.251 is in Network 10.72.109.0/24
	++IP Address 10.72.144.251 is in Network 10.72.144.0/24
	++IP Address 10.72.145.251 is in Network 10.72.145.0/24
	++IP Address 10.72.146.251 is in Network 10.72.146.0/24
	++IP Address 10.72.147.251 is in Network 10.72.147.0/24
	++IP Address 10.72.148.251 is in Network 10.72.148.0/24
	++IP Address 10.72.149.251 is in Network 10.72.149.0/24
	++IP Address 10.72.150.251 is in Network 10.72.150.0/24
	++IP Address 10.72.151.251 is in Network 10.72.151.0/24
	++IP Address 10.72.152.251 is in Network 10.72.152.0/24
	++IP Address 10.72.153.251 is in Network 10.72.153.0/24
	++IP Address 10.72.154.251 is in Network 10.72.154.0/24
	++IP Address 10.72.155.251 is in Network 10.72.155.0/24
	++IP Address 172.22.134.253 is in Network 172.22.134.0/24
	++IP Address 10.72.255.248 is in Network 10.72.255.0/24
	ERROR: No Network: --IP Address 3.3.3.1 is  NOT FOUND in ANY NETWORK!!!
	++IP Address 10.72.253.34 is in Network 10.72.253.32/30
	++IP Address 10.72.253.42 is in Network 10.72.253.40/30
	++IP Address 10.72.254.102 is in Network 10.72.254.64/26
	++IP Address 10.72.0.252 is in Network 10.72.0.0/24
	++IP Address 10.72.1.252 is in Network 10.72.1.0/24
	++IP Address 10.72.2.252 is in Network 10.72.2.0/24
	++IP Address 10.72.3.252 is in Network 10.72.3.0/24
	++IP Address 10.72.4.252 is in Network 10.72.4.0/24
	++IP Address 10.72.5.252 is in Network 10.72.5.0/24
	++IP Address 10.72.6.252 is in Network 10.72.6.0/24
	++IP Address 10.72.7.252 is in Network 10.72.7.0/24
	++IP Address 10.72.8.252 is in Network 10.72.8.0/24
	++IP Address 10.72.9.252 is in Network 10.72.9.0/24
	++IP Address 10.72.10.252 is in Network 10.72.10.0/24
	++IP Address 10.72.11.252 is in Network 10.72.11.0/24
	++IP Address 10.72.56.252 is in Network 10.72.56.0/24
	++IP Address 10.72.64.252 is in Network 10.72.64.0/24
	++IP Address 10.72.65.252 is in Network 10.72.65.0/24
	++IP Address 10.72.66.252 is in Network 10.72.66.0/24
	++IP Address 10.72.67.252 is in Network 10.72.67.0/24
	++IP Address 10.72.68.252 is in Network 10.72.68.0/24
	++IP Address 10.72.69.252 is in Network 10.72.69.0/24
	++IP Address 10.72.70.252 is in Network 10.72.70.0/24
	++IP Address 10.72.71.252 is in Network 10.72.71.0/24
	++IP Address 10.72.72.252 is in Network 10.72.72.0/24
	++IP Address 10.72.73.252 is in Network 10.72.73.0/24
	++IP Address 10.72.74.252 is in Network 10.72.74.0/24
	++IP Address 10.72.75.252 is in Network 10.72.75.0/24
	++IP Address 10.72.76.252 is in Network 10.72.76.0/24
	++IP Address 10.72.77.252 is in Network 10.72.77.0/24
	++IP Address 10.72.96.252 is in Network 10.72.96.0/24
	++IP Address 10.72.97.252 is in Network 10.72.97.0/24
	++IP Address 10.72.98.252 is in Network 10.72.98.0/24
	++IP Address 10.72.99.252 is in Network 10.72.99.0/24
	++IP Address 10.72.100.252 is in Network 10.72.100.0/24
	++IP Address 10.72.101.252 is in Network 10.72.101.0/24
	++IP Address 10.72.102.252 is in Network 10.72.102.0/24
	++IP Address 10.72.103.252 is in Network 10.72.103.0/24
	++IP Address 10.72.104.252 is in Network 10.72.104.0/24
	++IP Address 10.72.105.252 is in Network 10.72.105.0/24
	++IP Address 10.72.106.252 is in Network 10.72.106.0/24
	++IP Address 10.72.107.252 is in Network 10.72.107.0/24
	++IP Address 10.72.108.252 is in Network 10.72.108.0/24
	++IP Address 10.72.109.252 is in Network 10.72.109.0/24
	++IP Address 10.72.144.252 is in Network 10.72.144.0/24
	++IP Address 10.72.145.252 is in Network 10.72.145.0/24
	++IP Address 10.72.146.252 is in Network 10.72.146.0/24
	++IP Address 10.72.147.252 is in Network 10.72.147.0/24
	++IP Address 10.72.148.252 is in Network 10.72.148.0/24
	++IP Address 10.72.149.252 is in Network 10.72.149.0/24
	++IP Address 10.72.150.252 is in Network 10.72.150.0/24
	++IP Address 10.72.151.252 is in Network 10.72.151.0/24
	++IP Address 10.72.152.252 is in Network 10.72.152.0/24
	++IP Address 10.72.153.252 is in Network 10.72.153.0/24
	++IP Address 10.72.154.252 is in Network 10.72.154.0/24
	++IP Address 10.72.155.252 is in Network 10.72.155.0/24
	++IP Address 172.22.134.254 is in Network 172.22.134.0/24
	++IP Address 10.72.255.247 is in Network 10.72.255.0/24
	ERROR: No Network: --IP Address 3.3.3.2 is  NOT FOUND in ANY NETWORK!!!
	++IP Address 10.72.253.46 is in Network 10.72.253.44/30
	++IP Address 10.72.253.38 is in Network 10.72.253.36/30
	++IP Address 10.72.254.77 is in Network 10.72.254.64/26
	++IP Address 10.72.254.78 is in Network 10.72.254.64/26
	++IP Address 10.72.254.81 is in Network 10.72.254.64/26
	++IP Address 10.72.254.80 is in Network 10.72.254.64/26
	++IP Address 10.72.254.76 is in Network 10.72.254.64/26
	++IP Address 10.72.254.84 is in Network 10.72.254.64/26
	++IP Address 10.72.254.68 is in Network 10.72.254.64/26
	++IP Address 10.72.254.82 is in Network 10.72.254.64/26
	++IP Address 10.72.254.66 is in Network 10.72.254.64/26
	++IP Address 10.72.254.65 is in Network 10.72.254.64/26
	++IP Address 10.72.254.75 is in Network 10.72.254.64/26
	++IP Address 10.72.254.74 is in Network 10.72.254.64/26
	++IP Address 10.72.254.73 is in Network 10.72.254.64/26
	++IP Address 10.72.254.90 is in Network 10.72.254.64/26
	++IP Address 10.72.254.71 is in Network 10.72.254.64/26
	++IP Address 10.72.254.87 is in Network 10.72.254.64/26
	++IP Address 10.72.254.72 is in Network 10.72.254.64/26
	++IP Address 10.72.254.83 is in Network 10.72.254.64/26
	++IP Address 10.72.254.86 is in Network 10.72.254.64/26
	++IP Address 10.72.254.70 is in Network 10.72.254.64/26
	++IP Address 10.72.254.89 is in Network 10.72.254.64/26
	++IP Address 10.72.254.67 is in Network 10.72.254.64/26
	++IP Address 10.72.254.69 is in Network 10.72.254.64/26
	++IP Address 10.72.254.85 is in Network 10.72.254.64/26
	++IP Address 10.72.48.251 is in Network 10.72.48.0/24
	++IP Address 10.72.49.251 is in Network 10.72.49.0/24
	++IP Address 10.72.50.251 is in Network 10.72.50.0/24
	++IP Address 10.72.51.251 is in Network 10.72.51.0/24
	++IP Address 10.72.255.246 is in Network 10.72.255.0/24
	++IP Address 10.72.253.50 is in Network 10.72.253.48/30
	++IP Address 10.72.253.61 is in Network 10.72.253.60/30
	++IP Address 10.72.48.252 is in Network 10.72.48.0/24
	++IP Address 10.72.49.252 is in Network 10.72.49.0/24
	++IP Address 10.72.50.252 is in Network 10.72.50.0/24
	++IP Address 10.72.51.252 is in Network 10.72.51.0/24
	++IP Address 10.72.255.245 is in Network 10.72.255.0/24
	++IP Address 10.72.253.58 is in Network 10.72.253.56/30
	++IP Address 10.72.253.54 is in Network 10.72.253.52/30
	++IP Address 10.72.254.1 is in Network 10.72.254.0/26
	++IP Address 10.72.128.250 is in Network 10.72.128.0/24
	++IP Address 10.72.129.250 is in Network 10.72.129.0/24
	++IP Address 10.72.130.250 is in Network 10.72.130.0/24
	++IP Address 10.72.253.29 is in Network 10.72.253.24/29
	++IP Address 172.22.128.250 is in Network 172.22.128.0/24
	++IP Address 172.22.129.250 is in Network 172.22.129.0/24
	++IP Address 172.22.130.250 is in Network 172.22.130.0/24
	++IP Address 172.22.131.250 is in Network 172.22.131.0/24
	++IP Address 172.22.132.250 is in Network 172.22.132.0/24
	++IP Address 172.22.133.250 is in Network 172.22.133.0/24
	++IP Address 172.22.134.250 is in Network 172.22.134.0/24
	++IP Address 10.72.254.100 is in Network 10.72.254.64/26
	++IP Address 10.72.0.250 is in Network 10.72.0.0/24
	++IP Address 10.72.1.250 is in Network 10.72.1.0/24
	++IP Address 10.72.2.250 is in Network 10.72.2.0/24
	++IP Address 10.72.3.250 is in Network 10.72.3.0/24
	++IP Address 10.72.4.250 is in Network 10.72.4.0/24
	++IP Address 10.72.5.250 is in Network 10.72.5.0/24
	++IP Address 10.72.6.250 is in Network 10.72.6.0/24
	++IP Address 10.72.7.250 is in Network 10.72.7.0/24
	++IP Address 10.72.8.250 is in Network 10.72.8.0/24
	++IP Address 10.72.9.250 is in Network 10.72.9.0/24
	++IP Address 10.72.10.250 is in Network 10.72.10.0/24
	++IP Address 10.72.11.250 is in Network 10.72.11.0/24
	++IP Address 10.72.56.250 is in Network 10.72.56.0/24
	++IP Address 10.72.64.250 is in Network 10.72.64.0/24
	++IP Address 10.72.65.250 is in Network 10.72.65.0/24
	++IP Address 10.72.66.250 is in Network 10.72.66.0/24
	++IP Address 10.72.67.250 is in Network 10.72.67.0/24
	++IP Address 10.72.68.250 is in Network 10.72.68.0/24
	++IP Address 10.72.69.250 is in Network 10.72.69.0/24
	++IP Address 10.72.70.250 is in Network 10.72.70.0/24
	++IP Address 10.72.71.250 is in Network 10.72.71.0/24
	++IP Address 10.72.72.250 is in Network 10.72.72.0/24
	++IP Address 10.72.73.250 is in Network 10.72.73.0/24
	++IP Address 10.72.74.250 is in Network 10.72.74.0/24
	++IP Address 10.72.75.250 is in Network 10.72.75.0/24
	++IP Address 10.72.76.250 is in Network 10.72.76.0/24
	++IP Address 10.72.77.250 is in Network 10.72.77.0/24
	++IP Address 10.72.96.250 is in Network 10.72.96.0/24
	++IP Address 10.72.97.250 is in Network 10.72.97.0/24
	++IP Address 10.72.98.250 is in Network 10.72.98.0/24
	++IP Address 10.72.99.250 is in Network 10.72.99.0/24
	++IP Address 10.72.100.250 is in Network 10.72.100.0/24
	++IP Address 10.72.101.250 is in Network 10.72.101.0/24
	++IP Address 10.72.102.250 is in Network 10.72.102.0/24
	++IP Address 10.72.103.250 is in Network 10.72.103.0/24
	++IP Address 10.72.104.250 is in Network 10.72.104.0/24
	++IP Address 10.72.105.250 is in Network 10.72.105.0/24
	++IP Address 10.72.106.250 is in Network 10.72.106.0/24
	++IP Address 10.72.107.250 is in Network 10.72.107.0/24
	++IP Address 10.72.108.250 is in Network 10.72.108.0/24
	++IP Address 10.72.109.250 is in Network 10.72.109.0/24
	++IP Address 10.72.144.250 is in Network 10.72.144.0/24
	++IP Address 10.72.145.250 is in Network 10.72.145.0/24
	++IP Address 10.72.146.250 is in Network 10.72.146.0/24
	++IP Address 10.72.147.250 is in Network 10.72.147.0/24
	++IP Address 10.72.148.250 is in Network 10.72.148.0/24
	++IP Address 10.72.149.250 is in Network 10.72.149.0/24
	++IP Address 10.72.150.250 is in Network 10.72.150.0/24
	++IP Address 10.72.151.250 is in Network 10.72.151.0/24
	++IP Address 10.72.152.250 is in Network 10.72.152.0/24
	++IP Address 10.72.153.250 is in Network 10.72.153.0/24
	++IP Address 10.72.154.250 is in Network 10.72.154.0/24
	++IP Address 10.72.155.250 is in Network 10.72.155.0/24
	++IP Address 10.72.48.250 is in Network 10.72.48.0/24
	++IP Address 10.72.49.250 is in Network 10.72.49.0/24
	++IP Address 10.72.50.250 is in Network 10.72.50.0/24
	++IP Address 10.72.51.250 is in Network 10.72.51.0/24
	++IP Address 10.72.156.1 is in Network 10.72.156.0/24
	++IP Address 10.72.156.2 is in Network 10.72.156.0/24
	++IP Address 10.72.156.3 is in Network 10.72.156.0/24
	++IP Address 10.11.27.1 is in Network 10.11.27.0/24
	++IP Address 10.11.27.2 is in Network 10.11.27.0/24
	++IP Address 10.11.27.3 is in Network 10.11.27.0/24
	++IP Address 10.72.253.1 is in Network 10.72.253.0/30
	++IP Address 10.72.253.5 is in Network 10.72.253.4/30
	ERROR: No Network: --IP Address 172.23.37.127 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 0 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 0 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 0 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 202.191.223.130 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 202.191.223.121 is  NOT FOUND in ANY NETWORK!!!
	++IP Address 10.72.254.18 is in Network 10.72.254.0/26
	++IP Address 10.72.78.1 is in Network 10.72.78.0/24
	++IP Address 10.72.78.2 is in Network 10.72.78.0/24
	++IP Address 10.72.78.3 is in Network 10.72.78.0/24
	++IP Address 10.72.254.91 is in Network 10.72.254.64/26
	++IP Address 10.72.254.92 is in Network 10.72.254.64/26
	++IP Address 10.72.254.9 is in Network 10.72.254.0/26
	++IP Address 10.72.254.10 is in Network 10.72.254.0/26


	####### At least one Object per Subnet ########
	Network 172.22.133.0/24 has 3 IP Address objects
	Network 10.72.253.72/30 has 1 IP Address objects
	Network 172.22.134.0/24 has 5 IP Address objects
	Network 10.72.75.0/24 has 3 IP Address objects
	Network 10.72.65.0/24 has 3 IP Address objects
	ERROR: No Objects: Network 99.99.99.0/24 has **NO** (0) IP Address objects!
	Network 10.72.3.0/24 has 3 IP Address objects
	Network 172.22.129.0/24 has 3 IP Address objects
	Network 10.72.99.0/24 has 3 IP Address objects
	Network 10.72.146.0/24 has 3 IP Address objects
	Network 10.72.156.0/24 has 3 IP Address objects
	Network 10.26.50.200/30 has 1 IP Address objects
	Network 10.72.253.76/30 has 1 IP Address objects
	Network 10.72.152.0/24 has 3 IP Address objects
	Network 10.72.128.0/24 has 3 IP Address objects
	Network 10.72.5.0/24 has 3 IP Address objects
	Network 10.72.106.0/24 has 3 IP Address objects
	Network 10.72.253.32/30 has 2 IP Address objects
	Network 10.72.150.0/24 has 3 IP Address objects
	Network 10.72.9.0/24 has 3 IP Address objects
	Network 10.72.67.0/24 has 3 IP Address objects
	Network 10.72.253.44/30 has 2 IP Address objects
	Network 10.72.64.0/24 has 3 IP Address objects
	Network 10.72.148.0/24 has 3 IP Address objects
	Network 10.72.253.8/30 has 2 IP Address objects
	Network 10.72.144.0/24 has 3 IP Address objects
	Network 10.72.153.0/24 has 3 IP Address objects
	Network 10.72.147.0/24 has 3 IP Address objects
	Network 10.72.253.48/30 has 2 IP Address objects
	Network 10.72.48.0/24 has 3 IP Address objects
	Network 10.72.104.0/24 has 3 IP Address objects
	Network 10.72.253.40/30 has 2 IP Address objects
	Network 10.72.8.0/24 has 3 IP Address objects
	Network 10.72.254.0/26 has 6 IP Address objects
	Network 10.72.76.0/24 has 3 IP Address objects
	Network 10.72.73.0/24 has 3 IP Address objects
	Network 172.22.132.0/24 has 3 IP Address objects
	Network 10.11.27.0/24 has 3 IP Address objects
	Network 10.72.107.0/24 has 3 IP Address objects
	Network 10.72.255.0/24 has 9 IP Address objects
	Network 10.72.2.0/24 has 3 IP Address objects
	Network 10.72.105.0/24 has 3 IP Address objects
	Network 10.72.145.0/24 has 3 IP Address objects
	Network 10.72.4.0/24 has 3 IP Address objects
	Network 10.72.70.0/24 has 3 IP Address objects
	Network 172.22.130.0/24 has 3 IP Address objects
	Network 10.72.10.0/24 has 3 IP Address objects
	Network 10.72.253.64/30 has 1 IP Address objects
	Network 10.72.129.0/24 has 3 IP Address objects
	Network 10.72.253.60/30 has 2 IP Address objects
	Network 10.72.1.0/24 has 3 IP Address objects
	Network 10.72.72.0/24 has 3 IP Address objects
	Network 10.72.49.0/24 has 3 IP Address objects
	Network 10.72.253.24/29 has 3 IP Address objects
	Network 10.72.68.0/24 has 3 IP Address objects
	Network 10.72.11.0/24 has 3 IP Address objects
	Network 10.72.96.0/24 has 3 IP Address objects
	Network 10.72.74.0/24 has 3 IP Address objects
	Network 10.72.77.0/24 has 3 IP Address objects
	Network 10.72.66.0/24 has 3 IP Address objects
	Network 10.72.78.0/24 has 3 IP Address objects
	Network 10.72.6.0/24 has 3 IP Address objects
	Network 10.72.103.0/24 has 3 IP Address objects
	Network 172.22.131.0/24 has 3 IP Address objects
	Network 10.72.253.4/30 has 2 IP Address objects
	Network 10.72.97.0/24 has 3 IP Address objects
	Network 10.72.155.0/24 has 3 IP Address objects
	Network 10.72.253.68/30 has 1 IP Address objects
	Network 10.72.51.0/24 has 3 IP Address objects
	Network 10.72.253.36/30 has 2 IP Address objects
	Network 10.72.253.0/30 has 2 IP Address objects
	Network 10.72.108.0/24 has 3 IP Address objects
	Network 10.72.71.0/24 has 3 IP Address objects
	Network 10.72.69.0/24 has 3 IP Address objects
	Network 10.72.98.0/24 has 3 IP Address objects
	Network 10.72.253.16/29 has 2 IP Address objects
	Network 10.72.7.0/24 has 3 IP Address objects
	Network 10.72.50.0/24 has 3 IP Address objects
	Network 10.72.254.64/26 has 29 IP Address objects
	Network 10.72.253.12/30 has 2 IP Address objects
	Network 10.72.253.52/30 has 2 IP Address objects
	Network 10.72.151.0/24 has 3 IP Address objects
	Network 10.72.100.0/24 has 3 IP Address objects
	Network 10.72.253.56/30 has 2 IP Address objects
	Network 10.72.102.0/24 has 3 IP Address objects
	Network 10.72.101.0/24 has 3 IP Address objects
	Network 172.22.128.0/24 has 3 IP Address objects
	Network 10.72.0.0/24 has 3 IP Address objects
	Network 10.72.56.0/24 has 3 IP Address objects
	Network 10.72.154.0/24 has 3 IP Address objects
	Network 10.72.149.0/24 has 3 IP Address objects
	Network 10.72.109.0/24 has 3 IP Address objects
	Network 10.72.130.0/24 has 3 IP Address objects


	############### ERROR Report Summary ###############
	ERROR: No Network: --IP Address 202.191.223.123 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 4.4.4.1 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 4.4.4.2 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 3.3.3.1 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 3.3.3.2 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 172.23.37.127 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 0 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 0 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 0 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 202.191.223.130 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Network: --IP Address 202.191.223.121 is  NOT FOUND in ANY NETWORK!!!
	ERROR: No Objects: Network 99.99.99.0/24 has **NO** (0) IP Address objects!

