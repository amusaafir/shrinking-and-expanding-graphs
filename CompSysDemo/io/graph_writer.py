import time

class GraphWriter:
    def save_edge_list_graph_to_csv(self, graph):
        sampled_output = "sampled_output\\sampled_graph_" + time.strftime("%d-%m-%Y %I-%M-%S") + ".csv"
        output_file = open(sampled_output, "w")

        output_file.write("Source Target\n")

        for edge in graph.edges():
            output_file.write(str(edge[0]) + " " + str(edge[1]) + "\n")

        output_file.close()