from scapy.all import Ether, IP
Layer2 = Ether(src="01:02:03:04:05:06")
Layer3 = IP(dst="10.5.155.156")