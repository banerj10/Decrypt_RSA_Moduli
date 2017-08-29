import sys
from fractions import gcd

idx_list = [line.strip() for line in open('stage1.txt')]
mod_list = [int(line.strip(),16) for line in open('moduli.hex')]

ij_list = []
for n, val in enumerate(idx_list):
	i = val[12:16].strip()
	j = val[-4:].strip()
	ij_list.append([i,j])

gcd_list = []
for val in ij_list:
	i = int(val[0])
	j = int(val[1])
	k = gcd(mod_list[i], mod_list[j])
	l = mod_list[i]/k
	m = mod_list[j]/k 
	gcd_list.append([i,j,k,l,m])

with open('stage2.txt', 'w') as f:
	for val in gcd_list:
		f.write('%s\n' % 'factors from i: {} and j: {} are\n{}\n{}\n{}'.format(val[0], val[1], val[2], val[3], val[4]))

with open('stage3.txt', 'w') as f:
	for val in gcd_list:
		f.write('%s\n' % '{}\n{}\n{}\n{}'.format(val[2], val[3], val[2], val[4]))

 
		
