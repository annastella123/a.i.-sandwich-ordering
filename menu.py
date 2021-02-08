
BLT_MENU_ITEM = """We have our BLT, which is of course bacon, lettuce and tomato 
        on white bread with a touch of mayo."""

ANNA_MENU_ITEM = """Anna's Spicy comes with thin sliced turkey, provolone cheese, 
        lettuce and some of our signature chipotle sauce all on our very popular wheat bread."""

MOM_MENU_ITEM = """Mom's Healthy Lunch sandwich is gluten-free bread, chicken, spinach, tomato, 
        cucumber, smoked gouda cheese and a splash of vinegarette."""

DAD_MENU_ITEM = """Dad's sandwich is ham and cheddar with lettuce, tomato and mustard on wheat bread."""

BLT = {
    "name": "BLT",
    "bread": "white",
    "meat": ["bacon"],
    "veggies": ["lettuce", "tomato"],
    "cheese": [],
    "sauce": ["mayo"],
    "toasted": "not toasted",
    "extras": ["no extras"]
    }

ANNA = {
    "name": "Anna's Spicy",
    "bread": "wheat",
    "meat": ["turkey"],
    "veggies": ["lettuce"],
    "cheese": ["provolone"],
    "sauce": ["chipotle"],
    "toasted": "",
    "extras": ["no extras"]
    }

MOM = {
    "name": "Mom's Healthy Lunch",
    "bread": "gluten-free",
    "meat": ["chicken"],
    "veggies": ["spinach", "tomato", "cucumber"],
    "cheese": ["gouda"],
    "sauce": ["vinegarette"],
    "toasted": "",
    "extras": ["no extras"]
    }

DAD = {
    "name": "Dad's",
    "bread": "wheat",
    "meat": ["ham"],
    "veggies": ["lettuce", "tomato"],
    "cheese": ["cheddar"],
    "sauce": ["mustard"],
    "toasted": "",
    "extras": ["no extras"]
    }

BREAD = ["white", "wheat", "gluten-free"]

MEAT = ["bacon", "turkey", "chicken", "ham"]

VEGGIES = ["lettuce", "tomato", "spinach", "cucumber"]

CHEESE = ["provolone", "gouda", "cheddar"]

SAUCE = ["mayo", "chipotle", "vinegarette", "mustard"]

DIFF_BREAD = "What kind of bread do you want? We have: ", BREAD

DIFF_MEAT = "What kind of meat do you want? We have: ", MEAT

DIFF_VEGGIES = "Which veggies do you want? We have: ", VEGGIES

DIFF_CHEESE = "What kind of cheese do you want? We have: ", CHEESE

DIFF_SAUCE = "What kind of sauce do you want? We have: ", SAUCE

ALL_SANDWICHES = "\nMenu:\n\n" + BLT_MENU_ITEM + "\n\n" + ANNA_MENU_ITEM + "\n\n" + MOM_MENU_ITEM + "\n\n" + DAD_MENU_ITEM + "\n\n"

