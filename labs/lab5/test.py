"""
	Class notes
"""

import flowd
from pylab import *

log = flowd.FlowLog('flowd_capture_1')
counter = dict()

for flow in log:
    #print dir(flow)
    print flow.src_addr, flow.octets

    """
    shortest line
    counter[flow.src_addr] = counter.get(flow.src_addr, 0) + flow.octets
    """

    try:
        counter[flow.src_addr] += flow.octets
    except KeyError:
        counter[flow.src_addr] = flow.octets

    """
    worse way
    if flow.src_addr in counter:
        counter[flow.src_addr] += flow.octets
    else:
        counter[flow.src_addr] = flow.octets
    """

figure(1, figsize=(6,6))
ax = axes()
labels = counter.keys() # list of keys
values = counter.values() # list of values
pie (values, labels=labels, autopct='%1.0f%%')
savefig('test_pie.png')
