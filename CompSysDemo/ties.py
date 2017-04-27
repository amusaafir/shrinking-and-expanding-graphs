import networkx as nx
import random
import copy

"""
Total-Induced Edge Sampling (TIES): http://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=2743&context=cstech
"""

class TIES:
    def sample(self, graph, fraction):
        edge_based_node_graph = self.edge_based_node_step(graph, fraction)
        sampled_graph = self.induction_step(graph, edge_based_node_graph)

        return sampled_graph

    def edge_based_node_step(self, graph, fraction):
        max_amount_of_sampled_nodes = self.get_max_amount_of_sampled_nodes(graph, fraction)
        working_graph = copy.deepcopy(graph)
        graph = nx.Graph()
        graph.to_undirected() # set by default to undirected for now

        while len(graph.nodes()) < max_amount_of_sampled_nodes:
            random_edge_index = random.randint(0, working_graph.number_of_edges()-1)
            edge = working_graph.edges()[random_edge_index]
            graph.add_node(edge[0])
            graph.add_node(edge[1])
            working_graph.remove_edge(edge[0], edge[1])
            print 'Collected ', len(graph.nodes()), ' vertices.'

        print 'Edge based node step finished. Collected a total of ', len(graph.nodes()), ' vertices.'

        return graph

    def induction_step(self, graph, edge_based_node_graph):
        for edge in graph.edges():
            if (edge[0] in edge_based_node_graph.nodes()) and (edge[1] in edge_based_node_graph.nodes()):
                edge_based_node_graph.add_edge(edge[0], edge[1])

        print 'Induction step finished. Added ', len(edge_based_node_graph.edges()), ' edges.'

        return edge_based_node_graph

    def get_max_amount_of_sampled_nodes(self, graph, fraction):
        return int(round(fraction * graph.number_of_nodes()))
