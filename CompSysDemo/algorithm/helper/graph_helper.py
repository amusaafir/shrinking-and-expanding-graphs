import random

class GraphHelper:
    def put_nodes_from_original_graph_in_given_graph(self, original_graph, given_graph):
        for original_node in original_graph.nodes():
            given_graph.add_node(original_node)

    def put_edges_from_original_graph_in_given_graph(self, original_graph, given_graph):
        for original_edge in original_graph.edges():
            given_graph.add_edge(*original_edge)

    def get_random_node_from_graph(self, graph):
        return graph.nodes()[random.randint(0, graph.number_of_nodes() - 1)]