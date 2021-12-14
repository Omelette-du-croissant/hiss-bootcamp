# Coffee machine options : latte (200 mL water + 2 g coffee + 15 ml milk), espresso (50 ml water + 18 g coffee), cappuccino (250 ml water + 24 g coffee + 100 ml milk)
# Different prices (espresso = 1.50, latte = 2.50, cappuccino = 3.00)
# hardware : Water inlet, coin slot, ADD contactless, coin acceptor, LCD display, drinks 1-2-3, +-, Menu, drink outlet, waste water box


coffee_cup = """


                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,'
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'


"""



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coins= [
    {
        'name': 'Penny',
        'value': 0.01
    },
    {
        'name': 'Nickel',
        'value': 0.05
    },
    {
        'name': 'Dime',
        'value': 0.1
    },
    {
        'name': 'Quarter',
        'value': 0.25
    }]
    

def can_make_coffee(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Not enough {item}.")
            return False
    return True
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    

profit = 0

print("Welcome to Viper Coffee Co.")

is_on = True
while is_on:
    choice = input("What would you like to order?")
    if choice == "off":
        is_on = False
        print("Now turning off.")
    elif choice == "report":
        print(f"Water: {resources['water']} mL.")
        print(f"Milk: {resources['milk']} mL.")
        print(f"Coffee: {resources['coffee']} g.")
        print(f"Money: ${profit}.")
    else:
        drink = MENU[choice]
        if can_make_coffee(drink["ingredients"]):
            print(f"You have ordered a {choice}. That will be {drink['cost']}$.")
            
            
            pennies = 0
            nickels = 0
            dimes = 0
            quarters = 0
    
            inserted = 0
    
    
            price_met = False
            while not price_met:
        
                insert = input("What would you like to insert in the coin slot? [penny/nickel/dime/quarter]\n").title()
                if insert == "Penny".title():
                    pen_amount = input("How many pennies? ")
                    pennies += int(pen_amount)
                elif insert == "Nickel".title():
                    nic_amount = input("How many nickels? ")
                    nickels += int(nic_amount)
                elif insert == "Dime".title():
                    dim_amount = input("How many dimes? ")
                    dimes += int(dim_amount)
                elif insert == "Quarter".title():
                    quar_amount = input("How many quarters? ")
                    quarters += int(quar_amount)
                inserted = (float(pennies) * float(coins[0]['value'])) + (float(nickels) * float(coins[1]['value'])) + (float(dimes) * float(coins[2]['value'])) + (float(quarters) * float(coins[3]['value']))
                print(f"${round(inserted,2)}")
        
                if float(inserted) >= float(drink['cost']):
                    price_met = True
                    
                    make_coffee(choice, drink['ingredients'])
                    
                    if not can_make_coffee(drink["ingredients"]):
                        refill = input("Type 'refill' to refill.\n").lower()
                        if refill == "refill".lower():
                            print("Refilling.")
                            resources["water"] = 300
                            resources["coffee"] = 100
                            resources["milk"] = 200
                        
                        
                    
                    profit += drink["cost"]
                    print(f"One {choice} coming right up. Please wait.")
                    print(coffee_cup)
                    change = float(inserted) - float(drink['cost'])
                    if float(change) > 0:
                        print(f"Clink. Don't forget your change: ${round(change,2)}")
        



