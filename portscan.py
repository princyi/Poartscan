#!/usr/bin/python 3
import socket
import socketserver
import sys
import time
import threading

user = "python port_scan.py target start_port end_port"

print("_"*70)
print("Python Simple Port Scanner")
print("_"*70)

start_time = time.time()

if(len(sys.arg) !=4):
    print(user)
    sys.exit()

try:
    target = socket.gethostbyname(sys.arg[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_poart = int(sys.argv[3])

print("Scanning target",target)

def scan_port(port):
   # print("Scanning port:", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    if (not conn):
        print("Port {} is OPEN".format(port))
    s.close()

for port in range(start_port, end_port+1):

   thread = threading.Thread(target = scan_port, args = (port,))
   thread.start()

   end_time _ time.time()
   print("Time elapsed:,end_time  start_time,'s'")




