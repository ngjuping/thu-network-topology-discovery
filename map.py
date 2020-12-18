import os
import re
import networkx as nx
from networkx.readwrite import json_graph
import csv 
import json
import sys

# First argument(x) = n-th network block
# Second argument(n) = read once every x traversed

file_name = sys.argv[1]
network_group = int(sys.argv[2])
ip_addrs = csv.reader(open(file_name,'r'))

# 每n个跳过
operate_every_n = int(sys.argv[3])
counter_for_skip = 1

# Data for testing
# targets = ['101.5.224.77','101.5.3.33','166.111.79.129','166.111.68.150','59.66.217.10','59.66.212.8','118.229.25.226']

G = nx.Graph()

for raw_ip in ip_addrs:

    # Only perform traceroute every n, as specified in the cmd argument
    if(counter_for_skip < operate_every_n):
        counter_for_skip += 1
        continue

    # Reset counter
    counter_for_skip = 1

    ip = raw_ip[0]
    command = "traceroute -I %s > data.txt" % (ip)
    os.system(command)

    print('tracert ' + ip + ' done')

    with open('data.txt', 'r') as reader:
        reader.readline()  # Read off heading
        current_ip = ''
        previous_ip = None
        line = reader.readline()
        while( line ):
            x = re.search(r"\(([\d.]+)\)", line)
            if x:
                current_ip = x.group(1)
                # print(current_ip)
                if current_ip not in G:
                    G.add_node(current_ip,group=network_group)
                if previous_ip:
                    G.add_edge(previous_ip, current_ip)
                previous_ip = current_ip

            line = reader.readline()

nx_graph_dict = json_graph.node_link_data(G)

with open("data_for_d3js.json","w") as json_save_to_file:
    nx_graph_json = json.dump(nx_graph_dict,json_save_to_file)

