import networkx as nx
from string import ascii_lowercase
from ties import *
from string import ascii_lowercase
import random

class Expander:
    def expand(self, graph, improper_fraction):
        sampled_graphs = self.sample_graphs(graph, improper_fraction)
        expanded_graph = self.link_graphs_using_star(sampled_graphs)

        return expanded_graph

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

    def link_graphs_using_star(self, sampled_graphs):
        expanded_graph = nx.Graph()
        expanded_graph.to_undirected()
        centerGraph = None

        for graph in sampled_graphs:
            self.put_nodes_from_original_graph_in_given_graph(graph, expanded_graph)
            self.put_edges_from_original_graph_in_given_graph(graph, expanded_graph)

            if centerGraph is None: # Add center graph
                centerGraph = graph
                continue

            # Pick a random node from the center graph and target graph
            randomNodeSource = self.get_random_node_from_graph(centerGraph)
            randomNodeTarget = self.get_random_node_from_graph(graph)

            # Link it inside the expanded graph
            expanded_graph.add_edge(randomNodeSource, randomNodeTarget)

        return expanded_graph

    def put_nodes_from_original_graph_in_given_graph(self, original_graph, given_graph):
        for original_node in original_graph.nodes():
            given_graph.add_node(original_node)

    def put_edges_from_original_graph_in_given_graph(self, original_graph, given_graph):
        for original_edge in original_graph.edges():
            given_graph.add_edge(*original_edge)

    def get_random_node_from_graph(self, graph):
        return graph.nodes()[random.randint(0, graph.number_of_nodes() - 1)]

    # Add an indicator to the graph so that we can have separate sampled graphs that have different nodes#
    def convert_graph_to_indicated(self, graph, indicator):
        indicated_graph = nx.Graph()
        indicated_graph.to_undirected()

        for node in graph.nodes():
            indicated_graph.add_node(indicator + str(node))

        for edge in graph.edges():
            indicated_graph.add_edge(indicator + str(edge[0]), indicator + str(edge[1]))

        return indicated_graph