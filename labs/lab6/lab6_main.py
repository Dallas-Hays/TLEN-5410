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
from lab6_connection import Lab6

def check_config(hostname, host):
    """ Function will run all of the check functions and output the relevant
        information to the terminal.
    """

    print "Scanning the configuration for " + hostname + " ...",

    var1 = check_bob(host, 'bkool')
    var2 = check_readonly(host)
    var3 = check_http(host)
    var4 = check_mtu(host)

    #print host.data

    # Various tests to see if variables were changed
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
            print "Set the SNMP community string", var2[1], "to be read-only"
        if var3 == 1:
            print "Disabled the HTTP Service"
        if var4[0] == 1:
            for interface in var4[1]:
                print "Set the MTU for", interface, "to 1500"
    else:
        print 'OKAY'

    # Print with a comma so that the server response will be included
    print "",


def check_bob(host, del_user):
    """ Check if the user 'bkool' exists in the received xml file. if he
        does exist, remove him. Uses nested for loops to traverse the
        various children of the xml document. Returns 1 if it found the
        user and 0 if it did not
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
                            return 1 # HTTP service was running

        return 0 # There was no HTTP service running

    except xml.parsers.expat.ExpatError, ex:
        print ex



def check_mtu(host):
    """ Function will check for an MTU on all of the interfaces in the
        configuration. If there is no MTU it will add the xml element
        and if there is, it will set the MTU to 1500. Returns 1 if an MTU
        value was corrected and a 0 if there were no corrections. Also
        returns a list of the interfaces that were corrected.
    """
    try:
        tree = etree.fromstring(host.data)
        temp_list = [] # List for storing the interface that is changed
        var = 0

        for interfaces in tree.iter('interfaces'):
            for interface in interfaces.iter('interface'):
                for unit in interface.iter('unit'):
                    """
                    Decided to get rid of the following, just adds an
                    MTU if one does not exist, but then there is never
                    a case that is OKAY instead of NON-COMPLAINT
                    # ---------------------------------------
                    # If there is no mtu tag, add it
                    #if unit.find('mtu') is None:
                    #    unit.insert(1, etree.Element('mtu'))
                    # ---------------------------------------
                    """

                    # Change the mtu value to 1500
                    for mtu in unit:
                        if mtu.tag == 'mtu':
                            if mtu.text != '1500':
                                mtu.text = '1500'
                                temp_list.append(interface.find('name').text)
                                var = 1 # An MTU was changed

            host.data = etree.tostring(tree)
            return var, temp_list

        return 0

    except xml.parsers.expat.ExpatError, ex:
        print ex

def check_readonly(host):
    """ Function will check if the config is in read-write for
        authentication, if it is it will change it to read-only. Returns
        1 if it was converted to read-only and a 0 if it was already read-only.
        Also returns the community string.
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
                        return 1, community_string # Changed to read only

        return 0, community_string # Already read-only

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

    oureditconfig_template = '''
<rpc>
    <edit-config>
        <target>
            <running/>
        </target>
        <config>
            <configuration>
'''

    # The IPs that we will check configs of
    hostnames = ['172.20.74.238', '172.20.74.239', '172.20.74.240',
                '172.20.74.241', '172.20.74.242']

    username = 'netman'
    password = 'netman'

    for hostname in hostnames:
        # Establish the first host
        host1 = Lab6()

        # Create the host connection
        host1.establish_connection(hostname, username, password)

        # Create the host channel
        host1.establish_channel()

        # Strip the data
        host1.replace_data()

        # Send the hellow and ask for the client's config
        host1.channel.send(hello)
        host1.channel.send(get_config_request)

        # Receive the config and store in host1.data
        host1.replace_data()

        # Run all of the check functions on the pulled configuration
        check_config(hostname, host1)

        # Check to make sure the data being sent back is good
        #print host1.data

        # Remove the first and last lines of host1.data, strips the rpc-reply
        stripped_data = ''.join(host1.data.splitlines(True)[1:-1])

        # Add the closing xmls to the corrected config
        my_edit_config_request = (oureditconfig_template + stripped_data +
        '</configuration>\n</config>\n</edit-config>\n</rpc>\n]]>]]>\n')

        # Send the edited config file back to the server
        host1.channel.send(my_edit_config_request)

        # Receive the server response
        host1.replace_data()

        print "Server Response:", host1.data, "\n"

        # Close the connection
        host1.client.close()


if __name__ == "__main__":
    main()
