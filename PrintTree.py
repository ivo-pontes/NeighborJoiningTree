#!/usr/bin/env python3
# -*- coding: utf-8 -*

from ete3 import Tree

class PrintTree():
	"""PrintTree"""
	def __init__(self):
		pass

	def print(self, nodes):
		c = self.generateArrayStr(nodes)
		#c = self.generateArrayInt(nodes)
		print(c)
		#c = "(((A,B),C),((D,E),F));"
		tree = Tree(c)
		tree.render('tree.png', dpi=200)

	def generateArrayStr(self, nodes):
		coords = ""
		c = []
		v = []
		#print(len(nodes))
		#nodes = [['A','B'], [-1, 'C'], ['D', 'E'], [-3,-2], [-4,'F']]
		for i in range(len(nodes)):
			if isinstance(nodes[i][0], int) and isinstance(nodes[i][1],int) and nodes[i][0] < 0 and nodes[i][1] < 0:
				#print("Nodes({},{})".format(v[nodes[i][1]*(-1)-1],v[nodes[i][0]*(-1)-1]))
				v.append("({},{})".format(v[nodes[i][0]*(-1)-1],v[nodes[i][1]*(-1)-1]))
			elif isinstance(nodes[i][1], int) and nodes[i][1] < 0:
				#print("Nodes[{}][1]: {}".format(i, nodes[i]))
				v.append("({},{})".format(nodes[i][0],v[nodes[i][1]*(-1)-1]))			
			elif isinstance(nodes[i][0], int) and nodes[i][0] < 0:
				#print("Nodes[{}][0]: {}".format(i, nodes[i]))
				v.append("({},{})".format(v[nodes[i][0]*(-1)-1],nodes[i][1]))
			else:
				#print("Nodes[{}][{}]".format(nodes[i][0], nodes[i][1]))
				v.append("({},{})".format(nodes[i][0],nodes[i][1]))
			
		#print(v)
		coords += "{};".format(v[len(v)-1])

		return coords


	def generateArrayInt(self, nodes):
		coords = ""
		c = []
		v = []
		#print(len(nodes))
		#nodes = [['A','B'], [-1, 'C'], ['D', 'E'], [-3,-2], [-4,'F']]
		for i in range(len(nodes)):
			if nodes[i][0] < 0 and nodes[i][1] < 0:
				#print("Nodes({},{})".format(v[nodes[i][1]*(-1)-1],v[nodes[i][0]*(-1)-1]))
				v.append("({},{})".format(v[nodes[i][0]*(-1)-1],v[nodes[i][1]*(-1)-1]))
			elif nodes[i][1] < 0:
				#print("Nodes[{}][1]: {}".format(i, nodes[i]))
				v.append("({},{})".format(nodes[i][0],v[nodes[i][1]*(-1)-1]))			
			elif nodes[i][0] < 0:
				#print("Nodes[{}][0]: {}".format(i, nodes[i]))
				v.append("({},{})".format(v[nodes[i][0]*(-1)-1],nodes[i][1]))
			else:
				#print("Nodes[{}][{}]".format(nodes[i][0], nodes[i][1]))
				v.append("({},{})".format(nodes[i][0],nodes[i][1]))
			
		#print(v)
		coords += "{};".format(v[len(v)-1])

		return coords


