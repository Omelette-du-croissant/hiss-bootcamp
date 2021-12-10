rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

rps=[0,1,2]
gen = random.choice(rps)
if gen == 0:
  computer = rock
elif gen ==1:
  computer = paper
elif gen == 2:
  computer = scissors

user=input("Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
if user == "0":
  user = rock
elif user == "1":
  user = paper
elif user == "2":
  user = scissors
  
if user == computer:
  print(f"You chose:\n{user}\nComputer chose:\n{computer}\nDraw.")
    
elif user == rock and computer == paper:
  print(f"You chose:\n{user}\nComputer chose:\n{computer}\nYou lose.")
      
elif user == rock and computer == scissors:
  print(f"You chose:\n{user}\nComputer chose:\n{computer}\nYou win!")
      
elif user == paper and computer == rock:
  print(f"You chose:\n{user}\nComputer chose:\n{computer}\nYou win!")
      
elif user == paper and computer == scissors:
  print(f"You chose:\n{user}\nComputer chose:\n{computer}\nYou lose.")
        
elif user == scissors and computer == paper:
  print(f"You chose:\n{user}\nComputer chose:\n{computer}\nYou win!")
      
elif user == scissors and computer == rock:
  print(f"You chose:\n{user}\nComputer chose:\n{computer}\nYou lose.")
  
#ADD GAME LOOP
