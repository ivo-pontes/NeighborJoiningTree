#!/usr/bin/env python3
# -*- coding: utf-8 -*

from __future__ import division
import numpy as np
from Node import Node

class Nj():
	def __init__(self):
		pass

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
		self.backup = self.d
		self.n = len(self.d[0])

		while self.n > 2:
			self.differenceMatrix()
			self.stepOne()
			self.stepTwo()
			self.stepThree()
			self.stepFour()

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

	def stepOne(self):

		self.somas = []

		for i in range(0,self.TAM):
			self.somas.append(self.sumAllDistances(i))

	#	print(self.somas)


	def stepTwo(self):
		self.m = np.zeros([self.TAM, self.TAM])

		#print(self.m)

		for i in range(1,self.TAM):
			for j in range(0,self.TAM-1):
				if j <= i:
					self.m[i][j] = self.d[i][j] - (self.somas[i] + self.somas[j])/(self.TAM-2)
					#print("M(AB)=%s -[%s + %s]/(%s)" %(self.d[i][j], self.somas[i], self.somas[j],self.TAM-2) )
		
		#print(self.m)

	def stepThree(self):
		self.minMatrix()

		p1 = self.d[self.min[0]][self.min[1]]

		#print(self.somas)
		sumU1 = p1/2 + (self.somas[0] - self.somas[1])/(2*(self.TAM-2))
		sumU2 = p1 - sumU1
		
		#print("Sau1: %s\n" %(sumU1))
		#print("Sbu1: %s\n" %(sumU2))
		
		distancias = [sumU1,sumU2]
		posicoes = [self.min[0], self.min[1]]
		self.node = Node(distancias, posicoes)

	def stepFour(self):
		self.du = np.zeros([self.TAM, self.TAM])
		#print("min[0]: %d"%(self.min[0]))
		#print("min[1]: %d"%(self.min[1]))
		for i in range(2,self.TAM):
			dAC = self.d[i][self.min[0]]
			#print("dAC(d[%d][%d]): %s" %(i,self.min[0],dAC))
			dBC = self.d[i][self.min[1]]
			#print("dBC(d[%d][%d]): %s" %(i,self.min[1],dBC))
			dAB = self.d[self.min[0]][self.min[1]]
			#print("dAB: %s" %(dAB))
			self.du[i][0] = (dAC + dBC - dAB)/2

			for i in range(2,self.TAM):
				for j in range(1,self.TAM):
					self.du[i][j] = self.d[i][j]
				
			#print("Du: %s" %(self.du[i][0])) 
		
		#self.du = np.delete(self.du,self.node.uPositions[0], 1)
		#self.du = np.delete(self.du,0,0)
		#print(self.du)
		self.d = self.du
		self.n = self.n -1