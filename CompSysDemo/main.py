from io.graph_loader import *
from io.graph_writer import *
from expander import *
from graph_metrics import *
import networkx as nx

graph_metrics = GraphMetrics()
facebook_graph_src = "datasets/facebook_graph.txt"
email_enron_graph_src = "datasets/Email-Enron.csv"
graph_loader = GraphLoader()
input_graph = graph_loader.create_undirected_graph_from_file(facebook_graph_src)
print 'Amount of nodes original (input) graph: ', input_graph.number_of_nodes()
print 'Amount of edges original (input) graph: ', input_graph.number_of_edges()

graph_writer = GraphWriter()
expander = Expander()
facebook_expanded_graph = expander.expand(input_graph, 3)
graph_writer.save_edge_list_graph_to_csv(facebook_expanded_graph, "expanded_fb_graph_new")

"""
# Ties test for Gephi #
ties = TIES()
sampled_graph = ties.sample(input_graph, 1)

graph_writer = GraphWriter()
graph_writer.save_edge_list_graph_to_csv(sampled_graph, "sampled_single_fb_graph_new")
"""

"""
# Expanding test for Gephi #
graph = nx.Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)

expander = Expander()
expanded_graph = expander.expand(graph, 3)
"""