
"""
Visualization Module

Creates and saves visualizations of network graphs.
"""

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


def visualizeGraph(graph, title="Karate Club Network"):
    """
    Visualize a network graph and save the image.

    Parameters
    ----------
    graph : networkx.Graph
        The network to visualize.

    title : str
        Title of the visualization.
    """
    
    outputDirectory = Path("output/graphs")
    outputDirectory.mkdir(parents=True, exist_ok=True)

  
    pos = nx.spring_layout(graph, seed=42)

  
    plt.figure(figsize=(10, 8))

   
    nx.draw_networkx(
        graph,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=600,
        font_size=9,
        font_weight="bold",
        edge_color="gray",
        width=1.2
    )

    plt.title(title, fontsize=16)
    plt.axis("off")
    plt.tight_layout()

   
    filename = outputDirectory / "karate_club_raw.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")

    print(f"Visualization saved to: {filename}")

    
    plt.show()

    plt.close()
