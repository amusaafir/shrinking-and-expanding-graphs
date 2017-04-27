from graph_loader import *
from graph_metrics import *
from ties import *

graph_metrics = GraphMetrics()
graph_src_path = "datasets/facebook_graph.txt"
graph_loader = GraphLoader()
facebook_graph = graph_loader.create_undirected_graph_from_file(graph_src_path)
#graph_metrics.calculate_average_degree(facebook_graph)
ties = TIES()
print 'Amount of nodes: ', facebook_graph.number_of_nodes()
ties.sample(facebook_graph, 0.1)