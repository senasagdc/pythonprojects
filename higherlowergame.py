#you will need the game data file for playing the game.
# We don't go forward with the winner. We always go with second one (Choice B)

import random
import time
import game_data

def choose_person():
    return (random.choice(game_data.data))

def compare(A,B):
    if int(A['follower_count']) >= int(B['follower_count']):
        return A
    else:
        return B


def game():
    correct_count = 0
    print("Welcome to Higher or Lower game!! Here is coming our first comparison!")
    time.sleep(1.2)
    first_person = choose_person()
    second_person = choose_person()
    should_continue = True

    while should_continue:
        print(f"Round {correct_count+1}")
        print(f"Compare A: {first_person['name']} , {first_person['description']} , from {first_person['country']}")
        print(r"""
         _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)
        """)
        print(f"Compare B: {second_person['name']} , {second_person['description']} , from {second_person['country']}")
        result = compare(first_person, second_person)
        player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if player_choice == 'A' and result == first_person:
            first_person = second_person
            second_person = choose_person()
            print("its true")
            correct_count += 1
        elif player_choice == 'B' and result == second_person:
            print("its true")
            first_person = second_person
            second_person = choose_person()
            correct_count += 1
        else:
            print(f"Game over. The answer was {result}. Your score is {correct_count}")
            play_again = input("if you wanna play again press 'R' ").lower()
            if play_again == "r":
                game()
            else:
                should_continue = False


game()

