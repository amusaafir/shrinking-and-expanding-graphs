from io.graph_loader import *
from io.graph_writer import *
from expander import *
from graph_metrics import *
import networkx as nx

graph_metrics = GraphMetrics()
graph_src_path = "datasets/facebook_graph.txt"
graph_loader = GraphLoader()
facebook_graph = graph_loader.create_undirected_graph_from_file(graph_src_path)
print 'Amount of nodes original (input) graph: ', facebook_graph.number_of_nodes()
print 'Amount of edges original (input) graph: ', facebook_graph.number_of_edges()

"""ties = TIES()
sampled_graph = ties.sample(facebook_graph, 0.1)

graph_writer = GraphWriter()
graph_writer.save_edge_list_graph_to_csv(sampled_graph, "sampled_graph")
"""

# Expanding test for Gephi #
graph = nx.Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)

expander = Expander()
expanded_graph = expander.expand(graph, 3)

graph_writer = GraphWriter()
graph_writer.save_edge_list_graph_to_csv(expanded_graph, "expanded_graph")