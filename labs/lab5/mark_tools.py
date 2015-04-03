# -*- coding: utf-8 -*-

"""
"""

import socket

def reverse_dns(myip):
    try:
        myname = socket.gethostbyaddr(myip)
        #print "My DNS name is: ", myname[0]
        return myname[0]

    except socket.herror, ex:
        pass
        return myip
        #print myip, "doesn’t have a reverse record."

def port_service_lookup(mydstport):
    try:
        myservice = socket.getservbyport(mydstport, "tcp")
        #print "That service is: ", myservice
        return myservice
    except:
        return mydstport
        #print mydstport, "is not tracked by IANA."
