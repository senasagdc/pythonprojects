import random
import time

def number_generator():
    print("Computer thinks a number between 1 and 100 ")
    time.sleep(0.55)
    comp_number = random.randint(1,101)
    return comp_number

def choose_difficulty():
    player_choice = input("Choose a difficulty. 'easy' or 'hard' ")
    if player_choice == "easy":
        return 10
    elif player_choice == "hard":
        return 5
    else:
        return ("Invalid choice")


def game():
    print("Welcome to the Number Guessing Game!")
    comp_no = number_generator()
    difficulty = choose_difficulty()
    user_guess = 0
    while user_guess != comp_no and difficulty > 0:
        print(f"You have {difficulty} attempts")
        user_guess = int(input("Make a guess: "))
        if user_guess > comp_no:
            print("Too high!")
            difficulty -= 1
        elif user_guess < comp_no:
            print("Too low!")
            difficulty -= 1
        else:
            print("You guessed correct! Congrats!")
            return
    if difficulty == 0:
        print("You've run out of guesses, you lose.")
        return

game()