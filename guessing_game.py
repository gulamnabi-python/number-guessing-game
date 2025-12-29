import random

print("=== Number Guessing Game ===")
print("I am thinking of a number between 1 and 50")

secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
