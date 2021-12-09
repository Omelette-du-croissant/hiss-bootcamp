bill = float(input('What was the total bill? \n$'))
tip = float(input('What percentage tip would you like to give?\n'))
people = float(input('How many people to split the bill?\n'))
print(f'The bill is ${round(bill)} with {round(tip)}% tip. The bill is split {round(people)} ways.')
per_person = (bill/people)*((100+tip)/100)
              
rounded = '{0:.2f}'.format(per_person)
print(f'Each person should pay ${rounded}.')