# Détection de fraude par analyse de graphe

##  Description du projet

Ce projet consiste à modéliser un réseau d’interactions sous forme de graphe aléatoire **Erdős–Rényi** afin d’analyser sa structure et simuler une détection de comportements suspects.

Chaque sommet représente une personne et chaque arête représente une relation entre deux individus.

---

##  Objectifs

- Générer un graphe aléatoire $G(n,p)$
- Garantir la connexité du graphe
- Attribuer des caractéristiques aux nœuds (âge, statut)
- Analyser la structure du réseau
- Classifier les sommets selon leur importance

---

##  Modèle utilisé

Le graphe est construit selon le modèle :

\[
G(n, p)
\]

où :
- **n** = nombre de sommets
- **p** = probabilité de création d’une arête

Pour assurer une meilleure stabilité :

- Petit graphe : `p = 0.3`
- Grand graphe : `p = ln(n)/n`

---
