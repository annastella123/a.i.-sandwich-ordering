import re
import constants
import menu

def process_response(response):
    strip_response = re.sub(r'[^\w\s]', '', response)
    response_list = strip_response.split()
    keywords = []
    for word in response_list:
        if word in constants.RESPONSES:
            if word not in keywords:
                keywords.append(constants.RESPONSES[word])
    return keywords

def see_menu():
    response = (input("\n\nWould you like to see a menu?   ")).lower()
    keywords = process_response(response)
    if "yes" in keywords:
        print(menu.ALL_SANDWICHES)
    return keywords

def order():
    response = (input("\n\nWhich sandwich would you like? (You can modify any sandwich element later.)   ")).lower()
    keywords = process_response(response)
    sandwich = {
        "name": "",
        "bread": "",
        "meat": [],
        "veggies": [],
        "cheese": [],
        "sauce": [],
        "toasted": "",
        "extras": []
    }
    if "blt" in keywords:
        sandwich = menu.BLT
    elif "anna" in keywords:
        sandwich = menu.ANNA
    elif "mom" in keywords:
        sandwich = menu.MOM
    elif "dad" in keywords:
        sandwich = menu.DAD
    if "more" in keywords:
        print(menu.ALL_SANDWICHES)

    holds = []
    for word in keywords:
        if word in constants.HOLD or word in constants.NO:
            hold_index = keywords.index(word)
            holds.append(hold_index)
    if holds:
        for word in keywords:
            if word in menu.BREAD:
                if  sandwich["bread"] is word and ((keywords.index(word) - 1) in holds or (keywords.index(word) - 2) in holds):
                    sandwich["bread"] = ""
                else: 
                    sandwich["bread"] = word
            if word in menu.MEAT:
                if  word in sandwich["meat"] and ((keywords.index(word) - 1) in holds or (keywords.index(word) - 2) in holds):
                    sandwich["meat"].remove(word)
                else:
                    sandwich["meat"].append(word)
            if word in menu.VEGGIES:
                if word in sandwich["veggies"] and ((keywords.index(word) - 1) in holds or (keywords.index(word) - 2) in holds):
                    sandwich["veggies"].remove(word)
                else:
                    sandwich["veggies"].append(word)
            if word in menu.CHEESE:
                if word in sandwich["cheese"] and ((keywords.index(word) - 1) in holds or (keywords.index(word) - 2) in holds):
                    sandwich["cheese"].remove(word)
                else:
                    sandwich["cheese"].append(word)
            if word in menu.SAUCE:
                if word in sandwich["sauce"] and ((keywords.index(word) - 1) in holds or (keywords.index(word) - 2) in holds):
                    sandwich["sauce"].remove(word)
                else:
                    sandwich["sauce"].append(word)
            if word is "toasted":
                if (keywords.index(word) - 1) in holds:
                    sandwich["toasted"] = "not toasted"
                else:
                    sandwich["toasted"] = "toasted"
            if word is "extra":
                if (keywords.index(word) - 1) in holds or (keywords.index(word) - 2) in holds:
                    sandwich["extras"] = "no extras"

    else:
        for word in keywords:
            if word in menu.BREAD and sandwich["bread"] is not word:
                sandwich["bread"] = word
            if sandwich["meat"] and word in menu.MEAT and word not in sandwich["meat"]:
                sandwich["meat"].append(word)
            if sandwich["veggies"] and word in menu.VEGGIES and word not in sandwich["veggies"]:
                sandwich["veggies"].append(word)
            if sandwich["cheese"] and word in menu.CHEESE and word not in sandwich["cheese"]:
                sandwich["cheese"].append(word)
            if sandwich["sauce"] and word in menu.SAUCE and word not in sandwich["sauce"]:
                sandwich["sauce"].append(word)
            if word is "toasted":
                sandwich["toasted"] = word
                
    if not sandwich["name"]:
        print("\nI'm sorry I did not get that. Please choose from the menu. \n")
        return order()
    return sandwich

def check_bread(sandwich):
    response = (input("\nDo you still want that on " + sandwich["bread"] + " bread? We have other options.   ")).lower()
    keywords = process_response(response)
    bread = None
    if "yes" in keywords:
        return sandwich["bread"]
    for word in keywords:
        if word in menu.BREAD:
            bread = word
    if bread is not None:
        return bread
    elif "no" in keywords or "substitute" in keywords:
        bread = different_bread(sandwich)
        return bread
    return bread

def different_bread(sandwich):
    print("\nWhich bread would you like instead?   ")
    print("We have " + ", ".join(menu.BREAD))
    response = (input("   ")).lower()
    keywords = process_response(response)
    for word in keywords:
        if word in menu.BREAD:
            return word
    print("\nWe do not have that. Please choose from the breads we have.   ")
    return different_bread(sandwich)


def check_meat(sandwich):
    print("\nDo you still want the " + ", ".join(sandwich["meat"]) + "?   ")
    print("We have " + ", ".join(menu.MEAT))
    response = (input("   ")).lower()
    keywords = process_response(response)
    meats = []
    meats.append(sandwich["meat"])
    for word in keywords:
        if word in menu.MEAT and word is not sandwich["meat"]:
            meats.append(word)
    if "add" in keywords:
        return meats
    elif "yes" in keywords:
        return sandwich["meat"]
    else:
        meats = different_meat(sandwich)
        return meats
    return sandwich["meat"]

