import networkx as nx
import random
import copy

"""
Total-Induced Edge Sampling (TIES): http://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=2743&context=cstech
"""

class TIES:
    def sample(self, input_graph, fraction):
        edge_based_node_graph = self.edge_based_node_step(input_graph, fraction)
        sampled_graph = self.induction_step(input_graph, edge_based_node_graph)

        return sampled_graph

    def edge_based_node_step(self, input_graph, fraction):
        max_amount_of_sampled_nodes = self.get_max_amount_of_sampled_nodes(input_graph, fraction)
        working_graph = copy.deepcopy(input_graph)
        graph = nx.Graph()
        graph.to_undirected() # set by default to undirected for now

        working_graph_edges = working_graph.edges()

        while nx.number_of_nodes(graph) < max_amount_of_sampled_nodes:
            random_edge_index = random.randint(0, len(working_graph_edges)-1)
            edge = working_graph_edges[random_edge_index]
            graph.add_node(edge[0])
            graph.add_node(edge[1])
            del working_graph_edges[random_edge_index]

        print 'Edge based node step finished. Collected a total of ', nx.number_of_nodes(graph), ' vertices.'

        return graph

    def induction_step(self, graph, edge_based_node_graph):
        edge_based_graph_nodes = edge_based_node_graph.nodes()
        for edge in graph.edges():
            if (edge[0] in edge_based_graph_nodes) and (edge[1] in edge_based_graph_nodes):
                edge_based_node_graph.add_edge(edge[0], edge[1])

        print 'Induction step finished. Added ', len(edge_based_node_graph.edges()), ' edges.'

        return edge_based_node_graph

    def get_max_amount_of_sampled_nodes(self, graph, fraction):
        return int(round(fraction * graph.number_of_nodes()))
