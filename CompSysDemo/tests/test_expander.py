from __future__ import absolute_import

import unittest

import networkx as nx
from algorithm.expanding.expander import *


class TestTIES(unittest.TestCase):
    def test_convert_graph_to_indicated(self):
        # Arrange
        expander = Expander()

        graph = nx.Graph()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        # Act
        indicated_graph = expander.convert_graph_to_indicated(graph, "a")

        # Assert
        self.assertEqual(len(indicated_graph.nodes()), 3)
        self.assertEqual(len(indicated_graph.edges()), 3)
        for node in indicated_graph.nodes():
            self.assertTrue(node.startswith('a'))

    def test_sample_graphs(self):
        # Arrange
        expander = Expander()

        graph = nx.Graph()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        # Act
        sampled_graphs = expander.sample_graphs(graph, 3)

        # Assert
        self.assertEqual(len(sampled_graphs), 5)

    """def test_expand(self):
        # Arrange
        expander = Expander()

        graph = nx.Graph()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)

        # Act
        expanded_graph = expander.expand(graph, 3)

        # Assert
        print 'Length:',len(expanded_graph.nodes())
    """