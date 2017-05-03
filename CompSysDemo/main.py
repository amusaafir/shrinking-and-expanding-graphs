from algorithm.expanding.expander import *
from algorithm.helper.graph_metrics import *
from io.graph_loader import *
from io.graph_writer import *
from algorithm.expanding.topology.star import *
from algorithm.expanding.topology.line import *

graph_metrics = GraphMetrics()
facebook_graph_src = "datasets/facebook_graph.txt"
astro_graph_src = "datasets/CA-AstroPh_input.txt"
graph_loader = GraphLoader()
input_graph = graph_loader.create_undirected_graph_from_file(facebook_graph_src)
print 'Amount of nodes original (input) graph: ', input_graph.number_of_nodes()
print 'Amount of edges original (input) graph: ', input_graph.number_of_edges()

graph_writer = GraphWriter()
expander = Expander()
expanded_graph = expander.expand(input_graph, 3, LineTopology())
graph_writer.save_edge_list_graph_to_csv(expanded_graph, "expanded_fb_test_line2")

"""
# Ties test for Gephi #
ties = TIES()
sampled_graph = ties.sample(input_graph, 0.6)

graph_writer = GraphWriter()
graph_writer.save_edge_list_graph_to_csv(sampled_graph, "sampled_single_astro_graph")
"""