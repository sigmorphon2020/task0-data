import os
import numpy as np

def read_sigmorphon_test(f):
	with open(f) as inp:
		lines = inp.readlines()
	return [l.strip().split('\t')[1] for l in lines]

def eval_acc(gold,sys):
	return sum([1 if g == s else 0 for g, s in zip(gold, sys)]) / float(len(gold))

if __name__ == "__main__":
	# execute only if run as a script
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--gold', help='Gold File', default='')
	parser.add_argument('--sysout', help='System Output', default='')
	args = parser.parse_args()

	gold = args.gold
	sysout = args.sysout

	#print(f"Languages\tAccuracy")
	data = {}
	data['gold'] = read_sigmorphon_test(gold)
	data['system'] = read_sigmorphon_test(sysout)

	acc = eval_acc(data['gold'], data['system'])

	print(f"{acc}")

