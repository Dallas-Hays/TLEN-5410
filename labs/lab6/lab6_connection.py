""" Dallas Hays and Derrick Dsouza
    Lab 6: Netconf

    References:
    1. https://mail.python.org/pipermail/python-list/2013-
    September/667860.html
        -- Remove first and last lines of a multiline string (very cool)
"""

import paramiko
import xml.etree.ElementTree as etree
import xml.parsers.expat

class Lab6(object):
    """ This Class takes the python code we worked with in class and
        puts them into functions to be called by the other python file
        that will check the configs.
    """

    def establish_connection(self, hostname, username, password):
        # Establish the connection to the server
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname, 22, username, password,
                            allow_agent=False, look_for_keys=False)

    def establish_channel(self):
        # ssh name@address -s netconf   These lines do the -s netconf part
        transport = self.client.get_transport()
        self.channel = transport.open_channel('session')
        self.channel.invoke_subsystem('netconf')

    def replace_data(self):
        # Replace the delimiter at the end of the file
        data = ""
        while True:
            if data.find(']]>]]>') != -1:
                data = data.replace(']]>]]>', '')
                break

            data += self.channel.recv(1024)
        self.data = data.strip()


def main():
    """ DEBUG MAIN, USED TO TEST IF THE RPC SENDING AND RECEIVING IS WORKING
    """

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

    hostnames = ['172.20.74.238', '172.20.74.239', '172.20.74.240',
                '172.20.74.241', '172.20.74.242']

    username = 'netman'
    password = 'netman'
    hostname = '172.20.74.241'

    # Establish the first host
    host1 = Lab6()

    # Create the host connection
    host1.establish_connection(hostname, username, password)

    # Create the host channel
    host1.establish_channel()

    # Strip the data
    host1.replace_data()

    #print host1.data

    # Send data
    host1.channel.send(hello)
    host1.channel.send(get_config_request)

    # Receive the result
    host1.replace_data()

    print host1.data

    # Test contains host1.data without the first and last line
    test = ''.join(host1.data.splitlines(True)[1:-1])

    my_edit_config_request = (oureditconfig_template + test +
    '</configuration>\n</config>\n</edit-config>\n</rpc>\n]]>]]>\n')

    print my_edit_config_request

    print '1'
    host1.channel.send(my_edit_config_request)

    print '2'
    host1.replace_data()

    print '3'
    print host1.data


    host1.client.close()


if __name__ == "__main__":
    main()

