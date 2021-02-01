from lib.ip import *

ip = dhcpcdManager()

iface = "eth0"

test_set_ip = True
test_remove_static_info = False

set_ip = ip.set_static_info(iface, "192.168.15.7", "192.168.15.1", "8.8.8.8", "255.255.0.0")
print(set_ip)
# print(ip.set_static_info(iface, "192.168.15.6", "192.168.15.1", "8.8.8.8", "255.255.225.0"))

# if test_set_ip:
#     call_set_ip = set_ip
#     if call_set_ip[0] == 0:
#         print(call_set_ip)
#         print("SET INTERFACE IP")
#     elif call_set_ip[0] == -1:
#         print("SET INTERFACE IP FAIL")
#
# remove_static_info = ip.remove_static_info(iface)
#
# if test_remove_static_info:
#     if remove_static_info == 0:
#         print("SET INTERFACE TO DHCP")
#     elif remove_static_info == -1:
#         print("FAIL INTERFACE TO DHCP")
#
#

