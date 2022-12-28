import socket
import struct

# create a raw socket that listens to all incoming traffic
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# specify which interface to listen on (leave blank to listen on all interfaces)
# sniffer.bind(("eth0", 0))

# receive packets forever
while True:
    # receive a packet
    packet, addr = sniffer.recvfrom(65565)
    # unpack the packet header
    ip_header = packet[:20]
    iph = struct.unpack("!BBHHHBBH4s4s", ip_header)
    # print the source and destination IP addresses
    print("Source IP: {}\tDestination IP: {}".format(socket.inet_ntoa(iph[8]), socket.inet_ntoa(iph[9])))