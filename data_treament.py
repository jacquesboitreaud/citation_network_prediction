""" In this file, we extract the node_information.csv file to create a nice python list
	Thus, the data_set, named 'data' is a list of list. 
	The first axis gives access to the nodes of the datasets (27770 elements)
	The second axis gives access to the features of the the ith element :
	0 : ID
	1 : date
	2 : title
	3 : list of the authors (which varies through the dataset)
	4 : name of the revue, blanck if it is not provided
	5 : abstract
	6 : articles the paper mentions -> the first arg is the number of articles the paper mentions
	7 : articles in which the paper is mentionned -> the first arg is the number of articles in which the paper is mentionned """

def load_data():
	""" Export this function in another file to load the data in a python list"""
	import numpy as np
	data=[[0,0,0,0,0,0]]

	with open('node_information.csv') as informations:
	    informations=informations.readlines()
	with open('training_set.txt') as links:
		links=links.readlines()

	n_nodes=len(informations)
	n_links=len(links)

	for i in range(0,n_nodes):

		# Solve the characters' issues

		if i==23799:
			informations[i]=informations[i].replace('"""Black"',' Black ')
		if i==26573:
			informations[i]=informations[i].replace('"Zacatecas,"',' Zacatecas ')
		informations[i]=informations[i].replace('\n','')
		informations[i]=informations[i].replace('""o','o')
		informations[i]=informations[i].replace('""u','u')
		informations[i]=informations[i].replace('""a','a')
		informations[i]=informations[i].replace('""e','e')
		informations[i]=informations[i].replace('""i','i')
		informations[i]=informations[i].replace('""{o}','o')
		informations[i]=informations[i].replace('""{u}','u')
		informations[i]=informations[i].replace('""{a}','a')
		informations[i]=informations[i].replace('""{e}','e')
		informations[i]=informations[i].replace('""{i}','i')
		informations[i]=informations[i].replace('""{\o}','o')
		informations[i]=informations[i].replace('""{\u}','u')
		informations[i]=informations[i].replace('""{\a}','a')
		informations[i]=informations[i].replace('""{\e}','e')
		informations[i]=informations[i].replace('""{\i}','i')
		informations[i]=informations[i].replace('""',' '' ')


		if '"' not in informations[i]:
			line=informations[i].split(",")
			line[0]=int(line[0])
			line[1]=int(line[1])
			line[3]=[line[3]]
			line+=[[0]]+[[0]]

		if '"' in informations[i]:
			pre_line=informations[i].split('"')
			line=pre_line[0].split(",")[:-1]+[pre_line[1].split(",")]+pre_line[2].split(",")[1:]+[[0]]+[[0]]
			line[0]=int(line[0])
			line[1]=int(line[1])

		data.append(line)


	data=data[1:]

	IDs={}
	for i in range(n_nodes):
		IDs.update({data[i][0]:i})

	for i in range(n_links):
		link=links[i].split(" ")
		ID_from=int(link[0])
		ID_target=int(link[1])
		bool_link=int(link[2])

		if bool_link==1 :
			data[IDs[ID_from]][6]+=[ID_target]
			data[IDs[ID_from]][6][0]+=1
			data[IDs[ID_target]][7]+=[ID_from]
			data[IDs[ID_target]][7][0]+=1

	return data

data=load_data()
