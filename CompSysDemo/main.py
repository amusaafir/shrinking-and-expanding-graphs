from algorithm.expanding.expander import *
from io.graph_loader import *
from io.graph_writer import *
from algorithm.expanding.topology.star import *
from algorithm.expanding.topology.line import *

class Main():
    def __init__(self):
        self.graph_writer = GraphWriter()

    def run_sampling(self, input_graph_src, output_file_name, fraction):
        input_graph = self.create_undirected_graph_from_file(input_graph_src)
        ties = TIES()
        sampled_graph = ties.sample(input_graph, fraction)
        self.graph_writer.save_edge_list_graph_to_csv(sampled_graph, output_file_name)

    def run_expanding(self, input_graph_src, output_file_name):
        input_graph = self.create_undirected_graph_from_file(input_graph_src)
        expander = Expander()
        expanded_graph = expander.expand(input_graph, 3, LineTopology())
        self.graph_writer.save_edge_list_graph_to_csv(expanded_graph, output_file_name)

    def create_undirected_graph_from_file(self, input_file):
        graph_loader = GraphLoader()
        input_graph = graph_loader.create_undirected_graph_from_file(input_file)
        print 'Amount of nodes original (input) graph: ', input_graph.number_of_nodes()
        print 'Amount of edges original (input) graph: ', input_graph.number_of_edges()

        return input_graph

main = Main()
facebook_graph_src = "datasets/facebook_graph.txt"
astro_graph_src = "datasets/CA-AstroPh_input.txt"
ca_hepph_src = "datasets/CA-HepPh.txt"

#main.run_sampling(facebook_graph_src, "sampled_fb_file", 0.6)
main.run_expanding(facebook_graph_src, "expanded_fb_file")