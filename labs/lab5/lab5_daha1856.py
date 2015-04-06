""" Dallas Hays and Puneet Durve

    Lab 5: Netflow Detective

    References:
    1. http://stackoverflow.com/questions/16772071/sort-dict-by-value-python
    How to sort a dictionary in python
    2. http://stackoverflow.com/questions/17295060/sort-the-top-ten-results
    Get top 10 from sorted result
    3. http://stackoverflow.com/questions/1995615/how-can-i-format-a-
    decimal-to-always-show-2-decimal-places
    How to use the new "".format() to a certain amount of decimal places
"""

import os
import flowd
import sys
from pylab import *
import mark_tools

def TopPorts(flow_log):
    """ Function will analyze a NetFlow file to figure out the top
        Destination Ports that are being used. It will organize the data
        in order starting from the Top port by byte. Then it will cut off
        the top 10 which are then graphed using pyplot tools. It will also
        use the port lookup tool given by Mark to try and determine port
        alias.
    """

    log = flowd.FlowLog(flow_log)
    counter = dict()

    for flow in log:
        # Ensure that the destination is not a local address
        if not flow.dst_addr.startswith('192.168.1'):
            try:
                counter[flow.dst_port] += flow.octets
            except KeyError:
                counter[flow.dst_port] = flow.octets

    # counter_sorted is a list of tuples EX: counter_sorted[0][1]
    counter_sorted = sorted(counter.items(),key=lambda x:x[1], reverse=True)[:10]

    ports = list() # top 10 port list
    octets = list() # top 10 octets list

    for i, (a,b) in enumerate(counter_sorted):
        ports.append(mark_tools.port_service_lookup(a))
        octets.append(b)

    # Pyplot set-up
    figure(1, figsize=(6,6))
    ax = axes()
    colors = ['b','g','r','c','m','y','w','burlywood','chartreuse','grey']
    labels = ports # list of ports
    values = octets # list of octets

    # Outputs to the command line a legend for the pie graph
    printTopTen(labels, values)

    # Generate the pie chart and save it in the current directory
    pie (values, labels=labels, colors=colors, autopct='%1.1f%%')
    ax.set_title("Top 10 Destination Ports")
    savefig('TopPorts.png')
    print "Generated TopPorts.png..."

def TopDestinations(flow_log):
    """ Function will analyze a NetFlow file to figure out the top
        Destination Addresses that are being used. It will organize the data
        in order starting from the Top address by byte. Then it will cut off
        the top 10 which are then graphed using pyplot tools. It will also
        use the reverse dns tool given by Mark to try and determine port
        alias.
    """

    log = flowd.FlowLog(flow_log)
    counter = dict()

    for flow in log:
        if not flow.dst_addr.startswith('192.168.1'):
            try:
                counter[flow.dst_addr] += flow.octets
            except KeyError:
                counter[flow.dst_addr] = flow.octets

    # counter_sorted is a list of tuples EX: counter_sorted[0][1]
    # Change the [:10] of the next line to [1:11] to skip first entry
    counter_sorted = sorted(counter.items(),key=lambda x:x[1], reverse=True)[:10]

    dst_addresses = list() # top 10 address list
    octets = list()        # top 10 octets list

    for i, (a,b) in enumerate(counter_sorted):
        dst_addresses.append(mark_tools.reverse_dns(a))
        octets.append(b)

    # Pyplot set-up
    figure(2, figsize=(6,6))
    ax = axes()
    colors = ['b','g','r','c','m','y','w','burlywood','chartreuse','grey']
    labels = dst_addresses # list of destination addresses
    values = octets # list of octets

    # Ouputs to the command line a legend for the pie graph
    printTopTen(labels, values)

    # Generate the pie chart and save it in the current directory
    pie (values, labels=labels, colors=colors, autopct='%1.1f%%')
    ax.set_title("Top 10 Destination Addresses")
    savefig('TopDestination.png')
    print "Generated TopDestination.png..."

def printTopTen(labels, values):
    """ Function is used to create a legend that will correspond with
        the graphs. This was necessary as some graphs were cut off and
        so having the legend allows the reader to understand the graphs
        better. Prints to the command line.
    """
    sum = 0.0

    for i in values:
        sum += int(i)

    print ""
    print "=========================Top 10========================="
    print "Bytes | Percent of Sum | Port/Address "

    for i in range(len(labels)):
        pct = (values[i]/sum)*100
        print "{0}\t| {1:.1f}%\t| {2}".format(values[i], pct, labels[i])


def chooseFile():
    """ Function will simply ask the user for the NetFlow file to monitor
        and return the name of the file
    """
    print "Files available in directory: \n"+' \n'.join(os.listdir('.'))
    print ""
    while(True):
        input = raw_input("Enter the Netflow file to analyze: ")
        if os.path.isfile(input):
            return input
        else:
            print input, "does not exist in the current directory."


def main():
    input = chooseFile()
    #input = "flowd_capture_1" # For Debugging
    #print input
    TopPorts(input)
    TopDestinations(input)

if __name__ == "__main__":
    main()

