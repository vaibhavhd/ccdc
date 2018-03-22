#!/usr/bin/python

pairs = {}

while True:
    pair = raw_input("Enter new IP:PORT | 'q' to start scanning\n")
    if pair == 'q':
        break
    ip,port = pair.split(":")
    pairs[ip] =port

print pairs

# namp --script hostmap-bfk.nse 192.168.2.1-100
