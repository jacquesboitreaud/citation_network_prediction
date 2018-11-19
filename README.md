# citation_network_prediction
Edges have been deleted at random from a citation network. Your mission is to accurately reconstruct the initial network using graph-theoretical, textual, and other information.  In this competition, we define a citation network as a graph where nodes are research papers and there is an edge between two nodes if one of the two papers cite the other.

Bibliography 

https://www.semanticscholar.org/paper/Link-prediction-in-citation-networks-Shibata-Kajikawa/090883879b1343630f647f95c9c8fe2eb216e889

Problem description

Classification problem : 0 -> No citation ; 1 -> citation

Features :
1: ID
2: Publication year
3: Title
4: Authors
5: Name of the journals
6: Abstract

Problem questions 

1. Which technic is the most performant for this problem ?
-> Mathieu : SVM ?

2. What are the most relevant features ?
-> Mathieu : I think that we may preprocess the dataset to find another features. In particular, since we are studying a graph structure, we may compute the common neighbors between two nodes. There are some interesting details in [1] concerning the features.

3. How can we use the abstract/title features ?
-> Mathieu : I think that we may take a look at the Word2Vec technic to preprocess the "text" datas

4. How can we break the symmetry in the problem ?
-> Mathieu : If a paper points toward another paper, the opposite may not be true. Thus, we have to find features that break the symmetries between two papers...

Tasks

1. Preprocess the datas and create the features
2.
3.