def different_meat(sandwich):
    print("\nWhich meat would you like instead?   ")
    print("We have " + ", ".join(menu.MEAT))
    response = (input("   ")).lower()
    keywords = process_response(response)
    meats = []
    for word in keywords:
        if word in menu.MEAT:
            meats.append(word) 
    if meats:
        return meats
    print("\nWe do not have that. Please choose from the meats we have.   ")
    return different_meat(sandwich)

def check_veggies(sandwich):
    print("\nDo you still want the " + ", ".join(sandwich["veggies"]) + "?")
    print("We have " + ", ".join(menu.VEGGIES))
    response = (input("   ")).lower()
    keywords = process_response(response)
    veggies = []
    veggies.append(sandwich["veggies"])
    for word in keywords:
        if word in menu.VEGGIES  and word is not sandwich["veggies"]:
            veggies.append(word)
    if "add" in keywords:
        return veggies
    elif "yes" in keywords:
        return sandwich["veggies"]
    else:
        veggies = different_veggies(sandwich)
        return veggies
    return sandwich["veggies"]

def different_veggies(sandwich):
    print("\n\nWhich veggies would you like instead?   ")
    print("We have " + ", ".join(menu.VEGGIES))
    response = (input("   ")).lower()
    keywords = process_response(response)
    veggies = []
    for word in keywords:
        if word in menu.VEGGIES:
            veggies.append(word) 
    if veggies:
        return veggies
    print("\n\nWe do not have that. Please choose from the veggies we have.   ")
    return different_veggies(sandwich)

def check_cheese(sandwich):
    print("Do you still want the " + ", ".join(sandwich["cheese"]))
    print("We have " + ", ".join(menu.CHEESE))
    response = (input("   ")).lower()
    keywords = process_response(response)
    cheeses = []
    cheeses.append(sandwich["cheese"])
    for word in keywords:
        if word in menu.CHEESE and word is not sandwich["cheese"]:
            cheeses.append(word)
    if "add" in keywords:
        return cheeses
    elif "yes" in keywords:
        return sandwich["cheese"]
    else:
        cheeses = different_cheese(sandwich)
        return cheeses
    return sandwich["cheese"]

def different_cheese(sandwich):
    print("\nWhich cheese would you like instead?   ")
    print("We have " + ", ".join(menu.CHEESE))
    response = (input("   ")).lower()
    keywords = process_response(response)
    cheeses = []
    for word in keywords:
        if word in menu.CHEESE:
            cheeses.append(word) 
    if cheeses: 
        return cheeses
    print("\nWe do not have that. Please choose from the cheeses we have.   ")
    return different_cheese(sandwich)

def check_spread(sandwich):
    print("Do you still want the " + ", ".join(sandwich["sauce"]) + " spread?")
    print("We have " + ", ".join(menu.SAUCE))
    response = (input("   ")).lower()
    keywords = process_response(response)
    spreads = []
    spreads.append(sandwich["sauce"])
    for word in keywords:
        if word in menu.SAUCE and word is not sandwich["sauce"]:
            spreads.append(word)
    if "add" in keywords:
        return spreads
    elif "yes" in keywords:
        return sandwich["sauce"]
    else:
        spreads = different_spread(sandwich)
        return spreads
    return sandwich["spread"]

def different_spread(sandwich):
    print("\nWhich spread would you like instead?   ")
    print("We have " + ", ".join(menu.SAUCE))
    response = ("   ").lower()
    keywords = process_response(response)
    spreads = []
    for word in keywords:
        if word in menu.SAUCE:
            spreads.append(word) 
    if spreads:
        return spreads
    print("\nWe do not have that. Please choose from the spreads we have.   ")
    #return different_spread(sandwich)

def toast():
    response = (input("Should we toast that sandwich? ")).lower()
    keywords = process_response(response)
    if "yes" in keywords:
        return "toasted"
    else:
        return "not toasted"

def extras():
    response = (input("Any extras? Double meat? Double cheese?   ")).lower()
    keywords = process_response(response)
    extras = []
    if "extra" in keywords and "meat" in keywords:
        extras.append("extra meat")
    if "extra" in keywords and "cheese" in keywords:
        extras.append("extra cheese")
    if "yes" in keywords:
        extras.append("extra meat")
        extras.append("extra cheese")   
    return extras

def display(sandwich):
   
    
    meat = ", ".join([str(item) for item in sandwich["meat"]])
    veggies = ", ".join([str(item) for item in sandwich["veggies"]])
    cheese = ", ".join([str(item) for item in sandwich["cheese"]])
    spread = ", ".join([str(item) for item in sandwich["sauce"]])
    extras = ", ".join([str(item) for item in sandwich["extras"]])
  

    print("\n\nYour current order is: \n")
    print("name: " + sandwich["name"])
    print("bread: " + sandwich["bread"]) 
    print("meat: " + meat)
    print("veggies: " + veggies)
    print("cheese: " + cheese)
    print("spread: " + spread)
    print("toasted: " + sandwich["toasted"])
    print("extras: " + extras)
    print("\n")
    
