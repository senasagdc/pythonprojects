import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 500,
    "milk": 300,
    "coffee": 200,
}

def is_enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def make_coffee(coffee_type):
    order_ingredients = MENU[coffee_type]["ingredients"]
    if is_enough_resources(order_ingredients):
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your {coffee_type}. Enjoy! ☕")

def is_enough_money(coins_inserted, coffee_cost):
    if coins_inserted >= coffee_cost:
        change = coins_inserted - coffee_cost
        print(f"Here is your change: ${change}")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def fill():
    print("Refilling resources...")
    resources["water"] += int(input("How much water to add?: "))
    resources["milk"] += int(input("How much milk to add?: "))
    resources["coffee"] += int(input("How much coffee to add?: "))
    time.sleep(1.0)
    print("Resources refilled!")

is_on = True
while is_on:
    user_wants = input("What would you like? (espresso/latte/cappuccino or report/off): ")
    if user_wants == "off":
        is_on = False
    elif user_wants == "Report".lower():
        print(f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} gr\nProfit: {profit}" )
    elif user_wants == "fill":
        fill()
    elif user_wants in MENU:
        if is_enough_resources(MENU[user_wants]['ingredients']):
            given_money = process_coins()
            if is_enough_money(given_money, MENU[user_wants]['cost']):
                make_coffee(user_wants)
            else:
                print("money refunded.")






