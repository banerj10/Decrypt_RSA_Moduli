import sys

idx_list = [line.strip() for line in open('stage0.txt')]

ij_list = []
for n, val in enumerate(idx_list):
	i = val[12:16].strip()
	j = val[-4:].strip()
	ij_list.append([i,j])

for i in range(len(ij_list)):
	for j in range(i+1,len(ij_list)):
		if i != j and ij_list[i] == ij_list[j][::-1]:
			ij_list[j] = [0,0]

del ij_list[-1]
with open('stage1.txt', 'w') as f:
	for val in ij_list:
		if val != [0,0]:
			f.write('%s\n' % 'index of i: {} and index of j: {}'.format(val[0], val[1]))

 
		
