print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_ 
*******************************************************************************
''')


def game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 
    print('You\'re at a crossroad. Where do you want to go?\n')

    cross = input()
    if cross == 'right':
        print("You fell down a rabbit hole! Game Over.")
        return 
    elif cross == 'left':
        swim_or_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
        while True:
            if swim_or_wait == 'swim':
                print("You got attacked by a shrimp! Game Over.")
                return 
            elif swim_or_wait == 'wait':
                door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
                while True:
                  if door == 'blue':
                    print('You enter a room of murderous kittens. Game Over.')
                    return 
                  elif door == 'red':
                    print('The room is on fire! This is not fine, Game Over.')
                    return 
                  elif door == 'yellow':
                    print('You found the treasure! You Win.')
                  
                  else:
                    door = input('You chose a door that doesn\'t exist. Try again.')
                    while True:
                      if door == 'blue':
                        print('You enter a room of murderous kittens. Game Over.')
                        return 
                      elif door == 'red':
                        print('The room is on fire! This is not fine, Game Over.')
                        return 
                      elif door == 'yellow':
                        print('You found the treasure! You Win.')
                        return

            else:
                swim_or_wait = input('Sorry none can do.  Do you want to "swim" or "wait"?\n')
                while True:
                  if swim_or_wait == 'swim':
                    print("You got attacked by a shrimp! Game Over.")
                    return 
                  elif swim_or_wait == 'wait':
                    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
                    while True:
                      if door == 'blue':
                        print('You enter a room of murderous kittens. Game Over.')
                        return 
                      elif door == 'red':
                        print('The room is on fire! This is not fine, Game Over.')
                        return 
                      elif door == 'yellow':
                        print('You found the treasure! You Win.')
                      else:
                        door = input('You chose a door that doesn\'t exist. Try again.')
                        while True:
                          if door == 'blue':
                            print('You enter a room of murderous kittens. Game Over.')
                            return 
                          elif door == 'red':
                            print('The room is on fire! This is not fine, Game Over.')
                            return 
                          elif door == 'yellow':
                            print('You found the treasure! You Win.')
                            return
                
    else:
        cross = input('There is no turning back. Do you want to go right or left?\n')
        if cross == 'right':
          print("You fell down a rabbit hole! Game Over.")
          return 
        elif cross == 'left':
          swim_or_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
          while True:
            if swim_or_wait == 'swim':
              print("You got attacked by a shrimp! Game Over.")
              return 
            elif swim_or_wait == 'wait':
                door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
                while True:
                  if door == 'blue':
                    print('You enter a room of murderous kittens. Game Over.')
                    return 
                  elif door == 'red':
                    print('The room is on fire! This is not fine, Game Over.')
                    return 
                  elif door == 'yellow':
                    print('You found the treasure! You Win.')
                  else:
                    door = input('You chose a door that doesn\'t exist. Try again.')
                  while True:
                    if door == 'blue':
                      print('You enter a room of murderous kittens. Game Over.')
                      return 
                    elif door == 'red':
                      print('The room is on fire! This is not fine, Game Over.')
                      return 
                    elif door == 'yellow':
                      print('You found the treasure! You Win.') 
                      return

            else:
                swim_or_wait = input('Sorry none can do.  Do you want to "swim" or "wait"?\n')
            while True:
              if swim_or_wait == 'swim':
                print("You got attacked by a shrimp! Game Over.")
                return 
              elif swim_or_wait == 'wait':
                door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
                while True:
                  if door == 'blue':
                    print('You enter a room of murderous kittens. Game Over.')
                    return 
                  elif door == 'red':
                    print('The room is on fire! This is not fine, Game Over.')
                    return 
                  elif door == 'yellow':
                    print('You found the treasure! You Win.')
                  else:
                    door = input('You chose a door that doesn\'t exist. Try again.')
                    while True:
                      if door == 'blue':
                        print('You enter a room of murderous kittens. Game Over.')
                        return 
                      elif door == 'red':
                        print('The room is on fire! This is not fine, Game Over.')
                        return 
                      elif door == 'yellow':
                        print('You found the treasure! You Win.') 
                        return

        

while input('Do you want to play a game? [y/n]\n') == 'y':
    game()
    break      
    





