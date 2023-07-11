Influence Maximization (IM) is a problem in network analysis that aims to identify a small set of influential nodes in a network to maximize the spread of influence or information.

Budgeted Influence Maximization (BIM) is a variant of IM where there is a limited budget to select seed nodes for influence propagation.
The Independent Cascade Model is commonly used to model influence propagation in networks. It assumes that influence spreads through directed edges with a certain probability.

The proposed cost function for BIM takes into account two important metrics: geodesic distance and influential powers of seed and source nodes.

The geodesic distance factor in the cost function reflects that being closer to a seed node reduces the seeding effort, as it is easier to influence nearby nodes.

The influential powers factor in the cost function considers the difference in influence between the seed and source nodes. Higher influence difference implies greater seeding effort.

The cost function is designed to be exponential in distance and incorporates the h2 indices as approximations of the shell numbers of the nodes.

The budget factor (f) is used to define the total budget for a network, which determines the maximum allowable cost for selecting seed nodes.

The greedy BIM algorithm is proposed to find the optimal seed set given the budget. It iteratively selects seed nodes based on their influence and cost, until the budget is exhausted.

The performance of the proposed cost function is compared to baseline approaches that use degree-based cost functions in terms of the final influence achieved.

The proposed cost function (GSM-h2) leads to higher influence compared to the baseline approaches, indicating its effectiveness in selecting influential seed nodes.

The paper also highlights the importance of considering edge weights in influence propagation, which can improve the categorization of users based on their influential power.

Simple link prediction heuristics like resource allocation and Adamic-Adar coefficient are shown to be effective in predicting edge weights from the network structure.

The conclusion emphasizes the significance of considering the source node (interested firm) and its social distance from the influencer in defining the cost function for influence maximization.