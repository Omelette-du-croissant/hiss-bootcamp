import random

def get_number():
  number = random.randint(1,50)
  return number

def game(number):
  guessed = []
  difficulty = input("Choose your difficulty. Easy or Hard?\n").lower()
  if difficulty == "Easy".lower():
    tries = 10
  elif difficulty == "Hard".lower():
    tries = 5
  else:
    print("That's not a valid difficulty. Please choose Easy or Hard. \n")
    return
  print("The computer is thinking of a number.\n...")
  guessed = False
  while not guessed and tries > 0:
    guess = input("Guess the number. ")

    if float(guess) > float(number):
      print("Too high.")
      tries -= 1
      print(f"You have {tries} tries left.")
    elif float(guess) < float (number):
      print("Too low.")
      tries -= 1
      print(f"You have {tries} tries left.")
    elif float(guess) == float(number):
      print("Correct!")
      guessed = True
       
  if guessed and tries == 1:
    print(f"You win with {tries} try left!")
  elif guessed:
    print(f"You win with {tries} try left!")
  else:
    print(f"You ran out of tries. The number was {number}. You lose!")
    
def main():
  number = get_number()
  game(number)
  while input("Would you like to try again? [y/n]\n").lower() == "Y".lower():
    number = get_number()
    game(number)
  print("Goodbye.")

if __name__ == "__main__":
  main()
    
    
  

