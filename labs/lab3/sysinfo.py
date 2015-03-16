""" Dallas Hays
    Lab 3
    3/6/15

    TO USE:
        1. Run this program and go to localhost:5000/ in a browser
        2. Add an IP address to the list with the text box
        3. Select an IP address from the drop down to see its monitor page

    Community String in use: public

    References:
    1. http://stackoverflow.com/questions/423379/using-global-variables-
    in-a-function-other-than-the-one-that-created-them
    How to use global variables
    2.  http://stackoverflow.com/questions/13279399/how-to-obtain-values-
    of-request-variables-using-python-and-flask
    The difference in getting variable information from POST vs GET
    3. W3Schools
    For pretty much all of my HTML/CSS knowledge

"""
import myrouter
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
ips = []     # Global List of IP addresses being monitored
ip = ''      # Global variable for the current IP address
ref_val = 60 # Initial refresh value is 60 seconds

@app.route('/', methods=['GET', 'POST'])
def iplist():
    """ Homepage: Allows the user to add an IP address to the list, then
        it will add the IP to the global 'ips' list
    """
    global ip
    if request.method == 'POST':
        if request.form['ipaddr'] != '':
            ip = request.form['ipaddr']
            if ip not in ips:
                ips.append(ip)
    return render_template('iplist.html', ips=ips)

@app.route("/update", methods=['POST'])
def update():
    """ This page is called whenever an update to the monitor page is
        submitted. This includes updating the hostname, contact, location,
        and refresh values.

        Uses functions from myrouter.py

        Obtains the value of ipaddr-list from the monitor page, which
        corresponds to an ip address in the ips list. Uses this to make
        changes.
    """
    global ref_val # global so we can make changes to the global variable
    i = ips.index(request.form['address'])
    url = '/monitor?ipaddr-list=' + str(i)

    r1 = myrouter.Router(request.form['address'], 'public')

    modification = request.form['modification']
    mod = request.form['mod']

    if modification == 'hostname':
        r1.set_hostname(mod)
    if modification == 'contact':
        r1.set_contact(mod)
    if modification == 'location':
        r1.set_location(mod)
    if modification == 'refresh_value':
        if int(mod) > 0:
            ref_val = mod

    return redirect(url)

@app.route('/monitor', methods=['GET', 'POST'])
def monitor():
    """ POST: Will add the ip address to the list, and then reload the
        homepage.

        GET: Will load the monitor page, and use the getters of myrouter.py
        to display the SNMP information to the user.
    """
    global ip

    if request.method == 'GET':
        i = int(request.args.get('ipaddr-list'))
        r1 = myrouter.Router(ips[i], 'public')

    ### Variables that are used in the monitor.html page ###############
        hostname = r1.get_hostname()
        contact = r1.get_contact()
        location = r1.get_location()
        uptime = r1.get_uptime()
        cdp_neighbors_hostnames = r1.get_cdpneighbors_hostname()
        cdp_neighbors_len = len(r1.get_cdpneighbors_hostname())
        cdp_neighbors_interfaces = r1.get_cdpneighbors_interface()
        route_table_dest = r1.get_routetable_dest()
        route_table_mask =r1.get_routetable_mask()
        route_table_nexthop = r1.get_routetable_nexthop()
        route_table_metric = r1.get_routetable_metric()
        route_table_len = len(route_table_dest)
        ip = ips[i]
    ####################################################################

    # Many variables are passed in for Jinja to display on the html page
        return render_template('monitor.html',
                        ips=ips,
                        hostname=hostname,
                        contact=contact,
                        location=location,
                        uptime=uptime,
                        cdp_neighbors_hostnames=cdp_neighbors_hostnames,
                        cdp_neighbors_len=cdp_neighbors_len,
                        cdp_neighbors_interfaces=cdp_neighbors_interfaces,
                        route_table_dest=route_table_dest,
                        route_table_mask=route_table_mask,
                        route_table_nexthop=route_table_nexthop,
                        route_table_metric=route_table_metric,
                        route_table_len=route_table_len,
                        ref_val=ref_val,
                        ip=ip)

if __name__ == '__main__':
    app.run(debug=True)
