#!/usr/bin/env python3
# -*- coding: utf-8 -*
#import sys

from random import randint
import numpy as np

class PhylogeneticTree():
	'''
	A set of utilitarian methods for the reconstruction of phylogenetic trees
	'''
	def __init__(self):
		self.maxValue = 0
		self.matrix = []
		self.d = []

	'''
	Finds the max value in the matrix
	'''
	def maxMatrix(self, matrix):
		maxValue = 0
		for i in range(1, len(matrix) ):
			maxValue = max(maxValue, len(matrix[i]))

		self.maxValue = maxValue

	"""
	Randomly initialize the matrix by adding gaps to the right of each line until they all have the same length
	"""
	def normalizesMatrix(self, matrix):
		self.maxMatrix(matrix)
		for row in range(0, len(matrix)):
			while len(matrix[row]) < self.maxValue:
				j = randint(0, len(matrix[row])-1)
				matrix[row] = matrix[row][0:j] + "*" + matrix[row][j::]

		self.matrix = matrix

	'''
	Generate Matrix Distance
	'''
	def generateMatrixDistances(self):
		self.d = np.zeros([len(self.matrix),len(self.matrix)])

		strlen = len(self.matrix[0])
		for i in range(len(self.matrix)-1):
			for j in range(i+1,len(self.matrix)):
				count = 0
				for k in range(strlen):
					if self.matrix[i][k] != self.matrix[j][k]:
						count += 1
					if len(self.matrix)-i <2:
						print("Matriz[%d][%d]: %s\nMatriz[%d][%d]: %s\n" %(i,k,self.matrix[i][k],j,k, self.matrix[i+1][k]) )
				self.d[j][i] = count

