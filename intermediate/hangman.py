# ----------- HANGMAN GAME -----------

import random

words = ["python", "internship", "hangman", "computer", "programming"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You guessed the word correctly!")
        break

    guess = input("Enter a letter: ").lower()

    # validation
    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single valid letter!")
        continue

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")
    else:
        print("Correct guess!")

# final result
if attempts == 0:
    print(f"\nGame Over! The word was: {word}")