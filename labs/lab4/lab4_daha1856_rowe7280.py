""" Dallas Hays and Robert Werthman
    Lab 4

    Note to grader:
    Check the email_alert() function to change the email address you want
    the message to be sent to

    References:
    1.http://rosettacode.org/wiki/Send_an_email#Python
    For how to send an email with python

    2. Cisco SNMP Object navigator

    3. http://www.cisco.com/c/en/us/support/docs/network-management/
    remote-monitoring-rmon/17428-18.html
    For setting up rmon on the router

    4.

"""

import lab1
import smtplib

def find_interface(data):
    """
    """
    new_data = data.split(' ')
    for i in new_data:
        if i.startswith('IF-MIB::ifDescr'):
            return new_data[new_data.index(i)+1].splitlines()[0]

def find_trapaddress(data):
    """
    """
    new_data = data.split(' ')
    for i in new_data:
        if i.startswith('SNMP-COMMUNITY-MIB::snmpTrapAddress'):
            return new_data[new_data.index(i)+1].splitlines()[0]

def email_alert(data, trap, other):
    """
    """

    login = 'bobdallas.tlen5540'
    password = 'netman2015'
    from_addr = 'bobdallas.tlen5540@gmail.com'
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % from_addr
    message = ''

    if trap == 'linkUp':
        subject = 'TLEN5410 linkUp Notification'
        message = 'The interface %s has come up.\n' % other
        message += 'Full trap: %s ' % data

    if trap == 'linkDown':
        subject = 'TLEN5410 linkDown Notification'
        message = 'The interface %s has gone down.\n' % other
        message += 'Full trap: %s ' % data

    if trap == 'ConfigChange':
        subject = 'TLEN5410 configuration change Notification'
        message = other + '\n'
        message += 'Full trap: %s ' % data

    if trap == 'UpperThreshold':
        subject = 'TLEN5410 upper bandwidth threshold Notification'
        message = 'The device has surpassed the 5000 byte threshold\n'
        message += 'Full trap: %s ' % data

    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr,password)
    problems = server.sendmail(from_addr, from_addr, message)
    server.quit()
    return problems

def which_trap(data):
    """
    """

    if 'linkUp' in data:
        print 'linkUp'
        print find_interface(data)
        print email_alert(data, 'linkUp', find_interface(data))


    if 'linkDown' in data:
        print 'linkDown'
        print find_interface(data)
        print email_alert(data, 'linkDown', find_interface(data))

    if 'enterprises.9.9.43.2.0.1' in data:
        print 'Configuration change'
        print find_trapaddress(data)
        other = config_change(data)
        print email_alert(data, 'ConfigChange', other)

    if 'mib-2.16.0.1' in data:
        print 'bandwidth'
        # TODO: email

def config_change(data):
    """
    """
    connection = []
    connection.append(find_trapaddress(data))

    lab1.getConfigurations(connection)
    lab1.isNew(connection)
    return lab1.printInformation(connection)

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



#    which_trap(data1)
#    which_trap(data2)
    which_trap(data3)
#    which_trap(data4)


    """
def main():
    """

    """
    data = ''
    output_file = open('/tmp/trap.log', 'a')

    while(True):
        try:
            data = raw_input()
        #   which_trap(data)
        #   function call to handle trap
            output_file.write(data + '\n')
        # data += raw_input()
        except EOFError:
            break

    which_trap(data)
    output_file.close()
    """

if __name__ == '__main__':
    main()
