import random
WORDS = ["lion", "elephant", "kangaroo", "dolphin", "panda", "giraffe", "penguin", "tiger", "owl", "cheetah"]

# Draw a gallows and person
def draw_hangman(life):
    drawing = [
        '''
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
        ---------
        ''',
        '''
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
        ---------
        ''',
        '''
            -----
            |   |
            O   |
           /|\\  |
                |
                |
        ---------
        ''',
        '''
            -----
            |   |
            O   |
           /|   |
                |
                |
        ---------
        ''',
        '''
            -----
            |   |
            O   |
            |   |
                |
                |
        ---------
        ''',
        '''
            -----
            |   |
            O   |
                |
                |
                |
        ---------
        ''',
        '''
            -----
            |   |
                |
                |
                |
                |
        ---------
        '''
    ]
    return drawing[life]

# Select a word from WORDS
def select_word():
    return random.choice(WORDS)

# User input a guess
def make_guess():
 guess = input("Guess a letter:").upper()
 return guess

def hangman_game():
    word = select_word().upper()
    letters_to_guess = set(word)
    correct_guesses = set()
    wrong_guesses = set()
    life = 6
    guesses = 0

    # Greet the player
    print("\n\033[1;32mWelcome to Hangman game!","\033[0m")
    print(f"The word has \033[1;32m{len(word)}\033[0m letters")

    while len(letters_to_guess) > 0 and life > 0:
        # Diplay the current guessed word
        display_word = [ltr if ltr in correct_guesses else "_" for ltr in word]
        print(draw_hangman(life))
        print("\033[1;32mCurrent word: ", " ".join(display_word), "\033[0m")
        print(f"{guesses} guessess have been made (correct : {len(correct_guesses)} wrong : {guesses - len(correct_guesses)})")
        print(f"wrong_guesses : \033[1;31m{', '.join(wrong_guesses)}\033[0m")

        guess = make_guess()
        guesses += 1

        # Check if the guess is correct
        if guess in letters_to_guess:
            correct_guesses.add(guess)
            letters_to_guess.remove(guess)
            print(f"\n\033[1;32mCongrats, you guessed the letter {guess} right!\033[0m")
        else: 
            wrong_guesses.add(guess)
            life -=1
            print(f"\n\033[1;32mWrong guess! You have \033[1;31m{life}\033[0m \033[1;32mlives left\033[0m")
            print(life)


    # Tell the result
    if life == 0:
        print(draw_hangman(life))
        print(f"\033[1;31mHangman died! The word was '{word}'\033[0m")
    else:
        print(f"\033[1;32mCongratulations, you guessed the word {word} right!\033[0m")
        

    # Ask if the player wants to retry
    retry = input("Retry? (Y/N):").upper()
    if retry == "Y":
        hangman_game()
    else:
        print("Thanks for playing!")
            


def main():
    hangman_game()


if __name__=="__main__":
    main()