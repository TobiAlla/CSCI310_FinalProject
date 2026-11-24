
"""
Graph Loader Module

Loads network datasets using NetworkX.
"""

import networkx as nx


def loadGraph(dataset="karate"):
    """
    Load a network dataset.

    Parameters
    ----------
    dataset : str
        Name of the dataset to load.

    Returns
    -------
    networkx.Graph
        The loaded network graph.

    Raises
    ------
    ValueError
        If the requested dataset is not supported.
    """
    if dataset.lower() == "karate":
        graph = nx.karate_club_graph()

    else:
        raise ValueError(f"Unknown dataset: {dataset}")

    return graph


def displayGraphInfo(graph):
    """
    Display basic information about a network.

    Parameters
    ----------
    graph : networkx.Graph
        The network to analyze.
    """
   
    print(f"Number of Nodes: {graph.number_of_nodes()}")
    print(f"Number of Edges: {graph.number_of_edges()}")
    print(f"Average Degree: {sum(dict(graph.degree()).values()) / graph.number_of_nodes():.2f}")
    print(f"Network Density: {nx.density(graph):.4f}")
    print(f"Connected Components: {nx.number_connected_components(graph)}")
 
