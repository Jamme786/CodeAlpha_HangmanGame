import random

words = ["python", "coding", "laptop", "mouse", "keyboard"]

word = random.choice(words)

guessed_letters = []
attempts = 6
display_word = ["_"] * len(word)

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print("Wrong Guess! Attempts left:", attempts)

if "_" not in display_word:
    print("\nYou Win! The word was:", word)
else:
    print("\nGame Over! The word was:", word)