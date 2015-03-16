""" Lab 1 : Router Configurations
    By Dallas Hays
    1/22/15

    Note to grader:
    Will make the following directories
        /home/netman/tmpconf
        /home/netman/routerconfigs

    External Sources:

    1. http://pymotw.com/2/glob/
    For how to have unix style pattern matching for files with an
    asterisk IE: myfile.*

    2. http://stackoverflow.com/questions/17686809/how-to-find-word-next-
    to-a-word-in-python
    This was for trying to find a word after a search word. This was
    necessary for searching for the word after hostname and version
    when parsing the configuration file

    3. http://stackoverflow.com/questions/273192/check-if-a-directory-
    exists-and-create-it-if-necessary
    How to create a directory if it doesn't exist already
"""

import tftpy
import glob
import os

def getConnections():
    """ Function prompts the user for the ips of the routers we want
        configuration files from. Returns a list of the ips
    """
    i = 0
    connection = []
    while(True):
        connection.append(raw_input("Enter Management IP (or done):"))
        if connection[i] == "done":
            connection.pop()
            return connection
        i+=1

def check_for_dir():
    """ Checks if the directories exist, create them if necessary
    """
    d = "/home/netman/tmpconf"
    c = "/home/netman/routerconfigs"
    if not os.path.isdir(d):
        print "Creating directory /home/netman/tmpconf..."
        os.makedirs(d)

    if not os.path.isdir(c):
        print "Creating directory /home/netman/routerconfigs..."
        os.makedirs(c)

def getConfigurations(connection):
    """ Acquires the configuration files from each router specified
        using TFTP. Loops through each ip in the list, and saves the
        configuration file in the format: xxx.xxx.xxx.xxx_
    """
    for ips in connection:
        conn = tftpy.TftpClient(ips, 69)
        fname = "/home/netman/tmpconf/" + ips + "_"
        conn.download('/startup-config', fname)

def printInformation(connection):
    """ Once the configuration files are stored in tmpconf, we parse
        them for information to print to the user. The information
        needed is IP address, the IOS version, and the hostname of the
        router.
    """
    for ips in connection:
        fname = "/home/netman/tmpconf/" + ips + "_"
        content = open(fname, 'r').read().split()
        hostname = content[content.index("hostname") + 1]
        version = content[content.index("version") + 1]
        ip_addr = ips
        print ("New config for " + ip_addr + " (" + hostname + ") " +
        "running IOS version " + version)

def isNew(connection):
    """ This function will determine if the config file already exists
        or not. If it doesn't exist, it creates the first version. If it
        does exist, it checks if the files are the same or not. If they
        are the same, do nothing, if they are different, replace and
        increment the version number
    """
    for ips in connection:
        fname = "/home/netman/tmpconf/" + ips + "_"
        fname2 = "/home/netman/routerconfigs/" + ips + "_"
        no_existing_conf = 0
        for name in glob.glob(fname2+"v*"):
            """ Glob is used in this case to find files of the same name as
            the tmpconf file, but with a different version number (using
            the * to match any number after the v). This for loop works
            like an if statement, in that if a file exists in the
            routerconfigs directory with the same name as the tmpconf
            file, then we check if it is an older version or not
            """

            no_existing_conf = name
            # When no_existing_conf is given a value, then it will fail
            # the if statement later which is used to create the first
            # version of a file

            old_conf = open(name, 'r').read()
            new_conf = open(fname, 'r').read()
            if old_conf == new_conf:
                # print "They are the same"
                pass
            else:
                # print "They are not the same"
                create_new_version(fname, fname2, name)
        if no_existing_conf == 0:
            create_v1(fname, fname2)

def create_new_version(fname, fname2, name):
    """ This will be called if there is a previous version of a config
        file inside the routerconfig directory, but the new version has
        some changes so we need to overwrite the file. This function
        will also rename the file with a higher version number to show
        that the new config is a newer version.
    """
    version_number = (int(name.split('_v')[1])+1)
    tmp_config = open(fname, 'r').read()
    old_config = open(name, 'w')
    old_config.write(tmp_config)
    os.rename(name, fname2 + "v" + str(version_number))

def create_v1(fname, fname2):
    """ This function will simply create the version 1 config file for
        the routerconfig directory.
    """
    tmp_config = open(fname, 'r').read()
    first_config = open(fname2 + 'v1', 'w')
    first_config.write(tmp_config)

def main():
    """ Main function, used to call most of the other functions of the
        program. Starts by gettings the ips from the user, then it
        finds their configurations, prints the information to the user,
        and replaces as needed.
    """
    connection = getConnections()
    if not connection:
        print "No IPs entered"
        return
    check_for_dir()
    getConfigurations(connection)
    printInformation(connection)
    isNew(connection)

main()
