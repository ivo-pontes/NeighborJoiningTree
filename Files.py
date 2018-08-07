#!/usr/bin/env python3
# -*- coding: utf-8 -*
#import sys

class Files():
	"""docstring for Files"""
	def __init__(self):
		self.labels = []
		self.sequencias = []

	def open(self, arquivo):
		#filename = "./"+sys.argv[1] #nome do arquivo
		filename = "./%s" % (arquivo) #nome do arquivo
		#print(filename)	
		dados = []
		
		arquivo = open(filename)
		sg = ''
		

		for l in arquivo.readlines():
			if l[0] != '>':
				sg += l
			else:
				sg = sg.replace('\n', '')
				self.sequencias.append(sg)
				sg = ''
				l = l.strip().split(' ')
				self.labels.append(l[0].replace('>sp|', ''))

		arquivo.close() 
		self.sequencias = self.sequencias[1::]
		#print(self.labels)
		#print(self.sequencias)

	def getLabels(self):
		return self.labels

	def getSequencias(self):
		return self.sequencias


		
		