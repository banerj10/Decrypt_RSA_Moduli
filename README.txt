The file 3.2.4_ciphertext.enc.asc contains an encrypted message. The file moduli.hex contains 10,000 RSA moduli, some of which share a common key. Assuming the RSA key used to encrypt the message shares a common factor with another RSA modulus in the list, this weakness can be exploited to obtain its factors, find its private key, and use the key decrypt the encoded message.

The python scripts script1.py - script6.py decode the message step by step.
First, a simple for loop (script not included) is used to find the indices of all the RSA moduli that share a common key. The output is stored in stage0.txt.
script1.py elimimates all duplicate values from stage0.txt (eg index of i: 547 and index of j: 1386 and index of i: 1386 and index of j: 547). Outputs to stage1.txt.
script2.py uses gcd to find the factors of those moduli which share a common factor. Outputs to stage2.txt (human-readable, used for debugging) and stage3.txt (used in the next step).
script4.py uses the factors from stage3.txt to find the private key for the corresponding RSA moduli. Outputs to stage4.txt (human-readable, used for debugging) and stage5.txt (used in the next step). 
script6.py attempts to decrypt the message in 3.2.4_ciphertext.enc.asc using the private keys from stage5.txt. Decryptions which raise errors are discarded and the single correct decryption is output to stage6.txt.