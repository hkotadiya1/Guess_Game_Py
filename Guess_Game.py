from random import randint
#print(randint(1,10))
answer = randint(1,10)
while True:
    try:
        guess = int(input("Enter a number : "))
        if 0 < guess < 11 and guess == answer:
            print("You Won!")
            break
        else:
            print("Enter a valid number.")
            continue
    except ValueError:
        print("Enter an integer value.")

