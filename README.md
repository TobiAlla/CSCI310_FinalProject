# Community Detection Visualizer

## Introduction

The Community Detection Visualizer is a Python project that analyzes and visualizes networks. The goal is to identify groups of nodes that are more closely connected to each other than to the rest of the network.

The project will use NetworkX to create and analyze graphs and Matplotlib to visualize them.

## AI Disclaimer

ChatGpt was used to generate the general structure of the project and for parts of the sphinx documentation.

## Current Progress

The first milestone focuses on setting up the project and creating an initial network visualization.

Currently implemented:

- Project structure and documentation.
- Loading the Karate Club dataset using NetworkX.
- Displaying basic network statistics.
- Visualizing the original network.
- Saving network visualizations as PNG files.

## Planned Features

- Implement the Girvan-Newman algorithm from scratch.
- Implement Louvain community detection using Python-Louvain.
- Visualize detected communities using different node colors.
- Compare algorithms based on execution time, number of communities, and modularity.
- Test additional network datasets, including Facebook or collaboration networks.

## Technologies

- Python
- NetworkX
- Matplotlib
- Python-Louvain (planned)

## Installation

Install the required packages:

```bash
uv pip install -r requirements.txt
```

## Running the Program

Run the following command from the project directory:

```bash
python src/main.py
```

## Output

The program displays basic network statistics and generates a visualization of the Karate Club network.

The generated image is saved in:

`output/graphs/karate_club_raw.png`