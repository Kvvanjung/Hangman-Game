import random
WORDS = ["lion", "elephant", "kangaroo", "dolphin", "panda", "giraffe", "penguin", "tiger", "owl", "cheetah"]

# Select a word from WORDS
def select_word():
    return random.choice(WORDS)

# User input a guess
def make_guess():
 guess = input("Guess a letter:")
 return guess

def hangman_game():
    word = select_word()
    letters_to_guess = set(word)
    correct_guesses = set()
    wrong_guesses = set()
    life = 6
    guesses = 0

    print("\nWelcome to Hangman game!")
    print(f"The word has {len(word)} letters")

    while life > 0:
        # Diplay the current guessed word
        display_word = [ltr if ltr in correct_guesses else "_" for ltr in word]
        print("Current word: ", " ".join(display_word))
    
        guess = make_guess()
        guesses += 1

        # Check if the guess is correct
        if guess in letters_to_guess:
            correct_guesses.add(guess)
            letters_to_guess.remove(guess)
            print(f"\nCongrats, you guessed the letter {guess} right!")
        else: 
            wrong_guesses.add(guess)
            life -=1
            print(f"\nWrong guess! You have {life} lives left")

        print(f"{guesses} guessess have been made")
        print(f"correct: {len(set())} wrong:{guesses - len(set())}")

    # Tell the result
    if len(letters_to_guess) == 0:
        print(f"Congratulations, you guessed the word {word} right!")
    else:
        print(f"Hangman died! The word was '{word}'")

    # Ask if the player wants to retry
    retry = input("Retry? (Y/N):")
    if retry == "Y":
        hangman_game()
    else:
        print("Thanks for playing!")
            


def main():
    hangman_game()


if __name__=="__main__":
    main()