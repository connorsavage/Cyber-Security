# Purpose
Both packet sniffers only capture and display the IP header of each packet, which contain the source and destination IP addresses. To capture and display other information from the packets (such as the transport layer header and data), you can modify the code to unpack and process additional header fields.

# Java sniffer
This code creates a DatagramSocket that listens to all incoming traffic on the specified network interface (or on all interfaces if none is specified). It then enters an infinite loop and receives packets one at a time. The packet data is extracted and the source and destination IP addresses are extracted and printed to the console.

# Python Sniffer
This code creates a raw socket that listens to all incoming traffic on the specified network interface (or on all interfaces if none is specified). It then enters an infinite loop and receives packets one at a time. The packet header is then unpacked and the source and destination IP addresses are printed to the console.

