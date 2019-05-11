import random

def password_variations(password, count):

	CAPS_ODDS = 0.1
	NUMBER_END_ODDS = 0.35

	subs = {'a':[('4',5),('@',3)],
			'b':[('8',5)],
			'c':[('(',1)],
			#'d':,
			'e':[('3',8)],
			#'f':,
			'g':[('9',3),('6',1)],
			'h':[('#',3)],
			'i':[('1',4)],
			#'j':,
			#'k':,
			'l':[('1',10),('I',2),('!',1)],
			#'m':,
			#'n':,
			'o':[('0',12)],
			#'p':,
			#'q':,
			#'r':,
			's':[('5',8),('$',5)],
			't':[('+',3)],
			#'u':,
			#'v':,
			#'w':,
			#'x':,
			#'y':,
			'z':[('2',2)],
		}

	def append_random_number():
		'''Generates random number at end of password if needed'''
		rand = random.random()
		digits = 1
		if 0.7 < rand <= 0.9:
			digits = 2
		elif 0.9 < rand:
			digits = 3

		num_list = ['0','1','2','3','4','5','6','7','8','9']

		output = ''
		for digit in range(digits):
			output += random.choice(num_list)

		return output

	variations_list = []

	tries = 0

	while len(variations_list) < count:
		tries += 1
		if tries >= 2000:
			raise Exception('Too many tries')

		newpass = ''
		for i,char in enumerate(password):
			if i==0:
				if random.random() < CAPS_ODDS:
					newpass += char.upper()
					continue

			nextchar = char
			char_subs = subs.get(char)
			if char_subs != None:
				rand = random.random()*100
				for (sub, probability) in char_subs:
					rand -= probability
					if rand <= 0:
						nextchar = sub
						break
			newpass += nextchar

		#possibly append number to end
		if random.random() < NUMBER_END_ODDS:
			newpass += append_random_number()

		repeat = False

		for variation in variations_list:
			if newpass == variation: #repeat
				repeat = True
				break

		if not repeat:
			variations_list.append(newpass)

	return variations_list


if __name__ == '__main__':
	print(password_variations('password',20))
	print(password_variations('qwertyuiopasdfghjklzxcvbnm1234567890',20))
	print(password_variations('1qaz',20))




