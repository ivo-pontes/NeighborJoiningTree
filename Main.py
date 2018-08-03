#!/usr/bin/env python3
# -*- coding: utf-8 -*

from NeighbourJoining import NeighbourJoining


if __name__ == '__main__':

	seqs = [['AUGC'],['AUGC'],['AUGC']]

	nj = NeighbourJoining(seqs)

	nj.stepsOneTwo()

	nj.stepThree()

	print("Fim de execução!!")