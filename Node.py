#!/usr/bin/env python3
# -*- coding: utf-8 -*


class Node():
	'''
	Distâncias: São as distâncias entras sequências do Nó U
	Posições: As posições das seqs na Matriz de Diferenças
	'''
	def __init__(self, distances, positions):
		self.uDistances = distances
		self.uPositions = positions


	def toString(self):
		return "Distâncias: %s.\nPosições: %s.\n" %(self.uDistances, self.uPositions)