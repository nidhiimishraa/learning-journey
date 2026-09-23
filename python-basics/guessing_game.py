import random

number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == number:
        print("🎉 Correct! You guessed it!")
        print("You got it in", attempts, "attempts!")
        break
    elif guess < number:
        print("📈 Try a higher number!")
    else:
        print("📉 Try a lower number!")
