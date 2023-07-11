import numpy as np
from random import random
from igraph import *
import pandas as pd
def read_graph(data_file_path, direct=False, multiple_e=False, weighted=False):
    """
    Read graph from file and remove self-loops, multiple edges, and nodes with zero edges.

    Returns igraph Graph object.
    """

    extension = data_file_path.split('.')[-1]

    if extension == "graphml":
        G = Graph.Read_GraphML(data_file_path, directed=direct)
    elif extension == "txt" or extension == 'edgelist':
        G = Graph.Read_Edgelist(data_file_path, directed=direct)
    elif extension == "csv":
        dataframe = pd.read_csv(data_file_path)
        G = Graph.DataFrame(dataframe, directed=direct)
    else:
        print("Input file format not supported")
        return

    if direct == False:
        print("Converted the graph as directed")
        G.to_directed(mode='mutual')

    if multiple_e == True:
        print("Need to implement multiple edges")
        return
    else:
        G.simplify(loops=True)  # Remove self-loops

    G.delete_vertices(G.vs.select(_degree=0))  # Delete nodes with no edges

    return G
