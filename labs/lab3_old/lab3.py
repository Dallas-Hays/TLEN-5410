""" Dallas Hays
    Lab 3
    2-18-2015

    THIS FILE IS CURRENTLY A BACKUP, PROBABLY DOESN'T WORK

    References:
    1. https://supportforums.cisco.com/discussion/12090896/snmp-how-get-
    list-ip-addresses-and-corresponding-interface-names
    Found out about snmpwalk and how I should use it to get interface info

    2. http://www.ibm.com/developerworks/aix/library/au-netsnmpnipython/
    Made me aware that netsnmp could do a snmpwalk

    3. http://www.tutorialspoint.com/python/tuple_len.htm
    How to find length of a tuple, used for listof_ifdescr

    4. http://stackoverflow.com/questions/1759455/how-can-i-account-for-
    am-or-pm-with-datetime-strptime
    For printing 12 hour time with AM and PM (%I for 12 hour, %p for AM/PM)
"""

import netsnmp
import time

class Router(object):
    def __init__(self, host):
        self.session = netsnmp.Session(DestHost=host,
                                        Community='public',
                                        Version=1)
        self.host = host
        self.ifindex = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.1')
        self.ifdescr = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.2')
        self.ifoutdiscards = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.19')
        self.ifnumber = netsnmp.Varbind('.1.3.6.1.2.1.2.1.0')
        self.get_varlist = netsnmp.VarList()
        self.get_varlist.append(self.ifindex)
        self.get_varlist.append(self.ifdescr)
        self.get_varlist.append(self.ifoutdiscards)
        self.get_varlist.append(self.ifnumber)


    def int_list(self):
#        ifindex = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.1')
#        ifdescr = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.2')
#        ifoutdiscards = netsnmp.Varbind('.1.3.6.1.2.1.2.2.1.19')
#        ifnumber = netsnmp.Varbind('.1.3.6.1.2.1.2.1.0')

        listof_ifdescr = netsnmp.snmpwalk('.1.3.6.1.2.1.2.2.1.2',
                                Version = 1,
                                DestHost=self.host,
                                Community="public")

        """
            netsnmp.snmpwalk gives us the interfaces, but also includes
            a Null at the end of the list, we need to skip that value so
            we iterate until the penultimate value of the tuple
        """
        skip_null = len(listof_ifdescr)-1
        print "List of interfaces ----"
        for i in range(0,skip_null):
            print "{0}: {1}".format(i+1, listof_ifdescr[i])

#        print "List of interfaces ----"
#        for i, j in enumerate(listof_ifdescr):
#            print "{0}: {1}".format(i+1, j)

        monitored_int = int(raw_input("Enter the interface to monitor: "))
        print "You chose: ", str(listof_ifdescr[monitored_int-1])
        monitored_time = int(raw_input("Enter number of minutes to "
                    "monitor (0 for indefinite): "))
        print "You chose: ", str(monitored_time)

        self.monitor(monitored_int, monitored_time)

    def monitor(self, interface, minutes):
        outdiscards = ".1.3.6.1.2.1.2.2.1.19." + str(interface)
        print outdiscards
        seconds = minutes * 60
        print seconds

        now = time.strftime("%I:%M %p", time.localtime(time.time()))
        if seconds == 0:
            print "Monitoring indefinitely starting at ", now
        else:
            print "Monitoring for {0} seconds starting at {1}".format(
            seconds, now)
        self.calc_packets(outdiscards, seconds)

    def calc_packets(self, oid, seconds):
        ifoutdiscards = netsnmp.Varbind(oid)
        self.session.get(netsnmp.VarList(ifoutdiscards))

        initial = int(ifoutdiscards.val)
        dropped_packets = 0
        count = 0

        if seconds == 0:
            while(True):
                time.sleep(60)
                count += 60
                self.session.get(netsnmp.VarList(ifoutdiscards))
                dropped_packets += int(ifoutdiscards.val) - initial
                print "{0} Seconds Monitoring: {1} dropped packets".format(
                        count, dropped_packets)
                self.isviolation(dropped_packets, 13000)
                dropped_packets = 0
                initial = int(ifoutdiscards.val)
                count = self.isovertime(count)
        else:
            while(seconds):
                time.sleep(60)
                count += 60
                seconds -= 60
                self.session.get(netsnmp.VarList(ifoutdiscards))
                dropped_packets += int(ifoutdiscards.val) - initial
                print "{0} Seconds Monitoring: {1} dropped packets".format(
                        count, dropped_packets)
                self.isviolation(dropped_packets, 13000)
                dropped_packets = 0
                initial = int(ifoutdiscards.val)
                count = self.isovertime(count)





    def isviolation(self, pkts, sla_req):
        if pkts > sla_req:
            now = time.strftime("%I:%M %p", time.localtime(time.time()))
            print "!!! Critical !!! SLA Violation at ", now

    def isovertime(self, count):
        if count == 300:
            print "5 minutes have passed... resetting the counter"
            return 0
        else:
            return count





    #    while(True):
    #        print (int(self.session.get(netsnmp.VarList(ifoutdiscards))[0]) - initial)
    #        time.sleep(10)

"""

        initial = int(self.session.get(netsnmp.VarList(ifoutdiscards))[0])
        #initial = int(ifoutdiscards.val)
        print initial
        while(True):
            print (int(self.session.get(netsnmp.VarList(ifoutdiscards))[0]) - initial)
            print "initial", initial
            time.sleep(10)
"""



#        print ifindex, ifdescr, ifoutdiscards, ifnumber
#        ifnumber_result = int(self.session.get(netsnmp.VarList(ifnumber))[0])
#        print ifnumber_result

# IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#        get_varlist = netsnmp.VarList()
#        get_varlist.append(ifnumber)
#        get_varlist.append(ifindex)
#        get_varlist.append(ifdescr)


# Do I need this?
#        self.session.get(netsnmp.VarList(ifnumber))

# This will allow me to see interfaces
#        self.session.getnext(get_varlist)
#        print ifdescr.val
#        self.session.getnext(get_varlist)
#        print ifdescr.val

        #self.session.getnext(get_varlist)

# another way to do it
#        interface_number = netsnmp.VarList(ifnumber)
#        print self.session.get(interface_number)

def main():
    """
    """
    #ip_add = raw_input("Network Element Management Address: ")
    #ip_add = "198.51.100.1" # DEBUGBDGUDBGUEDBEGGUDEBGUDEUGDEBGDUGBDEBGUEBG
    ip_add = "172.20.74.101"
    man_router = Router(ip_add)
    man_router.int_list()
#    man_router.monitor()


if __name__ == '__main__':
    main()
