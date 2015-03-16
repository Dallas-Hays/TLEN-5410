""" Dallas Hays
    Lab 2
    2-4-2015

    References:
    1. http://stackoverflow.com/questions/176918/finding-the-index-of-an-i
       tem-given-a-list-containing-it-in-python
    For how to find an index in a list by reference to what is contained
    at the index, EG: self.index(something)

    2. https://docs.python.org/2/library/functions.html#isinstance
    How to use the isinstance function

    3.  http://stackoverflow.com/questions/875074/how-to-print-a-list-
        dict-or-collection-of-objects-in-python
    For printing the port values (print s0.ports) through the use of __repr__

"""
import random

class Switch(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.ports = []        # An empty list of switches/hosts connected to
        self.forwardtable = {} # An empty dictionary for forwardingtable

    def forward(self, in_packet, in_sender=None):
        """ Used to forward a packet to a destination host that exists
            in the forwarding table. This method performs both forwarding
            and broadcasting. This is determined by the in_sender argument

            if in_sender != None -> FORWARD
            if in_sender == None -> BROADCAST

            To forward, we get the packet's destination hostname from the
            forwardtable and send the packet through the receieve method

            To broadcast, we loop through all the ports of the switch, and
            call the receieve method on all but whoever originated the
            packet
        """
        if in_sender == None: # FORWARD
            host_dst = self.forwardtable[in_packet.dst]
            # If Host? only forward packet
            if isinstance(self.ports[host_dst], Host):
                self.ports[host_dst].receive(in_packet)
            # If Switch? send my switch info as well
            else:
                self.ports[host_dst].receive(self, in_packet)
        else: # BROADCAST
            for allports in self.ports:
                if allports != in_sender:
                    # If Host? Only send packet info
                    if isinstance(allports, Host):
                        allports.receive(in_packet)
                    # If Switch? send my switch infor as well
                    else:
                        allports.receive(self, in_packet)

    def connect(self, in_device):
        """ Connect a switch to another device (Host or Switch) """
        print "Connecting %s to %s" % (self.name, in_device.name)
        self.ports.append(in_device)

    def receive(self, in_sender, in_packet):
        """ Used to receive packets from the other devices. Upon receiving
            a packet, it will add the source to its forwarding table if
            necessary. Then it will decide if it should forward or broadcast
            depending on whether the destination address is in the forwarding
            table or not
        """
        if in_packet.src in self.forwardtable:
            # Exists in forward table, do nothing
            pass
        else:
            # Not in forward table, add it to it
            self.forwardtable[in_packet.src] = self.ports.index(in_sender)

        if in_packet.dst in self.forwardtable:
            self.forward(in_packet)            # FORWARD
        else:
            self.forward(in_packet, in_sender) # BROADCAST

    def __repr__(self):
        """ Needed for printing the port list and forwardtable """
        return self.name

class Host(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def connect(self, in_device):
        """ Used to connect a Host with a Switch
            connected will always be a switch for the Host
        """
        print "Connecting %s to %s" % (self.name, in_device.name)
        self.connected = in_device

    def receive(self, in_packet):
        """ Used when the Switch has determined to either forward or
            broadcast. Simply checks if the Host was the destination of
            the packet and prints, drops otherwise
        """
        if self.address == in_packet.dst:
            print 'Host %s (%s) Received "%s" from %s' % \
            (self.name, self.address, in_packet.payload, in_packet.src)

    def send(self, dst_host):
        """ Used to send a packet from one Host to another. Simply creates
            a packet, and uses the Switch receive method to send the packet
            to the dst_host
        """
        print "Sending data from %s (%s) to %s (%s)" % \
            (self.name, self.address, dst_host.name, dst_host.address)
        pkt = Packet(self.address, dst_host.address, "Hello World")
        self.connected.receive(self, pkt)

    def __repr__(self):
        """ For printing the port list in the Switch Class """
        return self.name

class Packet(object):
    """ A container class for packets
        Attributes: source, destination, and payload
    """
    def __init__(self, src, dst, payload):
        self.src = src
        self.dst = dst
        self.payload = payload

def generate_mac():
    """ From the lab3_simplemain.py file on D2L """
    mac = ""
    for i in range(0, 6):
        mac += "%02x:" % random.randint(0x00, 0xff)
    return mac.strip(":")

def main():
    # Create the 3 switches
    s0 = Switch("s0", generate_mac())
    s1 = Switch("s1", generate_mac())
    s2 = Switch("s2", generate_mac())

    # Create the 6 hosts
    h0 = Host("h0", generate_mac())
    h1 = Host("h1", generate_mac())
    h2 = Host("h2", generate_mac())
    h3 = Host("h3", generate_mac())
    h4 = Host("h4", generate_mac())
    h5 = Host("h5", generate_mac())

    # Connect the 3 switches, in a line s0-s1-s2
    s0.connect(s1)
    s1.connect(s0)
    s1.connect(s2)
    s2.connect(s1)

    # Connect the 1st switch (s0), with 2 hosts (h0, h1)
    s0.connect(h0)
    h0.connect(s0)
    s0.connect(h1)
    h1.connect(s0)

    # Connect the 2nd switch (s1), with 2 hosts (h2, h3)
    s1.connect(h2)
    h2.connect(s1)
    s1.connect(h3)
    h3.connect(s1)

    # Connect the 3rd switch (s2), with 2 hosts (h4, h5)
    s2.connect(h4)
    h4.connect(s2)
    s2.connect(h5)
    h5.connect(s2)

    # Send data between h0 and h5
    h0.send(h5)
    h5.send(h0)

    # Print out the values of ports & forward table from the switch
    print ""
    print "Port list: "
    print s0, s0.ports
    print s1, s1.ports
    print s2, s2.ports
    print "Forward table: "
    print s0, s0.forwardtable
    print s1, s1.forwardtable
    print s2, s2.forwardtable

if __name__ == "__main__":
    main()
