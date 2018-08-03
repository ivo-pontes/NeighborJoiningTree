#!/usr/bin/env python3
# -*- coding: utf-8 -*

from __future__ import division
import numpy as np
from Node import Node

class NeighbourJoining():
	"""docstring for NeighbourJoining"""
	def __init__(self, seqs):
		self.seqs = seqs
		#Nós U, que serão os nós internos da árvore
		self.nodes = []


	def differenceMatrix(self):
		
		'''
		Por ora, estamos setando a matriz com as diferenças
		'''
		self.d = [
		   # A  B  C  D  E  F
			[0, 0, 0, 0, 0, 0],	#A
			[5, 0, 0, 0, 0, 0],	#B
			[4, 7, 0, 0, 0, 0],	#C
			[7, 10, 7, 0, 0, 0],#D
			[6, 9, 6, 5, 0, 0],	#E
			[8, 11, 8, 9, 8, 0] #F
		]

		#Quantidade de Linhas/Colunas
		self.TAM = len(self.d[0])

	'''
	Método somará todas as distâncias entre 2 sequências
	'''
	def sumAllDistances(self, col):
		somaLinha = 0
		somaCol = 0

		for i in range(0,col):
			somaLinha += self.d[col][i]
			#print("Col: %s\n" %(d[col][i]))

		for j in range(col+1,self.TAM):
			somaCol += self.d[j][col]
			#print("Linha: %s\n" %(d[j][col]))
			
		return (somaLinha + somaCol)/(self.TAM-2)



	def stepsOneTwo(self):

		self.differenceMatrix()

		self.somas = []

		for i in range(0,self.TAM):
			self.somas.append(self.sumAllDistances(i))

		#print(somas)


		self.m = np.zeros([self.TAM, self.TAM])

		#print(self.m)

		for i in range(1,self.TAM):
			for j in range(0,self.TAM-1):
				if j < i:
					self.m[i][j] = self.d[i][j] - self.somas[i] - self.somas[j]

		print(self.m)
		print("\n")


	'''
	From here, step 3
	'''

	def stepThree(self):
		self.minMatrix()


		p1 = self.d[self.min[0]][self.min[1]]/2

		
		sumU1 = p1 + (self.somas[self.min[1]] - self.somas[self.min[0]])/2
		sumU2 = p1 + (self.somas[self.min[0]] - self.somas[self.min[1]])/2
		
		print("Sau1: %s\n" %(sumU1))
		print("Sbu1: %s\n" %(sumU2))
		
		distancias = [sumU1,sumU2]
		posicoes = [self.min[0], self.min[1]]

		self.nodes.append(Node(distancias, posicoes))

		print(self.nodes[0].toString())

	def minMatrix(self):
		minimum = 1000
		self.min = np.zeros(2).astype(int)

		for i in range(1,self.TAM):
			for j in range(0,self.TAM-1):
				if j < i:
					if self.m[i][j] < minimum:
						minimum = self.m[i][j]
						self.min[0] = i
						self.min[1] = j

	'''
	From here, step 4
	'''