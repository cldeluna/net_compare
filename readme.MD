# net_compare

##Synopsis
Network utility script to compare a list of IP addresses to a list of networks and determine matches and misses.


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
- a "mast" column that holds the network mask in dotted notation
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

This script requires the following modules:
- sys
- csv
- argparse
- netaddr


##Output

Currently the script outputs to stdout (the screen normally).
++ lines indicate a match between IP and Network list
-- lines indicate an IP address without a matching Network

	Loading CSV file qip-net-all.csv as a List of Dictionaries
	Number of Networks Loaded: 92
	Loading CSV file qip-bulk-all.csv as a List of Dictionaries
	Number of IPs Loaded: 301
	Loading CSV file cidr.csv CIDR Mapping 
	####### IP Lookup ########
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
	--IP Address 202.191.223.123 is  NOT FOUND in ANY NETWORK!!!
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
	--IP Address 4.4.4.1 is  NOT FOUND in ANY NETWORK!!!
	++IP Address 10.72.253.28 is in Network 10.72.253.24/29
	++IP Address 172.22.128.252 is in Network 172.22.128.0/24




