secret_num = 9
for i in range(1,6):
    guess = int(input("Guess the number from 1 to 10:"))
    if guess == secret_num:
        print("You won!")
        break
    elif guess < secret_num :
        print("Too low!Try again")
    elif guess > secret_num :
            print("Too high!Try again")
    else:
        print("Sorry you used all chances!!")