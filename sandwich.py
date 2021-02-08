import menu
import constants
import re
import string
import functions

#class Chat:
def main():
    

    print("\nWelcome! You look hungry. \n"
        + "Well I can't see you, but you are here so I am going to assume you are hungry. "
        + "Or maybe someone asked you to order them a sandwich becuase they are hungry. "
        + "Anyway. . .")
    
    functions.see_menu()
    sandwich = functions.order()

    functions.display(sandwich)
    sandwich["bread"] = functions.check_bread(sandwich)
    functions.display(sandwich)
    sandwich["meat"] = functions.check_meat(sandwich)
    functions.display(sandwich)
    sandwich["veggies"] = functions.check_veggies(sandwich)
    functions.display(sandwich)
    sandwich["cheese"] = functions.check_cheese(sandwich)
    functions.display(sandwich)
    sandwich["sauce"] = functions.check_spread(sandwich)
    functions.display(sandwich)
    sandwich["extras"] = functions.extras()
    functions.display(sandwich)
    sandwich["toasted"] = functions.toast()
    functions.display(sandwich)

    response = (input("Is that all?  ")).lower()
    keywords = functions.process_response(response)
    if "yes" in keywords:
        functions.display(sandwich)
    elif "no" in keywords:
        response = input("What else do you need?   ")
        not_done = functions.process_response(response) 
        for word in not_done:
            if word in menu.BREAD or word is "bread":
                sandwich["bread"] = functions.check_bread(sandwich)
            if word in menu.MEAT or word is "meat":
                sandwich["meat"] = functions.check_meat(sandwich)
            if word in menu.VEGGIES or word is "veggies":
                sandwich["veggies"] = functions.check_veggies(sandwich)
            if word in menu.CHEESE or word is "cheese":
                sandwich["cheese"] = functions.check_cheese(sandwich)
            if word in menu.SAUCE or word is "sauce":
                sandwich["sauce"] = functions.check_spread(sandwich)
            if word is "toasted":
                sandwich["toasted"] = functions.toast()
            if word is "extra":
                sandwich["extras"] = functions.extras()
            if word is "menu":
                functions.see_menu()
    functions.display(sandwich)
    
main()








   
