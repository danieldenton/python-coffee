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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

OUT_OF_RESOURCES = False


def check_selection(word):
    valid_selection = False
    for drink in MENU:
        if drink == word:
            valid_selection = True
    if valid_selection == False:
        word = input("Please make a valid selection. (espresso/latte/cappuccino): ").lower()
    return word


def make_drink():
    global OUT_OF_RESOURCES
    if resources["water"] < MENU[SELECTION]["ingredients"]["water"]:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
    elif resources["coffee"] < MENU[SELECTION]["ingredients"]["coffee"]:
        print("I'm sorry there's not enough coffee.")
        OUT_OF_RESOURCES = True
    resources["water"] -= MENU[SELECTION]["ingredients"]["water"]
    resources["coffee"] -= MENU[SELECTION]["ingredients"]["coffee"]
    if SELECTION == "espresso":
        pass
    elif resources["milk"] < MENU[SELECTION]["ingredients"]["milk"]:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
        resources["milk"] -= MENU[SELECTION]["ingredients"]["milk"]
    return resources


def calculate_cost():
    num_quarters = int(input("how many quarters? "))
    num_dimes = int(input("how many dimes? "))
    num_nickels = int(input("how many nickels? "))
    num_pennies = int(input("how many pennies? "))
    total_coins = (num_quarters * .25) + (num_dimes * .1) + (num_nickels * .05) + (num_pennies * .01)
    transaction = total_coins - MENU[SELECTION]["cost"]
    if transaction < 0:
        print(f"The {SELECTION} costs {MENU[SELECTION]['cost']}. You only put {total_coins}.\n Here is you're refund.")
    elif transaction == 0:
        print(f"Here's your {SELECTION}")
    else:
        print(f"Here's your {SELECTION}. Your change is {transaction}")


while OUT_OF_RESOURCES == False:
    SELECTION = input("What would you like? (espresso/latte/cappuccino): ").lower()
    valid_selection = False
    for drink in MENU:
        if drink == SELECTION:
            valid_selection = True
    if valid_selection == True:
        make_drink()
        if OUT_OF_RESOURCES == False:
            calculate_cost()























