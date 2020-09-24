import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)


print("------------------------------------------------------------")
print(f"Please wait, scanning remote host, {remoteServerIP}")
print("------------------------------------------------------------")

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("Exiting...")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting...')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server. Exiting...")
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print (f"Scanning Completed in: ', {total}")
