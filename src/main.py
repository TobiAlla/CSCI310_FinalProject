"""
main.py
====================================
Community Detection Visualizer

Main program for loading and visualizing network datasets.

| Author: Tobias Allerstorfer
| Date: 2026 November 23
"""



from graphloader import loadGraph, displayGraphInfo
from visualization import visualizeGraph


def main():
    """
    Run the Community Detection Visualizer.
    """

    graph = loadGraph("karate")
    
    displayGraphInfo(graph)

  
    print("Generating network visualization...")

    visualizeGraph(
        graph,
        title="Karate Club Network"
    )

    


if __name__ == "__main__":
    main()
