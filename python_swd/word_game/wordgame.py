import random
from collections import Counter
import sys

def select_word(words, length):
    suitable_words = [word for word in words if len(word) == length]
    return random.choice(suitable_words)

def scramble_word(word):
    scramble_word = random.sample(word, len(word))
    return ''.join(scramble_word)

def check_guess(guess, word, possible_words):
    counter_word = Counter(word)
    counter_guess = Counter(guess)

    if len(guess) in possible_words and counter_guess & counter_word == counter_guess and guess in possible_words[len(guess)]:
        return True
    return False

def generate_possible_words(word, low, high, words):
    possible_words = {i: [] for i in range(low, high+1)}
    counter_word = Counter(word)

    for w in words:
        if low <= len(w) <= high:
            counter_w = Counter(w)
            if counter_w & counter_word == counter_w:
                possible_words[len(w)].append(w)

    return possible_words

def play_game(low, high, base_word=None):
    with open('words.txt', 'r') as file:
        words = [line.strip() for line in file]

    if base_word is None:
        length = random.randint(low, high)
        word = select_word(words, length)
    else:
        word = base_word

    possible_words = generate_possible_words(word, low, high, words)
    guessed_words = {i: [] for i in range(low, high+1)}
    all_guesses = []

    while True:
        scrambled_word = scramble_word(word)

        print(f"{scrambled_word}\n")
        for length in range(low, high+1):
            words = possible_words[length] + guessed_words[length]
            words.sort()
            words_to_print = ', '.join([f"'{'-'*length}'" if word not in guessed_words[length] else f"'{word}'" for word in words])
            if (len(words_to_print) > 0):
                print(f"[{words_to_print}]")

        guess = input("Enter a guess: ")

        if guess == "q":
            break

        all_guesses.append(guess)

        if check_guess(guess, word, possible_words):
            print("Correct!\n")
            possible_words[len(guess)].remove(guess)
            guessed_words[len(guess)].append(guess)
            if all(len(words) == 0 for words in possible_words.values()):
                print("Congratulations, you've guessed all the words!")
                break
        else:
            print("Sorry. Try again.\n")

    all_guesses.sort()
    print(f"\n{repr(all_guesses)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        base_word = sys.argv[1]
        low, high = 1, len(base_word)
    else:
        low, high = map(int, input("Enter the range of word lengths (low,high): ").split(","))
        base_word = None

    play_game(low, high, base_word)