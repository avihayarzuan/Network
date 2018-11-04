# coding: utf-8
import sys
from socket import socket, AF_INET, SOCK_DGRAM


def read_from_path():
    path = sys.argv[4]
    d = {}
    with open(path) as f:
        for line in f:
            (key, val) = line.split(',')
            d[key] = val
    return d


def write_to_path(key, val):
    path = sys.argv[4]
    line = key + "," + val + '\n'
    file = open(path, "w")
    file.write(line)
    file.close()


def ask_daddy(website_key):
    s = socket(AF_INET, SOCK_DGRAM)
    parent_ip = sys.argv[2]
    parent_port = sys.argv[3]
    msg = website_key
    s.sendto(msg, (parent_ip, parent_port))
    answer, sender_info = s.recvfrom(2048)
    s.close()
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
source_ip = sys.argv[2]
s.bind((source_ip, my_port))
while True:
    websiteKey, sender_info = s.recvfrom(2048)
    s.sendto(find_address(dic, websiteKey), sender_info)
