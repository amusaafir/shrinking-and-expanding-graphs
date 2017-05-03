from __future__ import absolute_import

import unittest

import networkx as nx


class TestTIES(unittest.TestCase):
    def test_edge_based_node_step(self):
        # Arrange
        ties = TIES()
        graph = nx.Graph()
        graph.to_undirected()
        graph.add_edge(1,2)
        graph.add_edge(1,3)
        graph.add_edge(3,4)
        graph.add_edge(3,8)
        graph.add_edge(4,5)
        graph.add_edge(5,6)
        graph.add_edge(2,6)
        graph.add_edge(6,9)
        graph.add_edge(7,8)
        graph.add_edge(7,10)
        fraction = 0.5

        # Act
        edge_based_node_graph = ties.edge_based_node_step(graph, fraction)

        # Assert
        self.assertTrue(len(edge_based_node_graph.nodes()) == 5 or len(edge_based_node_graph.nodes()) == 6)

    def test_sample(self):
        # Arrange
        ties = TIES()
        graph = nx.Graph()
        graph.to_undirected()
        graph.add_edge(1,2)
        graph.add_edge(1,3)
        graph.add_edge(3,4)
        graph.add_edge(2,5)
        graph.add_edge(4,5)
        graph.add_edge(4,6)
        fraction = 1

        # Act
        sampled_graph = ties.sample(graph, fraction)

        # Assert
        self.assertEqual(len(sampled_graph.nodes()), 6)
        self.assertEqual(len(sampled_graph.edges()), 6)