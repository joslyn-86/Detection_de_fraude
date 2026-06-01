import networkx as nx

# ==============================
# CENTRALITÉ (plus scientifique)
# ==============================

def classify_nodes(G):

    centrality = nx.degree_centrality(G)

    labels = []

    for node in G.nodes():

        c = centrality[node]

        if c < 0.05:
            labels.append("isolated")
        elif c < 0.15:
            labels.append("normal")
        elif c < 0.3:
            labels.append("active")
        else:
            labels.append("hub")

    return labels


# ==============================
# COMMUNAUTÉS (différent du copier)
# ==============================

def detect_communities(G):

    from networkx.algorithms.community import greedy_modularity_communities

    communities = list(greedy_modularity_communities(G))

    return communities