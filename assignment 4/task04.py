import random
secret_number = random.randint(1,10)
print("I'm thinking of a number between 1 and 10.")
guess = 0
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10.")
    elif guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")

print("Correct! You guessed the number.")