# Graph expanding using sampling (TIES)

This expanding algorithm uses TIES as the sampling algorithm.

**How to run**

Run `main.py`. *Note: if you want to change the default expanding size (currently set as `3`), you also need to provide how many sampled graphs you want. This process will be later automated.*

## First results (CompSys)

**Dataset**

The following *undirected* Facebook graph from SNAP was used for the following results (edges from all egonets combined): https://snap.stanford.edu/data/egonets-Facebook.html. This graph was expanded times `3`, with a fraction size of `0.6` for `5` sampled versions of the original graph.

The output (expanded) graph can be found in `CompSysDemo/graph_output/expanded_fb_graph_28-04-2017 04-47-51.csv`

**Result: analyzing the expanded output file using Gephi**

|| Original Facebook Graph | Sampled version (1 version using TIES). Fraction = 0.5)| Expanded version - 3 times using TIES and the star topology structure. Sampled 5 different versions of the graph using a fraction of 0.6 of the original graph and connected them using the star structure. |
|:-------|:------------------------|:------------------------------------------------------:|:-----:|
| Amount of nodes |4039| 2020 | 12115 |
| Amount of edges | 88234 | 55633 | 336103 |
| Average degree | 43.691 | 55.082 | 55.485 |
| Network diameter | 8 | 6 | 20 |
| Graph density | 0.011 | 0.027 | 0.005 |
| Connected components | 1 | 5 | 3 |
| Avg. Clustering Coefficient | 0.617 | 0.643 | 0.628 |
| Avg. Path Length | 3.693 | 3.462 | 9.596 |
