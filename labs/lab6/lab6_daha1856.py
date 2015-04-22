""" Dallas Hays
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

hostname = '172.20.74.204'
hostnames = ['172.20.74.238', '172.20.74.239', '172.20.74.240',
            '172.20.74.241', '172.20.74.242']
username = 'netman'
password = 'netman'




# Get more information
#paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

# Establish the connection
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, 22, username, password, allow_agent=False, look_for_keys=False)

# ssh name@address -s netconf   These lines do the -s netconf part
transport = client.get_transport()
channel = transport.open_channel('session')
channel.invoke_subsystem('netconf')

data = ""
while True:
    if data.find(']]>]]>') != -1:
        data = data.replace(']]>]]>', '')
        break

    data += channel.recv(1024)
print data.strip()

channel.send(hello)
channel.send(get_config_request)

data = ""
while True:
    if data.find(']]>]]>') != -1:
        data = data.replace(']]>]]>', '')
        break

    data += channel.recv(1024)
print data.strip() # removes trailing newlines or white spaces

try:
    tree = etree.fromstring(data)
    print tree
except xml.parsers.expat.ExpatError, ex:
    print ex

# Create the shell channel, execute command & wait for response
#(stdin, stdout, stderr) = client.exec_command('show ip int br')
#for line in stdout.readlines():
#    print line
client.close()



def establish_connection(hostname, username, password):
    # Establish the connection
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, 22, username, password, allow_agent=False, look_for_keys=False)
    return client

def establish_channel(client)
    # ssh name@address -s netconf   These lines do the -s netconf part
    transport = client.get_transport()
    channel = transport.open_channel('session')
    channel.invoke_subsystem('netconf')
    return channel

def replace_data(channel):
    data = ""
    while True:
        if data.find(']]>]]>') != -1:
            data = data.replace(']]>]]>', '')
            break

    data += channel.recv(1024)
    return data.strip


def main():
    myclient = establish_connection()
    # TODO everything

    myclient.close()

if __name__ == "__main__":
    main()

