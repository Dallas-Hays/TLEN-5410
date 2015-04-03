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

    #i = 0
    for flow in log:
        if not flow.dst_addr.startswith('192.168.1'):
            #print flow.dst_addr, flow.src_port, flow.dst_port, mark_tools.port_service_lookup(flow.dst_port)

            try:
                counter[flow.dst_port] += flow.octets
            except KeyError:
                counter[flow.dst_port] = flow.octets


            #i += 1
            #if i >= 100:
            #    break

    # counter_sorted is a list of tuples EX: counter_sorted[0][1]
    counter_sorted = sorted(counter.items(),key=lambda x:x[1], reverse=True)[:10]
    print counter_sorted

    ports = list()
    octets = list()

    for i, (a,b) in enumerate(counter_sorted):
        print a, b
        ports.append(mark_tools.port_service_lookup(a))
        octets.append(b)

    figure(1, figsize=(7,7))
    ax = axes()
    colors = ['b','g','r','c','m','y','w','burlywood','chartreuse','grey']
    labels = ports # list of ports
    values = octets # list of octets
    pie (values, labels=labels, colors=colors, autopct='%1.0f%%')
    savefig('pie1.png')


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






if __name__ == "__main__":
    main()

