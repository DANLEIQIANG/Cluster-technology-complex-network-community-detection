# Cluster-technology-complex-network-community-detection
1 Experiment Content  
----

Complex network community structure is defined as a topological structure with tight inside and loose outside, that is, a set of nodes that interact closely with each other but loosely with the external nodes.  

2 Principal method  
----

2.1 According to the characteristics of network structure, the node similarity measurement index is given. Given node I, its neighbor node is defined as the set composed of all the nodes linked to this node, that is, N I ={j|Aij = 1,j = 1,2...,n} given a pair of nodes (I,j), its similarity is defined as the union of the common neighbor node and neighbor node of these two nodes.  

2.2 Greedy algorithm is used to extract modules.  

Randomly select an unclustered node as the current community C, and extract all unclustered neighbor nodes N C of community C.District in all not cluster node is added to reduce community density smallest node v C community, community density lower minimum judgment sign for this node v with maximum similarity of community C, here I choose judgment node v to community C similarity of each node and divided by the number of nodes in group C, the greater the value indicates node v and community C the more similar, update the current community of C = C ∪ v.Continue the process until the density of the current community is below a certain threshold.  

3 py3.x



