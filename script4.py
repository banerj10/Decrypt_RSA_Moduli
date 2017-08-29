import sys
from fractions import gcd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

key_list = [line.strip() for line in open('stage3.txt')]
mod_list = [int(line.strip(),16) for line in open('moduli.hex')]

key_pair = []
for i in range(0,len(key_list),2):
	key_pair.append([int(key_list[i]), int(key_list[i+1])])

dpq_list = []
#eulers algo here
#e_val = 65537
for pair in key_pair:
	 dpq_list.append([modinv(65537, (pair[0]-1)*(pair[1]-1)), pair[0], pair[1]])

with open('stage4.txt', 'w') as f:
	for val in dpq_list:
		f.write('%s\n' % 'private key, p, q:\n{}\n{}\n{}'.format(val[0], val[1], val[2]))

with open('stage5.txt', 'w') as f:
	for val in dpq_list:
		f.write('%s\n' % '{}\n{}\n{}'.format(val[0], val[1], val[2]))

 
		
