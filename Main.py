#!/usr/bin/env python3
# -*- coding: utf-8 -*

from __future__ import division
import numpy as np

def soma(d, col, TAM):
	soma_linha = 0
	soma_col = 0

	for i in range(0,col):
		soma_linha += d[col][i]
		#print("Col: %s\n" %(d[col][i]))

	for j in range(col+1,TAM):
		soma_col += d[j][col]
		#print("Linha: %s\n" %(d[j][col]))
		
	return (soma_linha + soma_col)/(TAM-2)

if __name__ == '__main__':

	d = [
	   # A  B  C  D  E  F
		[0, 0, 0, 0, 0, 0],	#A
		[5, 0, 0, 0, 0, 0],	#B
		[4, 7, 0, 0, 0, 0],	#C
		[7, 10, 7, 0, 0, 0],#D
		[6, 9, 6, 5, 0, 0],	#E
		[8, 11, 8, 9, 8, 0] #F
	]

	TAM = len(d[0])

	somas = []

	for i in range(0,TAM):
		somas.append(soma(d, i, TAM))

	#print(somas)


	m = np.zeros([TAM, TAM])

	print(m)

	for i in range(1,TAM):
		for j in range(0,TAM-1):
			if j < i:
				m[i][j] = d[i][j] - somas[i] - somas[j]

	print(m)

	



	print("Fim de execução!!")