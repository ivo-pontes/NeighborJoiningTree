#!/usr/bin/env python3
# -*- coding: utf-8 -*

from __future__ import division
import numpy as np
from Node import Node

class Njj():
	def __init__(self):
		self.nodes = []

	def execute(self):
		self.d = [
		   # A  B  C  D  E  F
			[0, 0, 0, 0, 0, 0],	#A
			[5, 0, 0, 0, 0, 0],	#B
			[4, 7, 0, 0, 0, 0],	#C
			[7, 10, 7, 0, 0, 0],#D
			[6, 9, 6, 5, 0, 0],	#E
			[8, 11, 8, 9, 8, 0] #F
		]
		
		#self.backup = self.d
		self.n = len(self.d[0])

		while self.n > 2:
			self.differenceMatrix()
			self.stepOne()
			self.stepTwo()
			self.stepThree()
			self.stepFour()
			self.stepFive()

		for i in range(len(self.nodes)):
			self.nodes[i] = self.nodes[i].reverse()

		print(self.nodes)

	def differenceMatrix(self):
		#Quantidade de Linhas/Colunas
		self.TAM = len(self.d[0])

	def sumAllDistances(self, col):
		somaLinha = 0
		somaCol = 0

		for i in range(0,col):
			somaLinha += self.d[col][i]
			#print("Col: %s\n" %(self.d[col][i]))

		for j in range(col+1,self.TAM):
			somaCol += self.d[j][col]
			#print("Linha: %s\n" %(self.d[j][col]))
			
		return (somaLinha + somaCol)

	def minMatrix(self):
		minimum = 10000
		self.min = np.zeros(2).astype(int)
		for i in range(1,self.TAM):
			for j in range(0,self.TAM-1):
				if j < i and self.m[i][j] < minimum:
					minimum = self.m[i][j]
					self.min[0] = i
					self.min[1] = j

	'''
	Compute the net divergence r for every endonde(N = 6)
	'''
	def stepOne(self):

		self.r = []

		for i in range(0,self.TAM):
			self.r.append(self.sumAllDistances(i))

		#print(self.r)
	#Complete


	'''
	Create a rate-corrected distance matrix;
	The elements are defined by Mi = dij - (ri+rj)/(N-2)
	'''
	def stepTwo(self):
		self.m = np.zeros([self.TAM, self.TAM])

		#print(self.m)

		for i in range(1,self.TAM):
			for j in range(0,self.TAM-1):
				if j < i:
					self.m[i][j] = self.d[i][j] - (self.r[i] + self.r[j])/(self.TAM-2)
					#print("M(%d,%d)=%s -[%s + %s]/(%s) = %s" %(i,j,self.d[i][j], self.r[i], self.r[j],self.TAM-2,self.m[i][j]) )
		
		#print(self.m)
	#Complete

	'''
	Define a new node that groups OTUs(Operational Taxonomic Units) i and j for which Mj is minimal
	'''
	def stepThree(self):
		self.minMatrix()
	#Complete

	'''
	Compute the branch lenghts from node U to A and B
	'''
	def stepFour(self):
		p1 = self.d[self.min[0]][self.min[1]]

		#print(self.r)
		sumU1 = p1/2 + (self.r[0] - self.r[1])/(2*(self.TAM-2))
		sumU2 = p1 - sumU1
		
		#print("Sau1: %s\n" %(sumU1))
		#print("Sbu1: %s\n" %(sumU2))
		
		distancias = [sumU1,sumU2]
		posicoes = [self.min[0], self.min[1]]
		self.node = Node(distancias, posicoes)

	def stepFive(self):
		self.du = []

		dAB = self.d[self.min[0]][self.min[1]]		
		for i in range(1,self.TAM):
			if i != self.min[0] and i != self.min[1]:
				daCdbC = self.d[i][self.min[1]] + self.d[i][self.min[0]]
				self.du.append( (daCdbC - dAB)/2 )
	
		#print(self.du)		
		
		self.Mdu = np.zeros([self.TAM-1, self.TAM-1])
		self.aux = np.zeros([self.TAM-1, 1])

		if len(self.du) > 1:
			for i in range(1, len(self.Mdu)):
				self.aux[i][0] = (self.du[i-1])
		else:
			print(self.du)

		self.dx = np.delete(self.d,self.node.uPositions[0], 1)
		self.dx = np.delete(self.dx,self.node.uPositions[1], 1)
		

		self.dx = np.delete(self.dx,0,0)

		#print(self.dx)
		for i in range(1, len(self.Mdu)):
			for j in range(len(self.Mdu)-1):
				if j == 0:
					self.Mdu[i][j] = self.aux[i][j]
				elif i < len(self.Mdu):
					self.Mdu[i][j] = self.dx[i][j-1]
		
		#print(self.Mdu)
		self.nodes.append(self.node.uPositions)
		self.d = self.Mdu
		#print(self.Mdu)
		self.n = self.n -1