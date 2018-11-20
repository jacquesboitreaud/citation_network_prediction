""" In this file, we extract the node_information.csv file to create a nice python list
	Thus, the data_set, named 'data' is a list of list. 
	The first axis gives access to the nodes of the datasets (27770 elements)
	The second axis gives access to the features of the the ith element :
	0 : ID
	1 : date
	2 : title
	3 : list of the authors (which varies through the dataset)
	4 : name of the revue, blanck if it is not provided
	5 : abstract """

def load_data():
	""" Export this function in another file to load the data in a python list"""
	import numpy as np
	data=[[0,0,0,0,0,0]]

	with open('node_information.csv') as informations:
	    informations=informations.readlines()

	n_nodes=len(informations)

	for i in range(1,n_nodes):

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

		if '"' in informations[i]:
			pre_line=informations[i].split('"')
			line=pre_line[0].split(",")[:-1]+[pre_line[1].split(",")]+pre_line[2].split(",")[1:]
			line[0]=int(line[0])
			line[1]=int(line[1])	

		data.append(line)
		data=data[1:]

		return data


