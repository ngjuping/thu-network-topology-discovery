import os
import re
import networkx as nx
from networkx.readwrite import json_graph
import csv 
import json
import sys
import signal
from optparse import OptionParser

# Initialize the command line parser instance
parser = OptionParser()
parser.add_option("-i", "--input", dest="in_filename",
                  help="read from file for ip to traceroute")
parser.add_option("-o", "--output", dest="out_filename",
                  help="write to file the json for d3js visualization")
parser.add_option("-g", "--group", dest="network_group",
                  help="group for the d3.js nodes")
parser.add_option("--skip", metavar="N", dest="operate_every_n", default=0, help="Traceroute every N ips")

(options, args) = parser.parse_args()

# Get parsed command line argument
in_filename = options.in_filename
out_filename = options.out_filename
network_group = int(options.network_group)
operate_every_n = int(options.operate_every_n)

# Read a series of ips to be traceroute'ed
ip_addrs = csv.reader(open(in_filename,'r'))

# Counter that is used for traceroute every n ips
counter_for_skip = 1

# Temporary file to store the traceroute result
tmp_filename = 'csv%d_tmp.txt' % (network_group)

G = nx.Graph()

def generate_json():
    os.remove(tmp_filename)

    nx_graph_dict = json_graph.node_link_data(G)

    with open(out_filename,"w") as json_save_to_file:
        nx_graph_json = json.dump(nx_graph_dict,json_save_to_file)


for raw_ip in ip_addrs:
    
    # Only perform traceroute every n ips, as specified in the cmd argument
    if(counter_for_skip < operate_every_n):
        counter_for_skip += 1
        continue
    else:
        # Reset counter
        counter_for_skip = 1

    ip = raw_ip[0]
    
    print('tracert ' + ip, end="... ")

    # Prevent OS buffering, otherwise done is printed before os.system(command)
    sys.stdout.flush()

    command = "traceroute -I %s > %s" % (ip,tmp_filename)

    status_code = os.system(command)

    # Ctrl+C pressed
    if status_code == 2:
        generate_json()
        sys.exit(0)

    print('done')

    with open(tmp_filename, 'r') as reader:
        reader.readline()  # Read off heading
        current_ip = ''
        previous_ip = None
        line = reader.readline()
        while( line ):
            match = re.search(r"\(([\d.]+)\)", line)
            if match:
                current_ip = match.group(1)
                if current_ip not in G:
                    G.add_node(current_ip,group=network_group)
                if previous_ip:
                    G.add_edge(previous_ip, current_ip)
                previous_ip = current_ip

            line = reader.readline()

generate_json()

