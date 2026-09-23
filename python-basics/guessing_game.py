import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
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

if attempts == max_attempts and guess != number:
    print("😢 Game over! The number was", number)
