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

infs = [x for x in os.listdir('../instances') if (x.startswith('color') and x.endswith('.dat'))]
infs = sorted(infs, key=lambda x: int(x.split('-')[0][5:]))

try:
	time = sys.argv[1]
	print("Time limit "+time+" seconds per problem")
except:
	time = None

for f in infs:
	n = f[5:-4]
	print("################################################################################")
	print("###				Problem "+n+"											###")
	fn = "color_full.run"
	os.system('cat color1.run > '+fn)
	with open(fn, 'a') as runf:
		runf.write("data ../instances/"+f+";\n")
		if time is not None:
			runf.write("option cplex_options 'timelimit="+time+"';\n")
	os.system('cat color.run >> '+fn)
	os.system('ampl '+fn+' > ../outputs/'+f[:-4]+'.output')
	os.system('rm '+fn)
