import networkx as nx
import random
import copy

"""
Total-Induced Edge Sampling (TIES): http://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=2743&context=cstech
"""

class TIES:
    def sample(self, graph, fraction):
        sampled_vertices = self.edge_based_node_step(graph, fraction)
        self.induction_step(graph, sampled_vertices)

        return None

    def edge_based_node_step(self, graph, fraction):
        max_amount_of_sampled_nodes = self.get_max_amount_of_sampled_nodes(graph, fraction)
        working_graph = copy.deepcopy(graph)
        vertices_set = set()

        while len(vertices_set) < max_amount_of_sampled_nodes:
            random_edge_index = random.randint(0, working_graph.number_of_edges())

            edge = working_graph.edges()[random_edge_index]
            vertices_set.add(edge[0])
            vertices_set.add(edge[1])
            working_graph.remove_edge(edge[0], edge[1])
            print 'Collected ', len(vertices_set), ' vertices.'

        print 'Edge based node step finished. Collected a total of ', len(vertices_set), ' vertices.'

        return None

    def induction_step(self, graph, sampled_vertices):
        return None

    def get_max_amount_of_sampled_nodes(self, graph, fraction):
        return int(round(fraction * graph.number_of_nodes()))
