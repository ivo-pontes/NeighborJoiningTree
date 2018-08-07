#!/usr/bin/env python3
# -*- coding: utf-8 -*
#import sys

from random import randint
import numpy as np

class Tree():
	def __init__(self):
		self.maximo = 0
		self.matriz = []
		self.d = []

	def maxMatriz(self, matrix):
		maximo = 0
		#print(matrix)
		for i in range(1, len(matrix) ):
			maximo = max(maximo, len(matrix[i]))

		#print("Máximo: %s.\n" %(maximo))
		self.maximo = maximo

	"""
	Inicializa de forma randomica o chromosome, adicionando gaps a direita de cada linha
	até que todos tenham o mesmo comprimento
	"""
	def normalizarMatriz(self, matrix):
		self.maxMatriz(matrix)
		for row in range(0, len(matrix)):
			while len(matrix[row]) < self.maximo:
				j = randint(0, len(matrix[row])-1)
				matrix[row] = matrix[row][0:j] + "*" + matrix[row][j::]

		self.matriz = matrix
		#return matrix

	def gerarMatrizDistancias(self):
		self.d = np.zeros([len(self.matriz),len(self.matriz)])

		strlen = len(self.matriz[0])
		for i in range(len(self.matriz)-1):
			for j in range(i+1,len(self.matriz)):
				count = 0
				for k in range(strlen):
					if self.matriz[i][k] != self.matriz[j][k]:
						count += 1
					if len(self.matriz)-i <2:
						print("Matriz[%d][%d]: %s\nMatriz[%d][%d]: %s\n" %(i,k,self.matriz[i][k],j,k, self.matriz[i+1][k]) )
				self.d[j][i] = count
				#print("Linhas %sx%s: %s" %(i,j,count))

