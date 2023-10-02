import random
import collections
import itertools

with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

def select_word(words, length):
    suitable_words = [word for word in words if len(word) == length]
    return random.choice(suitable_words)

def scramble_word(word):
    scramble_word = random.sample(word, len(word))
    return ''.join(scramble_word)

def check_guess(guess, word, words):
    counter_word = collections.Counter(word)
    counter_guess = collections.Counter(guess)

    if counter_guess & counter_word == counter_guess and guess in words:
        return True
    return False

def play_game(low, high):
    length = random.randint(low, high)
    word = select_word(words, length)
    scrambled_word = scramble_word(word)

    guessed_words = []

    while True:
        print(f"\nScrambled word: {scrambled_word}")
        guess = input("Enter a guess: ")

        if guess == "quit":
            break

        if check_guess(guess, word, words):
            print("Correct!")
            guessed_words.append(guess)
            guessed_words.sort(key=lambda x: (len(x), x))
            print("\nGuessed words:")
            for key, group in itertools.groupby(guessed_words, key=len):
                print(f"{key} letters: {', '.join(list(group))}")
        else:
            print("Sorry. Try again.")

    print("\nEnd of the game.")

if __name__ == "__main__":
    low, high = map(int, input("Enter the range of word lengths (low,high): ").split(","))
    play_game(low, high)