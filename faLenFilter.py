#!/usr/bin/env python
import sys
def filterLength(infile, outfile, l, label):
	#outfile = infile.rsplit('.', 1)[0]+str(l)+'_filter.fa'
	#print 'converting', infile, 'to', outfile
	f = open(infile, 'r')
	of = open(outfile, 'w')
	i = 0
	seq=[]
	id=''
	a, b = 0, 0
	for line in f:
		if line.strip().startswith('>'):
			a+=1
			if id!='' and len (''.join(seq)) >= l: 
				b+=1
				of.write('>Contig'+str(b)+'_'+label+'\n'+''.join(seq)+'\n')
			id = line.strip()[1:]
			seq=[]
		else:
			seq.append(line.strip())
	if id!='' and len (''.join(seq)) >= l: of.write('>Contig'+str(b+1)+'_'+label+'\n'+''.join(seq)+'\n')
	f.close()
	of.close()
	#print infile, 'num_contig =', a
	#print infile, 'num_contig_grater_'+str(l), ' = ', b
	
if __name__ == '__main__':
	infile, outfile, length = sys.argv[1], sys.argv[2], sys.argv[3]
	try: label= sys.argv[4]
	except: label=''
	filterLength(infile, outfile, int(length), label)
