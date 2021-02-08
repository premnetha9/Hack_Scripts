#!/usr/bin/python3

from netaddr import *

count = 0

with open("ipadder.txt") as file:
	for line in file:
		ip_address, ip_network = line.split(',')
		ip_network = ip_network.strip()
		if IPAddress(ip_address) in IPNetwork(ip_network):
			count += 1
print(count)
