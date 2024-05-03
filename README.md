# Project for Social Network Analysis 2024

By Matt Stirling

## About the code

The code can be found in the 'notebooks' folder. Each notebook is named according to a versioning scheme, which is explained below:

* **notebooks starting with 1.x:** Graph Construction
    - handling tweets dataset
    - construction of edge list
    - construction of adjacency matrix
    - (?) construction of adjacency list

* **notebooks starting with 2.x:** Rudimentary Network/Graph Analysis
    - degree centrality (viewing and analysis)
    - connected components
    - average path length & diameter
    - computing and displaying abstracted version of graph (hashtag network)

* **notebooks starting with 3.x:** Analysis of Network Evolution:
    - evolution of sentiments (positive and negative) over time
    - evolution of transitivity relations
    - triangle balance and its evolution
    - unbalanced triangle as virus propogation case

**Note:** The notebooks don't necessarliy correspond one-to-one to each bullet point. 

## Problems

The graph is very large

* Edges in whole graph: 684,732,453
* Nodes in whole graph: around 500,000
* Size of csv edge list file: 25 GB
* Size of potential adjacency matrix saved as a file: 250+ GB

