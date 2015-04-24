""" Dallas Hays and Derrick Dsouza
    Lab 6: Netconf

    References:
"""

import paramiko
import xml.etree.ElementTree as etree
import xml.parsers.expat

hello = '''<?xml version="1.0" encoding="UTF-8"?>
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

class Lab6(object):
    def __init__(self, hostnames, username, password):
        self.hostnames = hostnames
        self.username = username
        self.password = password
        self.hello = '''<?xml version="1.0" encoding="UTF-8"?>
        <hello>
            <capabilities>
                <capability>
                    urn:ietf:params:xml:ns:netconf:base:1.0
                </capability>
            </capabilities>
        </hello>
        ]]>]]>'''
        self.get_config_request = '''
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

    def establish_connection(self, hostname, username, password):
        # Establish the connection
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname, 22, username, password, allow_agent=False, look_for_keys=False)

    def establish_channel(self):
        # ssh name@address -s netconf   These lines do the -s netconf part
        self.transport = self.client.get_transport()
        self.channel = self.transport.open_channel('session')
        self.channel.invoke_subsystem('netconf')

    def replace_data(self):
        data = ""
        while True:
            if data.find(']]>]]>') != -1:
                data = data.replace(']]>]]>', '')
                break

        data += self.channel.recv(1024)
        self.data = data.strip

    def print_tree(self, data):
        try:
            tree = etree.fromstring(data)
            print tree
        except xml.parsers.expat.ExpatError, ex:
            print ex


def main():

    print 1
    hostnames = ['172.20.74.238', '172.20.74.239', '172.20.74.240',
                '172.20.74.241', '172.20.74.242']
    username = 'netman'
    password = 'netman'

    print 2
    host1 = Lab6(hostnames, username, password)
    host1.establish_connection(hostnames[0], username, password)

    print 3
    host1.establish_channel()

    print 4
    host1.replace_data()

    print 5
    host1.client.close()

    """
    print 2
    # Establish the connection to the hostname
    myclient = establish_connection(hostname, username, password)
    mychannel = establish_channel(myclient)
    mydata = replace_data(mychannel)
    print mydata


    print 3
    # Send data
    mychannel.send(hello)
    mychannel.send(get_config_request)

    print 4
    # Receive the data
    mydata = replace_data(mychannel)
    print mydata

    print 5
    # Print tree data
    print_tree(mydata)

    print 6
    myclient.close()
    """


if __name__ == "__main__":
    main()

