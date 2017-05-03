from topology_structure import *
from algorithm.helper.graph_helper import *
import networkx as nx

class LineTopology(TopologyStructure):
    def link_graphs(self, sampled_graphs):
        expanded_graph = nx.Graph()
        expanded_graph.to_undirected()
        last_added_graph = None
        graph_helper = GraphHelper()

        for graph in sampled_graphs:
            graph_helper.put_nodes_from_original_graph_in_given_graph(graph, expanded_graph)
            graph_helper.put_edges_from_original_graph_in_given_graph(graph, expanded_graph)

            if last_added_graph is not None:
                random_node_from_last_added_graph = graph_helper.get_random_node_from_graph(last_added_graph)
                random_node_target_sampled_graph = graph_helper.get_random_node_from_graph(graph)
                expanded_graph.add_edge(random_node_from_last_added_graph, random_node_target_sampled_graph)

            last_added_graph = graph

        return expanded_graph