import networkx as nx

class GraphLoader:
    def __init__(self):
        print 'Graph loader initialized.'

    def create_undirected_graph_from_file(self, path):
        graph = nx.Graph()
        graph.to_undirected()

        for line in open(path):
            current_line = line.rstrip()
            edges = current_line.split()
            graph.add_edge(edges[0], edges[1])

        return graph