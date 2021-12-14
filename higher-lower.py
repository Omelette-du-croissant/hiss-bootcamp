import random
from art import logo
from game_data import data

#pick random person from data
def get_celeb():
  celeb =random.sample(data, 1)[0]
  return celeb

def play(random_a, random_b):
  guessed = False
  score = 0
  
  while not guessed:
    print(f'Compare \nA: {random_a["name"]}, a  {random_a["description"]} from {random_a["country"]}\nand\nB: {random_b["name"]}, a  {random_b["description"]} from {random_b["country"]}')
    guess = input("Who has more followers on Instagram?\n").lower()
    if guess == "a".lower() and float(random_a["follower_count"]) > float(random_b["follower_count"]):
      print("Correct!")
      score += 1
      print(f"Your score is {score}.")
      random_a = get_celeb()
      random_b = get_celeb()
    elif guess == "a".lower() and float(random_a["follower_count"]) < float(random_b["follower_count"]):
      print(f'Incorrect. {random_b["name"]} has more followers than {random_a["name"]}.')
      print(f'Your score is {score}.')
      guessed = True
    elif guess == "b".lower() and float(random_b["follower_count"]) > float(random_a["follower_count"]):
      print("Correct!")
      score += 1
      print(f"Your score is {score}.")
      random_a = get_celeb()
      random_b = get_celeb()
    else:
      print(f'Incorrect. {random_a["name"]} has more followers than {random_b["name"]}.')
      guessed = True

  if guessed:
    print(f"You lose. Your score is {score}. Better luck next time.")


def main():
  
  while input("Welcome to Higher or Lower. Would you like to play a game? [y/n]\n").lower() == "Y".lower():
    print("The computer will think of two accounts on Instagram. Your mission, should you accept it, is to guess who has more followers. Begin!")
    random_a=get_celeb()
    random_b=get_celeb()
    play(random_a, random_b)
    while input("Would you like to try again? [y/n]\n").lower() == "Y".lower():
      random_a=get_celeb()
      random_b=get_celeb()
      play(random_a, random_b)
    print("Goodbye.")
    

if __name__ == "__main__":
  main()





