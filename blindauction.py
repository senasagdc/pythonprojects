is_other_bidders = "yes"
bid_dict = {}

while is_other_bidders == ("yes"):
    user_name = input("Welcome! What is your name? ")
    user_bid = input("What is your bid? ")
    bid_dict[user_name] = int(user_bid)
    is_other_bidders = input("Are there any other bidders? 'yes' or 'no' ")
    if is_other_bidders == "no":
        print(f"the bids are: {bid_dict}")
        who_is_winner = max(bid_dict, key = bid_dict.get)
        print("so the winner is " + who_is_winner )