# coding: utf-8
import sys
from socket import socket, AF_INET, SOCK_DGRAM


def readFromPath():
    #path = "C:\ips.txt"
	path = sys.argv[4]
	d ={}
	with open(path) as f:
		for line in f:
			(key,val) = line.split(',')
			d[key]=val
	return d

def writeToPath(key,val):
	#path = "C:\ips.txt"
	path = sys.argv[4]
	line = key + "," + val + '\n'
	file = open(path,w)
	file.write(line)
	file.close()

def askDaddy(websiteKey):
	s = socket(AF_INET, SOCK_DGRAM)
	#dest_ip = '127.0.0.1'
	parent_ip = sys.argv[2]
	parent_port = 8081
	msg = websiteKey
	s.sendto(msg, (parent_ip,parent_port))
	answer, sender_info = s.recvfrom(2048)
	s.close()

def findAddress(dic,websiteKey):
	if dic.has_key(websiteKey):
		return dic.get(websiteKey)
	else:
		answer = askDaddy(websiteKey)
		dic[websiteKey] = answer

		return answer
	#return "answer"

dic = readFromPath()
#print d

s = socket(AF_INET, SOCK_DGRAM)
#source_ip = '127.0.0.1'
#source_port = 8080
my_port = sys.argv[1]
source_ip = sys.argv[2]
s.bind((source_ip, my_port))
while True:
	websiteKey, sender_info = s.recvfrom(2048)
	s.sendto(findAddress(dic,websiteKey), sender_info)

	#print "Message: ", websiteKey, " from: ", sender_info
#	s.sendto(data.upper(), sender_info)

