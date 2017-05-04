from topology_structure import *
from algorithm.helper.graph_helper import *
import networkx as nx

class StarTopology(TopologyStructure):
    def link_graphs(self, sampled_graphs):
        expanded_graph = nx.Graph()
        expanded_graph.to_undirected()
        centerGraph = None
        graph_helper = GraphHelper()

        for graph in sampled_graphs:
            graph_helper.put_nodes_from_original_graph_in_given_graph(graph, expanded_graph)
            graph_helper.put_edges_from_original_graph_in_given_graph(graph, expanded_graph)

            if centerGraph is None: # Add center graph
                centerGraph = graph
                continue

            # Pick a random node from the center graph and target graph
            randomNodeSource = graph_helper.get_random_node_from_graph(centerGraph)
            randomNodeTarget = graph_helper.get_random_node_from_graph(graph)

            # Link it inside the expanded graph
            expanded_graph.add_edge(randomNodeSource, randomNodeTarget)

        return expanded_graph

    def link_graphs_control_links(self, sampled_graphs, number_of_nodes_target):
        expanded_graph = nx.Graph()
        expanded_graph.to_undirected()
        centerGraph = None
        graph_helper = GraphHelper()

        for graph in sampled_graphs:
            graph_helper.put_nodes_from_original_graph_in_given_graph(graph, expanded_graph)
            graph_helper.put_edges_from_original_graph_in_given_graph(graph, expanded_graph)
            amount_of_links_per_connection = nx.number_of_nodes(graph) #int(nx.number_of_nodes(graph) * amount_of_links_fraction)

            if centerGraph is None: # Add center graph
                centerGraph = graph
                continue

            target_graph_nodes = graph.nodes()
            center_graph_nodes = centerGraph.nodes()

            for i in range(0, amount_of_links_per_connection-1):
                # Pick a random node from the center graph and target graph
                randomNodeSource = center_graph_nodes[i]

                for x in range(0, number_of_nodes_target):
                    randomNodeTarget = target_graph_nodes[x]
                    # Link it inside the expanded graph
                    expanded_graph.add_edge(randomNodeSource, randomNodeTarget)

        return expanded_graph