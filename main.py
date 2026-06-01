import subprocess
import matplotlib.pyplot as plt
import networkx as nx

from generation import get_graph
from classification import classify_nodes, detect_communities

# ==============================
# DATASET
# ==============================

subprocess.run(["python3", "dataset.py"])

# ==============================
# GRAPH
# ==============================

G = get_graph()

# ==============================
# CLASSIFICATION
# ==============================

labels = classify_nodes(G)
communities = detect_communities(G)

# ==============================
# COULEURS
# ==============================

color_map = []

for l in labels:
    if l == "isolated":
        color_map.append("#95a5a6")
    elif l == "normal":
        color_map.append("#2ecc71")
    elif l == "active":
        color_map.append("#3498db")
    else:
        color_map.append("#e74c3c")

# ==============================
# VISUALISATION
# ==============================

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 6))

nx.draw(
    G,
    pos,
    node_color=color_map,
    node_size=300,
    edge_color="gray",
    with_labels=False
)

plt.title("Analyse réseau ")
plt.show()

# ==============================
# OUTPUT COMMUNAUTÉS
# ==============================

print("\nCOMMUNAUTÉS DETECTÉES")
for c in communities:
    print(list(c))

print("\nSTATS")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())
print("Density:", nx.density(G))