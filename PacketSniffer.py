import tkinter as tk
from scapy.all import sniff
from scapy.layers.l2 import Ether
from scapy.layers.http import HTTPRequest

def packet_callback(packet):
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        listbox.insert(tk.END, f"Packet: {ip_src} -> {ip_dst}")
        listbox.yview(tk.END)
    else:
        print("Non-IP packet captured")
    if packet.haslayer(HTTPRequest):
        print(f"HTTP Request: {packet[HTTPRequest].Host.decode()} {packet[HTTPRequest].Path.decode()}")
window = tk.Tk()
window.title("Packet Sniffer")

listbox = tk.Listbox(window, width=50, height=20)
listbox.pack()

sniff(iface="en0", prn=packet_callback, count=30)
window.mainloop()
