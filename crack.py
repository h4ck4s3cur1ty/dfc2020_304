import hashlib
import itertools

enc_flag = 'F87EDB663F3A0F51B900360F5331E7133FF4D5A4B9B25FD8874878B81D377A'

for i in itertools.product(xrange(10), repeat=3):
	for j in itertools.product(xrange(10), repeat=3):
		pin1 = ''.join(str(pins) for pins in i)
		pin2 = ''.join(str(pins) for pins in j)
		hashed_pin1 = hashlib.sha256(pin1).hexdigest()
		hashed_pin2 = hashlib.sha256(pin2).hexdigest()

		tmp = ''
		for k in range(len(enc_flag)/2):
			xor_hash = int(hashed_pin1[k*2:][:2], 16) ^ int(hashed_pin2[k*2:][:2], 16)
			tmp += '{0:02X}'.format(xor_hash)
			if tmp[::-1] == enc_flag:
				print '[*] Found !'
				print '[*] KEY : ' + pin1 + pin2