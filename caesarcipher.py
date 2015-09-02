"""
Functions to encode and decode Caesar ciphers given
the numerical key.
If the character in the plaintext/ciphertext is not
an alphabet, then the character is left untouched.

"""
alphabets = "abcdefghijklmnopqrstuvwxyz"

__all__= ['encode']

def encode(plaintext, key):
	"""
	Encodes the plaintext using the key provided and 
	returns the ciphertext.
	"""
	plaintext = plaintext.lower()
	ciphertext = ""
	for i in plaintext:
		if (alphabets.find(i) != -1):
			finalIndex = (alphabets.find(i) + key) % 26
			ciphertext += alphabets[finalIndex]
		else:
			ciphertext += i
	return ciphertext

def decode(ciphertext, key):
	"""
	Decodes the ciphertext using the key provided and
	returns the plaintext.
	"""
	ciphertext = ciphertext.lower()
	plaintext = ""
	key = key%26
	for i in ciphertext:
		if (alphabets.find(i) != -1):
			if ((alphabets.find(i) - key) > 0):
				finalIndex = (alphabets.find(i) - key)
			else:
				finalIndex = (alphabets.find(i) - key + 26)
			plaintext += alphabets[finalIndex]
		else:
			plaintext += i
	return plaintext



