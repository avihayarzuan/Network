# coding: utf-8
import sys
from socket import socket, AF_INET, SOCK_DGRAM

# creating our udp socket and saving our program arguments
s = socket(AF_INET, SOCK_DGRAM)
dest_ip = sys.argv[1]
dest_port = int(sys.argv[2])
print "Please enter a website address!\nTo quit - simply type quit..."
web_add = raw_input()
# sending the request to our server and printing the response
while not web_add == 'quit':
    s.sendto(web_add, (dest_ip, dest_port))
    web_ip, sender_info = s.recvfrom(2048)
    print web_ip
    web_add = raw_input()
# lastly closing the socket
s.close()
