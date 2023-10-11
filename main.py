import random

random_number = random.randint(1, 20)

def number_check(num):
    if num == random_number:
        print("You got it right! Great job!")
        exit(1)
    elif num > 20:
        print("The number has to be equal to or smaller than 20.")
    elif num < 1:
        print("The number has to be equal to or greater than 1.")
    elif 1 <= num < random_number:
        print("Your guess is smaller than the chosen number.")
    elif random_number < num <= 20:
        print("Your guess is greater than the chosen number.")
    else:
        print("I don't understand this input. Please try again.")
        exit(1)

print("Hello and welcome to the number guessing game.")

rules = input("\nWould you like to know the rules? (Y/N): ")

if rules.capitalize() == "Y" or rules.capitalize() == "Yes":
    print("\nOk, here are the rules:")
    print("1. The computer chooses a random number from 1 - 20")
    print("2. The user, you, have three chances to get it right.")
    print("3. If you get it right, you win.")
    print("4. If you don't get it right, you lose.")

elif rules.capitalize() == "N" or rules.capitalize() == "No":
    print("\nOk, I won't show you the rules.")
else:
    print("I don't understand this input. Please try again.")
    exit(1)

num1 = int(input("\nThe computer chose the random number. Enter your first guess: "))

number_check(num1)

num2 = int(input("\nTry again. Enter your second guess: "))

number_check(num2)

num3 = int(input("\nLast chance. Enter your third guess: "))

number_check(num3)

print(f"\nThe number was: {random_number}")
print("You lost. It's ok. Play again.")