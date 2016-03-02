
print("Guess a number between 1 and 50.")
print("you have just five chances to make a right guess.")

import random
number = random.randint(1, 50) # setting the range for the random integer
guess = int(input("Make a guess: ")) # to take the input of the guesser
attempts = 1

# The condition loop for guesses
while guess != number:
    if guess < number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    guess = int(input("Make a guess: "))
    attempts += 1 #Attempts counter
    if attempts == 5:
        print ("Sorry, you have made five failed attempts!")
        break
    if guess == number:
        print("Your guess was right in " + str(attempts) + " attempts!")