

from ipaddress import IPv4Network

netmask = '255.255.255.0'
# netmask = '255.255.255.0'


print(IPv4Network(f"0.0.0.0/{netmask}").prefixlen)