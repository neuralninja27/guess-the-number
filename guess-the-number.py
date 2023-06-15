import random

num = random.randint(1, 100)
guesses = 10
print(f"You have {guesses} guesses to guess the correct number")

while(True):
    if guesses != 0:
        input_num = int(input("Guess the number: "))
        if input_num > num:
            print("Your guess is greater than the actual number. Try again.")
            guesses -= 1
            print(f"You have {guesses} guesses left")
            continue
        elif input_num < num:
            print("Your guess is less than the actual number. Try again.")
            guesses -= 1
            print(f"You have {guesses} guesses left")
            continue
        else:
            print("Congrats! You guessed the number correctly.")
            print(f"You finished the game with {guesses - 1} guesses left")
            break
    else:
        print("Game over :(")
        print(f"The number was {num}")
        break
