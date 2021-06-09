import dynetx as dn
import csv
import matplotlib.pyplot as plt
#import networkx as nx

# create the network directed time depend graph
G = dn.DynDiGraph()

path_plot = './figures/'

with open('manunited_cont.csv', mode ='r') as file:
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for nodes in csvFile:
        node_out = int(nodes[0])
        node_in = int(nodes[1])
        timestamp = int(nodes[2])
        G.add_node(node_out)
        G.add_node(node_in)
        G.add_interaction(node_out, node_in, t=timestamp)

# find in - out nodes degrees
# no matter dublicate nodes pair in same timestamp
node_max_degree_out = 0
node_max_degree_in = 0
max_out_degree = 0
max_in_degree = 0

for node in G.nodes():
    print('The out degree of node ', node, ' is : ', G.out_degree(node))
    print('The in degree of node ', node, ' is : ', G.in_degree(node))
    print()
    if G.out_degree(node) >= max_out_degree:
        max_out_degree = G.out_degree(node)
        node_max_degree_out = node
    if G.in_degree(node) >= max_in_degree:
        max_in_degree = G.in_degree(node)
        node_max_degree_in = node
    print('----------')

print('The node ', node_max_degree_out, ' has the max out degree  : ', max_out_degree)
print('The node ', node_max_degree_in, ' has tha max in degree : ', max_in_degree)

#https://pypi.org/project/pathpy2/
print('----------')
#print(G.temporal_snapshots_ids())

k = G.edges()
print(k)

x = G.interactions_per_snapshots()

for value in x.keys():
    y = x[value]
    #print(y)









# giant
"""previous_max_interactions = 0
for timestamp in G.temporal_snapshots_ids():
    if previous_max_interactions <= G.number_of_interactions(t=timestamp):
        previous_max_interactions = G.number_of_interactions(t=timestamp)
        current_timestamp = timestamp

print(previous_max_interactions)
print(current_timestamp)"""


# max nodes in timestamp
"""max_nodes = 0
for timestamp in G.temporal_snapshots_ids(): # list with unique snapshot
    current_max = dn.number_of_nodes(G, timestamp)
    if current_max >= max_nodes:
        max_nodes = current_max
        current_timestamp = timestamp

print(max_nodes)
print(current_timestamp)"""




x = [1,2,3]
y = [2,4,1]

plt.plot(x,y)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('the graph')

#plt.show()
plt.savefig(path_plot + 'foo.pdf')