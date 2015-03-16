""" myrouter.py

    Uses code from Mark's github, adds more OID gets/sets as well as
    the ability to snmpwalk

"""

import netsnmp

class Router(object):
    def __init__(self, host, community):
        self.session = netsnmp.Session(DestHost=host,
                                        Community=community,
                                        Version=1)
        self.host = host
        self.refresh_value = 60

    def get_walk(self,oid):
        walked_list = netsnmp.snmpwalk(oid,
                        Version = 1,
                        DestHost=self.host,
                        Community="public")
        return walked_list

    def get_value(self, oid):
        varbind = netsnmp.Varbind(oid)
        self.session.get(netsnmp.VarList(varbind))
        return varbind.val

    def set_value(self, oid, value):
        varbind = netsnmp.Varbind(oid)
        self.session.get(netsnmp.VarList(varbind))
        varbind.val = value
        self.session.set(netsnmp.VarList(varbind))

    def get_hostname(self):
        return self.get_value('.1.3.6.1.2.1.1.5.0')

    def set_hostname(self, new_value):
        self.set_value('.1.3.6.1.2.1.1.5.0', new_value)

    def get_contact(self):
        return self.get_value('.1.3.6.1.2.1.1.4.0')

    def set_contact(self, new_value):
        self.set_value('.1.3.6.1.2.1.1.4.0', new_value)

    def get_location(self):
        return self.get_value('.1.3.6.1.2.1.1.6.0')

    def set_location(self, new_value):
        self.set_value('.1.3.6.1.2.1.1.6.0', new_value)

    def get_uptime(self):
        return self.get_value('.1.3.6.1.2.1.1.3.0')

    def get_routetable(self):
        return self.get_walk('.1.3.6.1.2.1.4.21.1.1')

    def get_routetable_dest(self):
        return self.get_walk('.1.3.6.1.2.1.4.24.4.1.1')

    def get_routetable_mask(self):
        return self.get_walk('.1.3.6.1.2.1.4.24.4.1.2')

    def get_routetable_nexthop(self):
        return self.get_walk('.1.3.6.1.2.1.4.24.4.1.4')

    def get_routetable_metric(self):
        # Get metric1
        return self.get_walk('.1.3.6.1.2.1.4.24.4.1.11')

    def get_cdpneighbors_hostname(self):
        # get neighbor hostname
        return self.get_walk('.1.3.6.1.4.1.9.9.23.1.2.1.1.6')

    def get_cdpneighbors_interface(self):
        # get neighbor interface
        return self.get_walk('.1.3.6.1.4.1.9.9.23.1.2.1.1.7')

def main():
    ### For Testing ####################################################
    r1 = Router("172.20.74.101", "public")
    print r1.get_hostname(), 'hostname'
    print len(r1.get_routetable_dest()), 'dest'
    print len(r1.get_routetable_mask()), 'mask'
    print len(r1.get_routetable_nexthop()), 'nexthop'
    print len(r1.get_routetable_metric()), 'metric'
    ####################################################################


if __name__ == '__main__':
    main()
