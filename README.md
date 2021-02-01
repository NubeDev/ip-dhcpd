Some code to set a manual IP/DHCP for dhcpcd (as used on the raspberry pi)


usage

```python
from lib.ip import *

ip = dhcpcdManager()
iface = "eth0"

# update the etc/dhcpcd.conf when testing in /lib/ip.py
ip.set_static_info(iface, "192.168.15.7", "192.168.15.1", "8.8.8.8", "255.255.255.0")  # add a static ip
ip.remove_static_info(iface)  # set back to DHCP

#
```