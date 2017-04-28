import networkx as nx
from string import ascii_lowercase
from ties import *
from string import ascii_lowercase

class Expander:
    def expand(self, graph, improper_fraction):
        sampled_graphs = self.sample_graphs(graph, improper_fraction)

        return None

    def sample_graphs(self, graph, improper_fraction):
        # Hardcoded sampling size at the moment: 5 different sampled graphs - fraction: 0.6 if improper fraction = 3#
        amount_of_sampled_graphs = 5
        sampling_fraction = float(improper_fraction) / float(amount_of_sampled_graphs)
        sampled_graphs = set()
        ties = TIES()

        for graph_indicator in range(0, amount_of_sampled_graphs):
            indicated_graph = self.convert_graph_to_indicated(graph, ascii_lowercase[graph_indicator])
            sampled_graphs.add(ties.sample(indicated_graph, sampling_fraction))

        return sampled_graphs


    def link_graphs_using_star(self, graphs):
        graph = nx.Graph()
        graph.to_undirected()

    # Add an indicator to the graph so that we can have separate sampled graphs that have different nodes#
    def convert_graph_to_indicated(self, graph, indicator):
        indicated_graph = nx.Graph()
        indicated_graph.to_undirected()

        for node in graph.nodes():
            indicated_graph.add_node(indicator + str(node))

        for edge in graph.edges():
            indicated_graph.add_edge(indicator + str(edge[0]), indicator + str(edge[1]))

        return indicated_graph