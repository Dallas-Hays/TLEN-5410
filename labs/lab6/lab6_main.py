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



def check_config(hostname):
    print "Scanning the configuration for " + hostname + " ...",


def check_bob(host):
    """ Check if the user 'bkool' exists in the received xml file. if he
        does exist, remove him. Uses nested for loops to traverse the
        various children of the xml document
    """
    # host is object of class Lab6 from lab6_daha1856.py
    try:
        tree = etree.fromstring(host.data)
        #foos = tree.findall('.//user')
        for rpcreply in tree.find('configuration'):
            for configuration in rpcreply:
                for user in configuration.findall('user'):
                    if user.find('name').text == 'admin': # user to remove
                        configuration.remove(user)
                        host.data = etree.tostring(tree)
                        return 1; # bkool was found

        return 0; # bkool was not found

    except xml.parsers.expat.ExpatError, ex:
        print ex

def check_http(host):
    # TODO
    pass

def check_mtu(host):
    # TODO
    pass

def check_readonly(host):
    """ TODO
    """
    try:
        tree = etree.fromstring(host.data)
        for rpcreply in tree.find('configuration'):
            for snmp in rpcreply:
                for community in snmp.findall('authorization'):
                    # if read-write, change to read-only
                    if community.text == 'read-write':
                        community.text = 'read-only'
                        host.data = etree.tostring(tree)
                        return 1;
            #    for community in snmp:
            #        print community.find('authorization').text
        return 0;

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

    check_config(hostname)

    # Establish the first host
    host1 = Lab6()

    # Create the host connection
    host1.establish_connection(hostnames[2], username, password)

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

    # End
    host1.client.close()

    print "This is data"
    print host1.data
    print "End Data"

    print check_bob(host1)
    print check_readonly(host1)

    print host1.data




if __name__ == "__main__":
    main()
