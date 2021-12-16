class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")


class CoffeeMachine:
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

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Not enough {item}.")
                can_make = False
        return can_make

    def refill(self):
        refill = input("Type 'refill' to refill.\n").lower()
        if refill == "refill".lower():
            print("Refilling.")
            self.resources["water"] = 300
            self.resources["coffee"] = 100
            self.resources["milk"] = 200

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"One {order.name} coming right up.\n{self.coffee_cup}\nHere's your {order.name}. Enjoy!")


class MoneyMachine:
    CURRENCY = "$"

    coins = [
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

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def make_payment(self, cost):
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
            inserted = (float(pennies) * float(self.coins[0]['value'])) + (float(nickels) * float(self.coins[1]['value'])) + (
                    float(dimes) * float(self.coins[2]['value'])) + (float(quarters) * float(self.coins[3]['value']))
            print(f"${round(inserted, 2)}")
            if float(inserted) >= float(drink.cost):
                price_met = True
                self.profit += drink.cost
                change = float(inserted) - float(drink.cost)
                if float(change) > 0:
                    print(f"Clink. Don't forget your change: ${round(change, 2)}")


print("Welcome to Viper Coffee Co.")

is_on = True
stevie = CoffeeMachine()
counter_prompt = MoneyMachine()
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"Enter order. \n{options}\n")
    if choice == "off":
        is_on = False
        print("Turning off.")
    elif choice == "report":
        stevie.report()
        counter_prompt.report()
    else:
        drink = menu.find_drink(choice)
        if stevie.is_resource_sufficient(drink):
            counter_prompt.make_payment(drink.cost)
            stevie.make_coffee(drink)
        else:
            stevie.refill()
            stevie.make_coffee(drink)
