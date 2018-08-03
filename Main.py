#!/usr/bin/env python3
# -*- coding: utf-8 -*

from NeighbourJoining import NeighbourJoining


if __name__ == '__main__':

	seqs = [['AUGC'],['ACGC'],['ACGC']]

	nj = NeighbourJoining(seqs)

	nj.stepsOneTwo()

	nj.stepThree()

	nj.stepFour()

	print("Fim de execução!!")