import random

tries = 3
randomNum = random.randrange(1, 10)

while tries > 0:
    print("try # ", tries)    
    tries -= 1

    guess = int(input("Guess a number: "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range.")
        print("You have ", tries, "remaining attempts")
    elif guess > randomNum:
        print("The number you guessed is greater than the correct number")
    elif guess < randomNum:
        print("The number you guessed is smaller than the correct number")
    else:
        print("Bingo")
        break
if guess != randomNum:    
    print("You have used all 3 attempts.")
    
print("The correct number was:", randomNum)