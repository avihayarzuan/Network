# coding: utf-8
import sys
from socket import socket, AF_INET, SOCK_DGRAM


def read_from_path():
    path = sys.argv[4]
    d = {}
    with open(path) as f:
        for line in f:
            if line.strip():
                (key, val) = line.split(',')
                d[key] = val
    return d


def write_to_path(key, val):
    path = sys.argv[4]
    line = key + "," + val
    file = open(path, "a")
    file.write(line)
    file.close()


def ask_daddy(website_key):
    parent_ip = sys.argv[2]
    parent_port = int(sys.argv[3])
    msg = website_key
    s.sendto(msg, (parent_ip, parent_port))
    answer, sender_info = s.recvfrom(2048)
    write_to_path(website_key, answer)
    return answer


def find_address(dic, website_key):
    if dic.has_key(website_key):
        return dic.get(website_key)
    else:
        answer = ask_daddy(website_key)
        dic[website_key] = answer
        return answer


dic = read_from_path()
s = socket(AF_INET, SOCK_DGRAM)
my_port = int(sys.argv[1])
print "Server is running on port " + str(my_port) + "\n"
source_ip = sys.argv[2]
if source_ip != str(-1):
    s.bind((source_ip, my_port))
else:
    s.bind(('', my_port))
while True:
    websiteKey, sender_info = s.recvfrom(2048)
    s.sendto(find_address(dic, websiteKey), sender_info)
