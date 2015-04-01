
import socket
#mydstport = 80
mydstport = int(raw_input("Port Service Lookup --- Enter port number: "))

try:
    myservice = socket.getservbyport(mydstport, "tcp")
    print "That service is: ", myservice
except:
    print mydstport, "is not tracked by IANA."
