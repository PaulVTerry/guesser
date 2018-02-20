import random

secret_number = random.randint(0, 100)

guess = -1
number_of_guesses = 1

while secret_number != guess:
	if number_of_guesses <= 10:
		print "Guess number " + str(number_of_guesses) + "/10"
		guess = int(raw_input('Enter a number:'))
		if guess < secret_number:
			print guess
			print "Your guess is low, try again!"
			number_of_guesses = number_of_guesses + 1
		elif guess > secret_number:
			print guess
			print "Your guess is high, try again!"
			number_of_guesses = number_of_guesses + 1
		else:
			print "You guessed right!"
	else:
		print "You're out of guesses"
		break