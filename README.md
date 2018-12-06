# antarcticrx
Code to support an HF receiver for Antarctica

# Red Pitaya IP Address
DNSMasq acts as DHCP server that creates the 192.168.5.x network
the Red Pitaya is connected to. To find the Red Pitaya IP address
and see DNSMasq DHCP Leases:

$ cat /var/lib/misc/dnsmasq.leases
