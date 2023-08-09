# Poartscan to attack a target by yourself
# With the help of Python
#python3.11.1

I  make a small port scanner script in Python. The concept is to make a connection with each given port and if it is successful, that port is open. 

DETAILS OF Port-Scanner Code.

1. Command line arguments in Python
2. Importing socket, sys, time, threading
3. Iterating through start and end ports
4. Making socket connections on each port
5. Checking if the connection is successful
6. Optimizing the script with multi-threading
7. Calculating time elapsed in the scan 




Port Scanner Code of Conduct

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


