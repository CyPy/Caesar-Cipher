
alphabets = "abcdefghijklmnopqrstuvwxyz"

class caesar:
	def encode(plaintext, key):
		plaintext = plaintext.lower()
		ciphertext = ""
		for i in plaintext:
			if (alphabets.find(i) != -1):
				finalIndex = (alphabets.find(i) + key) % 26
				ciphertext += alphabets[finalIndex]
			else:
				ciphertext += i
		print ciphertext

	def decode(ciphertext, key):
		ciphertext = ciphertext.lower()
		plaintext = ""
		for i in ciphertext:
			if (alphabets.find(i) != -1):
				finalIndex = (abs(alphabets.find(i) - key)) % 26
				plaintext += alphabets[finalIndex]
			else:
				plaintext += i
		print plaintext



