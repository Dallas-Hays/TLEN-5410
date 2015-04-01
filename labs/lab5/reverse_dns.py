# -*- coding: utf-8 -*-

import socket
#myip = "128.138.224.33"

myip = raw_input("Reverse DNS -- Enter an IP: ")

try:
    myname = socket.gethostbyaddr(myip)
    print "My DNS name is: ", myname[0]

except socket.herror, ex:
    print myip, "doesn’t have a reverse record."
