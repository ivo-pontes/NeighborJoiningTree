#!/usr/bin/env python3
# -*- coding: utf-8 -*


class Node():
	'''
	Distances: These are the distances between the U-Node sequences
	Positions: The positions of the seqs in the Matrix of Differences
	'''
	def __init__(self, distances, positions):
		self.uDistances = distances
		self.uPositions = positions


	def toString(self):
		return "Distance: %s.\nPosition: %s.\n" %(self.uDistances, self.uPositions)