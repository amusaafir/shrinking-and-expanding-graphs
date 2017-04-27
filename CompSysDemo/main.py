from graph_loader import *

class GraphMetrics:
    # Just to test whether the loader works we calculate the average degree and compare it with the result from Gephi #
    def calculate_average_degree(self, graph):
        total_degree = 0

        for key in nx.degree(graph):
            total_degree += nx.degree(graph)[key]

        avg_deg = float(total_degree) / float(graph.number_of_nodes())

        print 'Average degree: ', avg_deg

graph_metrics = GraphMetrics()
graph_src_path = "datasets/facebook_graph.txt"
GraphLoader = GraphLoader()
facebook_graph = GraphLoader.create_undirected_graph_from_file(graph_src_path)
graph_metrics.calculate_average_degree(facebook_graph)