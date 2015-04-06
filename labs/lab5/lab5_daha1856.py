""" Dallas Hays

    References:
    1. http://stackoverflow.com/questions/16772071/sort-dict-by-value-python
    How to sort a dictionary in python
    2. http://stackoverflow.com/questions/17295060/sort-the-top-ten-results
    Get top 10 from sorted result
"""

import os
import flowd
import sys
from pylab import *
import mark_tools

def TopPorts(flow_log):
    """ Top dstports
    """

    log = flowd.FlowLog(flow_log)
    counter = dict()

    for flow in log:
        if not flow.dst_addr.startswith('192.168.1'):
            try:
                counter[flow.dst_port] += flow.octets
            except KeyError:
                counter[flow.dst_port] = flow.octets

    # counter_sorted is a list of tuples EX: counter_sorted[0][1]
    counter_sorted = sorted(counter.items(),key=lambda x:x[1], reverse=True)[:10]

    ports = list()
    octets = list()

    for i, (a,b) in enumerate(counter_sorted):
        ports.append(mark_tools.port_service_lookup(a))
        octets.append(b)

    figure(1, figsize=(6,6))
    ax = axes()
    colors = ['b','g','r','c','m','y','w','burlywood','chartreuse','grey']
    labels = ports # list of ports
    values = octets # list of octets

    printTopTen(labels, values)

    pie (values, labels=labels, colors=colors, autopct='%1.1f%%')

    ax.set_title("Top 10 Destination Ports")
    savefig('TopPorts.png')
    print "Generated TopPorts.png..."

def TopDestinations(flow_log):
    """ Top dstports
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
    # Change the [:10] of the next line to [1:11] to skip first value
    counter_sorted = sorted(counter.items(),key=lambda x:x[1], reverse=True)[:10]

    dst_addresses = list()
    octets = list()

    for i, (a,b) in enumerate(counter_sorted):
        dst_addresses.append(mark_tools.reverse_dns(a))
        octets.append(b)

    figure(2, figsize=(6,6))
    ax = axes()
    colors = ['b','g','r','c','m','y','w','burlywood','chartreuse','grey']
    labels = dst_addresses # list of destination addresses
    values = octets # list of octets

    printTopTen(labels, values)

    pie (values, labels=labels, colors=colors, autopct='%1.1f%%')

    ax.set_title("Top 10 Destination Addresses")
    savefig('TopDestination.png')
    print "Generated TopDestination.png..."

def printTopTen(labels, values):
    """
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
    print "Files available in directory: \n"+' \n'.join(os.listdir('.'))
    print ""
    while(True):
        input = raw_input("Enter the Netflow file to analyze: ")
        if os.path.isfile(input):
            return input
        else:
            print input, "does not exist in the current directory."


def main():
    #input = chooseFile()
    input = "flowd_capture_1"
    print input
    TopPorts(input)
    TopDestinations(input)

if __name__ == "__main__":
    main()

