#!/usr/bin/env python3
# -*- coding: utf-8 -*

from NeighbourJoining import NeighbourJoining
from Files import Files


if __name__ == '__main__':

	files = Files()
	files.open("arq.fasta")


	nj = NeighbourJoining(files.getLabels(), files.getSequencias())
	nj.execute()


	print("Fim de execução!!")