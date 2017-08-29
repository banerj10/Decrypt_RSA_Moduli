import sys
from pbp import decrypt
from Crypto.PublicKey import RSA

temp_list = [line.strip() for line in open('stage5.txt')]

dpq_list = []
for i in range(0,len(temp_list),3):
	dpq_list.append([int(temp_list[i]), int(temp_list[i+1]), int(temp_list[i+2])])

with open('3.2.4_ciphertext.enc.asc') as f:
	cipher = f.read()

text_list = []
for i, val in enumerate(dpq_list):
	rsaobj = RSA.construct((val[1]*val[2],long(65537),val[0]))
	try:
		text = decrypt(rsaobj,cipher)
		text_list.append(text)
	except:
		continue

with open('stage6.txt', 'w') as f:
	for idx, val in enumerate(text_list):
		f.write('%s\n' % 'attempt {} to decrypt: {}'.format(idx, val))
