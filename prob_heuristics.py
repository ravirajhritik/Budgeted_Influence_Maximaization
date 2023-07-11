import numpy as np
from random import random
from igraph import *
import pandas as pd

def AA(G: Graph) -> list:
    """
    Returns a list of Adamic Adar Index scores for edges.

    Input:
    G: Igraph Graph object
    """
    prob = []
    for edge in G.es:
        u = edge.source
        v = edge.target
        common_ne = list(set(G.neighbors(u, 'out')).intersection(G.neighbors(v, 'in')))
        score = 0
        for d in G.degree(common_ne, mode='out'):
            score += 1 / (np.log(d + 0.001))
        prob.append(score)
    return prob

def RA(G: Graph) -> list:
    """
    Returns a list of Resource Allocation scores for edges.

    Input:
    G: Igraph Graph object
    """
    prob = []
    for edge in G.es:
        u = edge.source
        v = edge.target
        common_ne = list(set(G.neighbors(u, 'out')).intersection(G.neighbors(v, 'in')))
        score = 0
        for d in G.degree(common_ne, mode='out'):
            score += 1 / d
        prob.append(score)
    return prob

def LHI(G: Graph) -> list:
    """
    Returns a list of Lichtenwalter-Harrell-Newman Index scores for edges.
    """
    prob = []
    for edge in G.es:
        u = edge.source
        v = edge.target
        common_ne = list(set(G.neighbors(u, 'out')).intersection(G.neighbors(v, 'in')))
        prob.append(len(common_ne) / (G.degree(u, mode='out') * G.degree(v, mode='in')))
    return prob

def Jaccard(G: Graph) -> list:
    """
    Returns a list of Jaccard coefficient scores for edges.
    """
    prob = []
    for edge in G.es:
        u = edge.source
        v = edge.target
        common_ne = list(set(G.neighbors(u, 'out')).intersection(G.neighbors(v, 'in')))
        union_ne = list(set(G.neighbors(u, 'out') + G.neighbors(v, 'in')))
        prob.append(len(common_ne) / len(union_ne))
    return prob

def scale(l: list, t_min=0, t_max=1) -> list:
    return (l - np.min(l)) / (np.max(l) - np.min(l)) * (t_max - t_min) + t_min

def prob_heuristics(G: Graph, method: str) -> list:
    """
    Computes edge probability based on different link prediction heuristics.

    Supported methods: 'AA', 'RA', 'LHI', 'Jaccard'

    Returns a list of edge probabilities.
    """
    if method == 'AA':
        return scale(AA(G))
    elif method == 'RA':
        return scale(RA(G))
    elif method == 'LHI':
        return LHI(G)
    elif method == 'Jaccard':
        return Jaccard(G)