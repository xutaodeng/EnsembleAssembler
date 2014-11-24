#!/usr/bin/env python
from collections import defaultdict
import operator
import sys
import os
import os.path
import itertools
import gzip

def partition(filename, k):
	f=open(filename, 'r') #fastq file
	nchunk=0
	buf=[]
	nread =0
	i=0
	for line in f:
		i+=1
		buf.append(line.strip())
		if i%4==0:
			nread+=1
			if nread%k==1: of = open(filename+'_'+str(nchunk), 'w')
			of.write('\n'.join(buf)+'\n')
			if nread%k==0:
				of.close()
				nchunk+=1
			buf=[]
	of.close()
	f.close()
	return nchunk+1 #number of chunks

if __name__ == '__main__':
	filename=sys.argv[1]
	k=int(sys.argv[2])
	nchunk = partition(filename, k)