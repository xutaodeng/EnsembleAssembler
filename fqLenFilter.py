#!/usr/bin/env python
import sys
f=open(sys.argv[1], 'r')
of=open(sys.argv[2],'w')
try:length=int(sys.argv[3])
except: length=0

i=0
for line in f:
	i+=1
	if i%4==1:
		id=line.strip()[0:30]
		try: pair= line.strip().split()[1]
		except: pair=''
		#id='@mira'+str(i/4)+' '+pair
	elif i%4==2:
		seq=line.strip()
	elif i%4==3:
		qid=line.strip()
	elif i%4==0:
		qseq=line.strip()
		if len(seq) >= length:
			of.write('\n'.join([id,seq, qid, qseq])+'\n')
f.close()
of.close()

