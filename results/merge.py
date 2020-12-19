import glob
import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--output", dest="out_filename",
                  help="save merged json to file")

(options, args) = parser.parse_args()
out_filename = options.out_filename

json_files = []
for file in glob.glob("*.json"):
    if(file == out_filename):
        continue
    json_files.append(file)

finaldict = None

def addToFinal(new_node):

    global finaldict
    if new_node['group'] == 'local':
        return

    # Indicate if the new node ip exists
    ip_exists = False

    # The final node collection
    nodes = finaldict.get('nodes')

    # Core logic
    for node in nodes:
        if node['id'] == new_node['id']:
            ip_exists = True
            if node['group'] == 0:
                node['group'] = new_node['group']
                
    if not ip_exists:
        finaldict['nodes'].append(new_node)

for jsonfile in json_files:
    with open(jsonfile,'r') as ojsonfile:
        jsondict = json.load(ojsonfile)
        if finaldict is None:
            finaldict = jsondict
        else:
            currdict_nodes = jsondict.get("nodes")
            for node in currdict_nodes:
                addToFinal(node)

        finaldict["links"].extend(jsondict.get("links"))
            
        
with open(out_filename,'w') as outfile:
    json.dump(finaldict,outfile)
