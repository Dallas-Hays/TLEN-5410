"""
"""

import lab1

def find_interface(data):
    new_data = data.split(' ')
    for i in new_data:
        if i.startswith('IF-MIB::ifDescr'):
            return new_data[new_data.index(i)+1]

def find_trapaddress(data):
    new_data = data.split(' ')
    for i in new_data:
        if i.startswith('SNMP-COMMUNITY-MIB::snmpTrapAddress'):
            return new_data[new_data.index(i)+1].splitlines()[0]
            #return new_data[new_data.index(i)+1]


def which_trap(data):

    if 'linkUp' in data:
        print 'linkUp'
        print find_interface(data)

    if 'linkDown' in data:
        print 'linkDown'
        print find_interface(data)

    if 'enterprises.9.9.43.2.0.1' in data:
        config_change(data)

    if 'mib-2.16.0.1' in data:
        print 'bandwidth'
        print find_trapaddress(data)

def config_change(data):
    """

    """
    print find_trapaddress(data)

    connection = []
    connection.append(find_trapaddress(data))

    lab1.getConfigurations(connection)
    lab1.isNew(connection)


def main():
    data1 = """
    <UNKNOWN>
    UDP: [198.51.100.1]:53935->[198.51.100.2]:162
    DISMAN-EVENT-MIB::sysUpTimeInstance 0:1:41:20.79
    SNMPv2-MIB::snmpTrapOID.0 IF-MIB::linkUp
    IF-MIB::ifIndex.2 2
    IF-MIB::ifDescr.2 FastEthernet1/0
    IF-MIB::ifType.2 ethernetCsmacd
    SNMPv2-SMI::enterprises.9.2.2.1.1.20.2 "up"
    SNMP-COMMUNITY-MIB::snmpTrapAddress.0 198.51.100.1
    SNMP-COMMUNITY-MIB::snmpTrapCommunity.0 "public"
    SNMPv2-MIB::snmpTrapEnterprise.0 SNMPv2-MIB::snmpTraps"""

    data2 = """
    <UNKNOWN>
    UDP: [198.51.100.1]:53935->[198.51.100.2]:162
    DISMAN-EVENT-MIB::sysUpTimeInstance 0:1:40:16.05
    SNMPv2-MIB::snmpTrapOID.0 IF-MIB::linkDown
    IF-MIB::ifIndex.2 2
    IF-MIB::ifDescr.2 FastEthernet1/0
    IF-MIB::ifType.2 ethernetCsmacd
    SNMPv2-SMI::enterprises.9.2.2.1.1.20.2 "administratively down"
    SNMP-COMMUNITY-MIB::snmpTrapAddress.0 198.51.100.1
    SNMP-COMMUNITY-MIB::snmpTrapCommunity.0 "public"
    SNMPv2-MIB::snmpTrapEnterprise.0 SNMPv2-MIB::snmpTraps"""

    data3 = """
    <UNKNOWN>
    UDP: [198.51.100.1]:58951->[198.51.100.2]:162
    DISMAN-EVENT-MIB::sysUpTimeInstance 0:0:13:14.28
    SNMPv2-MIB::snmpTrapOID.0 SNMPv2-SMI::enterprises.9.9.43.2.0.1
    SNMPv2-SMI::enterprises.9.9.43.1.1.6.1.3.10 1
    SNMPv2-SMI::enterprises.9.9.43.1.1.6.1.4.10 3
    SNMPv2-SMI::enterprises.9.9.43.1.1.6.1.5.10 4
    SNMP-COMMUNITY-MIB::snmpTrapAddress.0 198.51.100.1
    SNMP-COMMUNITY-MIB::snmpTrapCommunity.0 "public"
    SNMPv2-MIB::snmpTrapEnterprise.0 SNMPv2-SMI::enterprises.9.9.43.2"""

    data4 = """
    <UNKNOWN>
    UDP: [198.51.100.1]:58951->[198.51.100.2]:162
    DISMAN-EVENT-MIB::sysUpTimeInstance 0:0:17:28.36
    SNMPv2-MIB::snmpTrapOID.0 SNMPv2-SMI::mib-2.16.0.1
    SNMPv2-SMI::mib-2.16.3.1.1.1.2 2
    SNMPv2-SMI::mib-2.16.3.1.1.3.2 IF-MIB::ifInOctets.2
    SNMPv2-SMI::mib-2.16.3.1.1.4.2 2
    SNMPv2-SMI::mib-2.16.3.1.1.5.2 277704
    SNMPv2-SMI::mib-2.16.3.1.1.7.2 5124
    SNMP-COMMUNITY-MIB::snmpTrapAddress.0 198.51.100.1
    SNMP-COMMUNITY-MIB::snmpTrapCommunity.0 "public"
    SNMPv2-MIB::snmpTrapEnterprise.0 SNMPv2-SMI::mib-2.16"""



    which_trap(data1)
    which_trap(data2)
    which_trap(data3)
    which_trap(data4)

    """
def main():
    """


    data = ''
    output_file = open('/tmp/trap.log', 'a')

    while(True):
        try:
            data = raw_input()
        #    which_trap(data)
        #   function call to handle trap
            output_file.write(data + '\n')
        # data += raw_input()
        except EOFError:
            break
    output_file.close()

if __name__ == '__main__':
    main()
