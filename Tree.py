#!/usr/bin/env python3
# -*- coding: utf-8 -*
#import sys

from random import randint

class Tree():
	def __init__(self):
		self.maximo = 0

	def maxMatriz(self, matrix):
		maximo = 0
		#print(matrix)
		for i in range(1, len(matrix) ):
			maximo = max(maximo, len(matrix[i]))

		print("Máximo: %s.\n" %(maximo))
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
		return matrix

		


