#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 zacharyneveu <zacharyneveu@Iota>
#
# Distributed under terms of the MIT license.

"""
Runs all knapsack instances
"""
import sys, os

infs = [x for x in os.listdir('../instances') if (x.startswith('knapsack') and x.endswith('.dat'))]
infs = sorted(infs, key=lambda x: int(x[8:-4]))

try:
	time = sys.argv[1]
	print("Time limit "+time+" seconds per problem")
except:
	time = None

for f in infs:
	n = int(f[8:-4])
	print("################################################################################")
	print("###				Problem "+str(n)+"											###")
	print("################################################################################")
	fn = "knap.run"
	os.system('cat knap1.run > '+fn)
	with open(fn, 'a') as runf:
		runf.write("data ../instances/"+f+"\n")
		if time is not None:
			runf.write("option cplex_options 'timelimit="+time+"';\n")
	os.system('cat knap2.run >> '+fn)
	os.system('ampl '+fn+' > ../outputs/'+f[:-4]+'.output')
	os.system('rm '+fn)
