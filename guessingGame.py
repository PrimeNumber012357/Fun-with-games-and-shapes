import random

def guess(x):
    random_number = random.randint(1,x)
    i= 0
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: ")) #get user guess
            if guess < 1 or guess > x:
                print("You didn't enter an integer in the chose range")
            elif guess < random_number:
                print("Sorry you're too low")
                i += 1 #increment guess count
            elif guess > random_number:
                print("Woah that's too high!")
                i += 1 #increment guess count
            else:
                i += 1 #increment guess count
                print(f"Nice, you guessed the number {random_number}.  And it took you {i} tries.")
        except ValueError: #make sure guess is valid
            print("You didn't enter an integer in the chosen range")
        except TypeError: #make sure guess is valid
            print("You didn't enter an integer in the chosen range")


#pick the range from 1 up to x and start guessing!
#guess(1000)