import dynetx as dn
import csv
import matplotlib.pyplot as plt

# Define variables
PATH_TO_DATASET = 'manunited_cont.csv'
PATH_TO_PLOT = './figures/'


################################################################
# find in - out nodes degrees, no average
# no matter dublicate nodes pair in same timestamp
def find_degree(graph):

    node_max_degree_out = 0
    node_max_degree_in = 0
    max_out_degree = 0
    max_in_degree = 0

    # find in-out degree per node
    for node in graph.nodes():
        print('The out degree of node ', node, ' is : ', graph.out_degree(node))
        print('The in degree of node ', node, ' is : ', graph.in_degree(node))
        print()
        if graph.out_degree(node) >= max_out_degree:
            max_out_degree = graph.out_degree(node)
            node_max_degree_out = node
        if graph.in_degree(node) >= max_in_degree:
            max_in_degree = graph.in_degree(node)
            node_max_degree_in = node
        print('----------')

    # which node has max in or max out degree
    print('The node ', node_max_degree_out, ' has the max out degree  : ', max_out_degree)
    print('The node ', node_max_degree_in, ' has tha max in degree : ', max_in_degree)
    print('----------')
################################################################

################################################################
# max number of edges for specific timestamp
def max_edges_timestamp(graph):
    previous_max = 0
    snap_dict = graph.interactions_per_snapshots()
    for value in snap_dict.keys():
        current_max = snap_dict[value]
        if previous_max <= current_max:
            previous_max = current_max
            current_timestamp = timestamp

    print("Max count of edges ", int(previous_max), " exist at timestamp ", current_timestamp)
    print('----------')

################################################################

# create the network directed time depend graph
G = dn.DynDiGraph(edge_removal=True)

################################################################
# open and read dataset file
with open(PATH_TO_DATASET, mode ='r') as file:
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for nodes in csvFile:
        source = int(nodes[0])
        target = int(nodes[1])
        timestamp = int(nodes[2])
        # G.add_node(source)
        # G.add_node(target)
        # add edges and nodes per timestamp
        G.add_interaction(source, target, t=timestamp)

################################################################

find_degree(G)
max_edges_timestamp(G)
