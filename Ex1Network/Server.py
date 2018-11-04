# coding: utf-8
import sys
from socket import socket, AF_INET, SOCK_DGRAM


def read_from_path():
    """ Simple function for creating our dictionary"""
    path = sys.argv[4]
    d = {}
    with open(path) as f:
        for line in f:
            # making sure to ignore empty lines
            if line.strip():
                (key, val) = line.split(',')
                d[key] = val
    return d


def write_to_path(key, val):
    """ Function for appending and updating our ips.txt"""
    path = sys.argv[4]
    line = key + "," + val
    file = open(path, "a")
    file.write(line)
    file.close()


def ask_daddy(website_key):
    """ Function for addressing father server,
        after no match was found in current dictionary"""
    parent_ip = sys.argv[2]
    parent_port = int(sys.argv[3])
    msg = website_key
    s.sendto(msg, (parent_ip, parent_port))
    answer, sender_info = s.recvfrom(2048)
    write_to_path(website_key, answer)
    return answer


def find_address(dic, website_key):
    """ Return a value in dictionary if found or ask father server"""
    if dic.has_key(website_key):
        return dic.get(website_key)
    else:
        answer = ask_daddy(website_key)
        dic[website_key] = answer
        return answer


# first loading our dictionary to the server
dic = read_from_path()
s = socket(AF_INET, SOCK_DGRAM)
my_port = int(sys.argv[1])
print "Server is running on port " + str(my_port) + "\n"
source_ip = sys.argv[2]
# noticing whether the server is the almighty last father or not
if source_ip != str(-1):
    s.bind((source_ip, my_port))
else:
    s.bind(('', my_port))
# receiving and answering client requests indefinably
while True:
    websiteKey, sender_info = s.recvfrom(2048)
    s.sendto(find_address(dic, websiteKey), sender_info)
