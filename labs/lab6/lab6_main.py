""" Dallas Hays and Derrick Dsouza
    Lab 6: Netconf

    References:
    1. https://docs.python.org/2/library/xml.etree.elementtree.html
        --Documentation on how to use element tree (removing nodes)
    2. http://stackoverflow.com/questions/8186343/how-do-you-parse-
    nested-xml-tags-with-python
        --Helped me understand how to parse nested xml
"""

import paramiko
import xml.etree.ElementTree as etree
import xml.parsers.expat
from lab6_daha1856 import Lab6

first_config = """<rpc-reply><configuration>
    <version>9.3R4.4</version>
    <system>
        <host-name>rancid</host-name>
        <login>
            <user>
                <name>admin</name>
                <full-name>Administrator</full-name>
                <uid>2001</uid>
                <class>superuser</class>
            </user>
            <user>
                <name>netman</name>
                <uid>2000</uid>
                <class>super-user</class>
            </user>

        </login>
        <services>
            <ssh>
            </ssh>
            <netconf>
                <ssh>
                </ssh>
            </netconf>

        </services>
    </system>
    <interfaces>
        <interface>
            <name>ge-0/0/0</name>
            <unit>
                <name>0</name>
                <family>
                    <inet>
                    </inet>
                </family>
            </unit>
        </interface>
        <interface>
            <name>ge-0/0/1</name>
            <unit>
                <name>0</name>
                <mtu>1500</mtu>
                <family>
                    <inet>
                    </inet>
                </family>
            </unit>
        </interface>
    </interfaces>
    <snmp>
        <community>
            <name>euFohca7na</name>
            <authorization>read-write</authorization>
        </community>
    </snmp>
</configuration></rpc-reply>"""



def check_config(hostname, host):
    print "Scanning the configuration for " + hostname + " ...",

    var1 = check_bob(host, 'bkool')
    var2 = check_readonly(host)
    var3 = check_http(host)
    var4 = check_mtu(host)

    #print host.data

    #print var1, "bkool"
    #print var2, "read-only"
    #print var3, "web-man"
    #print var4, "mtu"
    #print var4[1][0], 'test'

    if var1 or var2[0] or var3 or var4[0] == 1:
        print 'NON-COMPLAINT'

    if var1 == 1:
        print "Removed User Bob Kool"
    if var2[0] == 1:
        print "Set the SNMP community string ", var2[1], "to be read-only"
    if var3 == 1:
        print "Disabled the HTTP Service"
    if var4[0] == 1:
        for interface in var4[1]:
            print "Set the MTU for", interface, "to 1500"



def check_bob(host, del_user):
    """ Check if the user 'bkool' exists in the received xml file. if he
        does exist, remove him. Uses nested for loops to traverse the
        various children of the xml document
    """
    try:
        tree = etree.fromstring(host.data)
        for rpcreply in tree.find('configuration'):
            for configuration in rpcreply:
                for user in configuration.findall('user'):
                    if user.find('name').text == del_user: # user to remove
                        configuration.remove(user)
                        host.data = etree.tostring(tree)
                        return 1; # bkool was found

        return 0; # bkool was not found

    except xml.parsers.expat.ExpatError, ex:
        print ex

def check_http(host):
    """ Function will check if the config shows a running http server
        running. If it does then it will remove the web-management from
        the config.
    """
    try:
        tree = etree.fromstring(host.data)

        for rpcreply in tree:
            for configuration in rpcreply:
                for system in configuration:
                    for services in system:
                        if services.tag == "web-management":
                            system.remove(services)
                            host.data = etree.tostring(tree)
                            return 1

        return 0

    except xml.parsers.expat.ExpatError, ex:
        print ex



def check_mtu(host):
    """ Function will check for an MTU on all of the interfaces in the
        configuration. If there is no MTU it will add the xml element
        and if there is it will set the MTU to 1500

        TODO:
            -Right now it will say it changed the MTU to 1500 of all
            interfaces even if only 1 was changed
    """
    try:
        tree = etree.fromstring(host.data)

        temp_list = []
        var = 0

        for interfaces in tree.iter('interfaces'):
            # Find the interface name
            for interface in interfaces.iter('interface'):
                temp_list.append(interface[0].text)

            # Check mtu
            for unit in interfaces.iter('unit'):
                # If there is no mtu tag, add it
                if unit.find('mtu') is None:
                    unit.insert(1, etree.Element('mtu'))

                # Change the mtu value to 1500
                for mtu in unit:
                    if mtu.tag == 'mtu':
                        if mtu.text != '1500':
                            mtu.text = '1500'
                            var = 1


            host.data = etree.tostring(tree)
            return var, temp_list

        return 0

    except xml.parsers.expat.ExpatError, ex:
        print ex

def check_readonly(host):
    """ Function will check if the config is in 'read-write' for
        authentication, if it is it will change it to 'read-only'
    """
    try:
        tree = etree.fromstring(host.data)

        # Find the community string
        for test in tree.iter('community'):
            for name in test.iter('name'):
                community_string = name.text

        # Convert to read-only
        for rpcreply in tree.find('configuration'):
            for snmp in rpcreply:
                for community in snmp.findall('authorization'):
                    # if read-write, change to read-only
                    if community.text == 'read-write':
                        community.text = 'read-only'
                        host.data = etree.tostring(tree)
                        return 1, community_string;
        return 0, community_string

    except xml.parsers.expat.ExpatError, ex:
        print ex

def main():
    hello = '''
<?xml version="1.0" encoding="UTF-8"?>
<hello>
    <capabilities>
        <capability>
            urn:ietf:params:xml:ns:netconf:base:1.0
    </capability>
</capabilities>
</hello>
]]>]]>'''

    get_config_request = '''
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="105" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<get-config>
    <source>
        <running/>
    </source>
</get-config>
</rpc>
]]>]]>
'''

    hostnames = ['172.20.74.238', '172.20.74.239', '172.20.74.240',
                '172.20.74.241', '172.20.74.242']

    username = 'netman'
    password = 'netman'
    hostname = '172.20.74.238'

    # Establish the first host
    host1 = Lab6()

    # Create the host connection
    host1.establish_connection(hostnames[3], username, password)

    # Create the host channel
    host1.establish_channel()

    # Strip the data
    host1.replace_data()

    print host1.data

    # Send data
    host1.channel.send(hello)
    host1.channel.send(get_config_request)

    # Receive the result
    host1.replace_data()

    print "This is data"
    print host1.data
    print "End Data\n"

    check_config(hostname, host1)

    host1.client.close()

if __name__ == "__main__":
    main()