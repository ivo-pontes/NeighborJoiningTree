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
		
		linhas = arquivo.readlines()

		for l in linhas:
			#print(l[0])
			if l[0] != '>':
				sg += l
				#print(sg)
			else:
				sg = sg.replace('\n', '')
				self.sequencias.append(sg)
				sg = ''
				l = l.strip().split(' ')
				#print(l[0])
				self.labels.append(l[0].replace('>sp|', ''))

		sg = sg.replace('\n','')
		self.sequencias.append(sg)

		arquivo.close()
		#print(self.sequencias)
		self.sequencias = self.sequencias[1::]
		#print(self.labels)
		#print(self.sequencias)

	def getLabels(self):
		return self.labels

	def getSequencias(self):
		return self.sequencias


		
		