import random

word_list = ["aardvark","camel","baboon"]

def get_word():
  word = random.choice(word_list)
  return word.upper()

def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print(f"Let\'s play Hangman.\n{disp_hangman(tries)}\n{word_completion}\n")
  while not guessed and tries > 0:
    guess = input("Guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print(f"Already guessed {guess}.")
      elif guess not in word:
        print(f"Nope.")
        tries -= 1
        guessed_letters.append(guess)
      else:
        print(f"Yoohoo.")
        guessed_letters.append(guess)
        listed_word = list(word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          listed_word[index] = guess
        word_completion = "".join(listed_word)
        if "_" not in word_completion:
          guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print(f"Already guessed {guess}.")
      elif guess != word:
        print(f"Nope.")
        tries -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        word_completion = word

    else:
      print("Invalid guess.")
    print(f"{disp_hangman(tries)}\n{word_completion}\n")
  
  if guessed:
    print("You win!")
  else:
    print(f"You ran out of tries. The word was {word}. You lose!")

def disp_hangman(tries):
  stages = ["""
                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========
            """, 
            """
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========
            """, 
            """
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========
            """, 
            """
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========
            """, 
            """
                  +---+
                  |   |
                  O   |
                 /|\  |
                      |
                      |
                =========
            """, 
            """
                  +---+
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |
                =========
            """, 
            """
                  +---+
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
                =========
            """]
  return stages[-tries -1]

def main():
  word = get_word()
  play(word)
  while input("Do you want to play again? [Y/N]\n").upper() == "Y":
    word = get_word()
    play(word)

if __name__ == "__main__":
  main()
