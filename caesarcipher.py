
alphabets = "abcdefghijklmnopqrstuvwxyz"

__all__= ['encode']

def encode(plaintext, key):
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



