import random
def ICM_decay(G, start_nodes, decay_fn):
    uninfected = [v for v in G.vs.indices if v not in start_nodes]
    infected = start_nodes.copy()
    active = start_nodes.copy()

    t = 0
    while len(active) != 0 and len(uninfected) != 0:
        reached = []
        for node in active:
            for neighbor in G.neighbors(node, mode='out'):
                if neighbor in uninfected:
                    if random() <= decay_fn(G.es[G.get_eid(node, neighbor)]['p'], t):
                        infected.append(neighbor)
                        reached.append(neighbor)
                        uninfected.remove(neighbor)

        active = reached.copy()
        t += 1
        return infected