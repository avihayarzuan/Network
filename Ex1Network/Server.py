# coding: utf-8
from socket import socket, AF_INET, SOCK_DGRAM


def readFromPath():
    path = "C:\ips.txt"
    #path = "C:\Users\Avihay Arzuan\Google Drive\שיתוף אורי אביחי\רשתות תרגיל 1\ips.txt"
    d ={}
    with open(path) as f:
        for line in f:
            (key,val) = line.split(',')
            d[key]=val
    return d

def askDaddy(data):
	s = socket(AF_INET, SOCK_DGRAM)
	dest_ip = '127.0.0.1'
	dest_port = 8081
	msg = data
	#msg = raw_input(data)
	#while not msg == 'quit':
	s.sendto(msg, (dest_ip,dest_port))
	data, sender_info = s.recvfrom(2048)
		#print "Server sent: ", data
		#msg = raw_input("Message to send: ")
	s.close()

def findAdress(dic,data):
	if dic.has_key(data):
		return dic.get(data)
	else:
		return askDaddy(data)
	#return "answer"

dic = readFromPath()
print d

s = socket(AF_INET, SOCK_DGRAM)
source_ip = '127.0.0.1'
source_port = 8080
s.bind((source_ip, source_port))
while True:
	data, sender_info = s.recvfrom(2048)
	print "Message: ", data, " from: ", sender_info
	s.sendto(findAdress(dic,data), sender_info)


#	s.sendto(data.upper(), sender_info)

