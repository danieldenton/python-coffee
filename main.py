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

def make_espresso():
    global resources
    global OUT_OF_RESOURCES
    if resources["water"] < 50:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
    elif resources["coffee"] < 18:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
    resources["water"] - 50
    resources["coffee"] - 18
    return resources


def make_latte():
    global resources
    global OUT_OF_RESOURCES
    if resources["water"] < 200:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
    elif resources["milk"] < 150:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
    elif resources["coffee"] < 24:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
    else:
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    return resources


def make_cappuccino():
    global resources
    global OUT_OF_RESOURCES
    if resources["water"] < 250:
        print("I'm sorry there's not enough water.")
        OUT_OF_RESOURCES = True
    elif resources["milk"] < 100:
        print("I'm sorry there's not enough milk.")
        OUT_OF_RESOURCES = True
    elif resources["coffee"] < 24:
        print("I'm sorry there's not enough coffee.")
        OUT_OF_RESOURCES = True
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
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

while not OUT_OF_RESOURCES:
    SELECTION = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if SELECTION == "espresso":
        make_espresso()
    elif SELECTION == "latte":
        make_latte()
    elif SELECTION == "cappuccino":
        make_cappuccino()
    else:
        SELECTION = input("Please make a valid selection (espresso/latte/cappuccino): ").lower()
    if OUT_OF_RESOURCES == False:
        calculate_cost()














