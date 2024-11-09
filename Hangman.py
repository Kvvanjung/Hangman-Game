import random
WORDS = ["lion", "elephant", "kangaroo", "dolphin", "panda", "giraffe", "penguin", "tiger", "owl", "cheetah"]

def select_word():
    return random.choice(WORDS)

def make_guess():
 guess = input("Guess a letter:")
 return guess

def hangman_game():
    word = select_word()
    correct_guesses = []
    wrong_guesses = []
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters")
    guess = make_guess()


def main():
    hangman_game()


if __name__=="__main__":
    main()