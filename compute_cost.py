def compute_cost(G):
    cost = {}
    for node in G.nodes():
        cost[node] = 0

    for edge in G.edges():
        weight = G[edge[0]][edge[1]]['weight']
        cost[edge[0]] += weight
        cost[edge[1]] += weight

    return cost
