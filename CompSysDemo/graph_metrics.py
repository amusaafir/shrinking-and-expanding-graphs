import networkx as nx

class GraphMetrics:
    # Just to test whether the loader works we calculate the average degree and compare it with the result from Gephi #
    def calculate_average_degree(self, graph):
        total_degree = 0

        for key in nx.degree(graph):
            total_degree += nx.degree(graph)[key]

        avg_deg = float(total_degree) / float(graph.number_of_nodes())

        print 'Average degree: ', avg_deg