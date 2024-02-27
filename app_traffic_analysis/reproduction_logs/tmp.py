import numpy as np
import networkx as nx
from sklearn.cluster import KMeans
import json

# Original graph data
graph_data = {
    "directed": False,
    "multigraph": False,
    "graph": {},
    "nodes": [
        {
            "ip_address": "10.55.223.209",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.223.209",
        },
        {
            "ip_address": "149.196.199.81",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "149.196.199.81",
        },
        {
            "ip_address": "10.55.136.2",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.136.2",
        },
        {
            "ip_address": "10.55.204.47",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.204.47",
        },
        {
            "ip_address": "10.55.11.110",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.11.110",
        },
        {
            "ip_address": "10.55.111.179",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.111.179",
        },
        {
            "ip_address": "10.55.192.247",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.192.247",
        },
        {
            "ip_address": "10.55.25.2",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.25.2",
        },
        {
            "ip_address": "10.55.218.175",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.218.175",
        },
        {
            "ip_address": "10.55.227.88",
            "color": "steelblue",
            "size": 4,
            "labels": ["type=VM"],
            "id": "10.55.227.88",
        },
    ],
    "links": [
        {
            "source_ip_address": "149.196.199.81",
            "target_ip_address": "10.55.227.88",
            "byte_weight": 1.0824926674973954,
            "connection_weight": 0.5751799817272489,
            "packet_weight": 0.8967376844051819,
            "source": "149.196.199.81",
            "target": "10.55.227.88",
        },
        {
            "source_ip_address": "10.55.111.179",
            "target_ip_address": "10.55.25.2",
            "byte_weight": 1.6856020671703364,
            "connection_weight": 0.13089314460287413,
            "packet_weight": 0.6299688175490727,
            "source": "10.55.111.179",
            "target": "10.55.25.2",
        },
        {
            "source_ip_address": "10.55.227.88",
            "target_ip_address": "10.55.25.2",
            "byte_weight": 0.46166850774476115,
            "connection_weight": 0.21475819782321132,
            "packet_weight": 1.0206248780754055,
            "source": "10.55.25.2",
            "target": "10.55.227.88",
        },
    ],
}

# Initialize NetworkX graph
G = nx.Graph()

# Add nodes
for node in graph_data["nodes"]:
    G.add_node(
        node["id"],
        ip_address=node["ip_address"],
        size=node["size"],
        labels=node["labels"],
    )

# Add edges with weights
for link in graph_data["links"]:
    G.add_edge(link["source"], link["target"], byte_weight=link["byte_weight"])

# Calculate total byte weight of edges incident on each node
total_byte_weight = {}
for node in G.nodes():
    total_byte_weight[node] = sum(
        [G[node][nbr]["byte_weight"] for nbr in G.neighbors(node)]
    )

# Shape the data for KMeans clustering
byte_weights = np.array(list(total_byte_weight.values())).reshape(-1, 1)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=0).fit(byte_weights)

# Assign cluster labels to nodes and pick colors
colors = ["red", "green", "blue", "yellow", "purple"]
for i, node in enumerate(G.nodes()):
    cluster_label = kmeans.labels_[i]
    G.nodes[node]["cluster"] = str(cluster_label)
    G.nodes[node]["color"] = colors[cluster_label]

# Return the modified graph object
print(json.dumps(nx.readwrite.json_graph.node_link_data(G), indent=4))
