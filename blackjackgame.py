import random
from art import logo
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    sum_cards = sum(cards)
    if sum_cards == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum_cards


def compare(userScore, compScore):
    if userScore == compScore:
        return ("It it draw")
    elif userScore == 0:
        return ("It is Blackjack!! You win")
    elif compScore == 0:
        return ("Computer did blackjack. You lose!")
    elif userScore > 21:
        return ("you lose!!")
    elif compScore > 21:
        return ("Computer went over. You win!")
    elif userScore > compScore:
        return ("You win!!")
    else:
        return ("You lose!!")


def main_game():
    print(logo)
    user_cards = []
    comp_cards = []
    game_over = False
    print("Cards are dealing...")
    time.sleep(1.0)

    for i in range(0,2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())
    print("Cards dealed!!!!!")

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards} and your score: {user_score}")
        print(f"Computer's first card is: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            will_continue = input("Do you want to get another card? Type 'y' for yes 'n' for no ")
            if will_continue == 'y':
                user_cards.append(deal_cards())
            else:
                game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score = calculate_score(comp_cards)

    print("Your final hand is being revealed...")
    time.sleep(1.1)
    print(f"Your final hand is {user_cards} and your score is {user_score}")
    print(f"Computers final hand is {comp_cards} and its score is {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    main_game()