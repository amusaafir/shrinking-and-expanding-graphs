import time

class GraphWriter:
    def save_edge_list_graph_to_csv(self, graph, file_name):
        sampled_output = "graph_output\\" + file_name + "_" + time.strftime("%d-%m-%Y %I-%M-%S") + ".csv"
        output_file = open(sampled_output, "w")

        output_file.write("Source Target\n")

        for edge in graph.edges():
            output_file.write(str(edge[0]) + " " + str(edge[1]) + "\n")

        output_file.close()