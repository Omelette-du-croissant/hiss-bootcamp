#Write your code below this line 👇

def prime_checker(number):
    isprime = 0
    if number > 1:
        for i in range(2, int(number/2)):
            if number%i == 0:
                isprime=1
                break
        if isprime == 0:
            print("It's a prime number.")
        elif isprime == 1:
            print("It's not a prime number.")
    else:
        print("It's not a prime number.")


#TEST
#n = int(input("Check this number: "))
#prime_checker(number=n)
