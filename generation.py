import pandas as pd
import networkx as nx
import random
import math

df = pd.read_csv("dataset_people.csv")
n = len(df)

# ==============================
# PROBABILITÉ ADAPTATIVE
# ==============================

def compute_p(n):
    return min(0.4, math.log(n + 1) / n * 5)

p = compute_p(n)

# ==============================
# GRAPHE INITIAL
# ==============================

G = nx.Graph()
G.add_nodes_from(range(n))

# génération des liens
for i in range(n):
    for j in range(i + 1, n):

        if random.random() < p:

            # éviter sur-connexion
            if G.degree[i] < 10 and G.degree[j] < 10:
                G.add_edge(i, j)

# ==============================
# GARANTIR CONNEXE
# ==============================

if not nx.is_connected(G):
    components = list(nx.connected_components(G))

    for i in range(len(components) - 1):
        a = list(components[i])[0]
        b = list(components[i + 1])[0]
        G.add_edge(a, b)

# ==============================
# AJOUT ATTRIBUTS
# ==============================

for i, row in df.iterrows():
    G.nodes[i]["name"] = row["name"]
    G.nodes[i]["age"] = row["age"]

def get_graph():
    return G