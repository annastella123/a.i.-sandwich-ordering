YES = ["yes", "yeah", "yup", "sure"]

NO = ["no", "nope"]

HOLD = ["hold", "remove", "without", "with out", "dont", "do not"]

ADD = ["add", "with"]

SUBSTITUTE = ["different", "substitute", "other"]

ORDER_BLT = ["blt", "b l t", "bacon lettuce tomato", "bacon lettuce and tomato"]

ORDER_ANNA = ["anna", "annas", "anna spicy turkey", "annas spicy turkey", "spicy turkey"]

ORDER_MOM = ["mom", "moms", "mom healthy lunch", "moms healthy lunch", "healthy lunch"]

ORDER_DAD = ["dad", "dads", "dad ham and cheese", "dads ham and cheese", "ham and cheese"]

MAYO = ["mayo", "mayonnaise"]

GLUTEN_FREE = ["gluten free", "glutenfree"]

EXTRAS = ["double meat", "extra meat", "double cheese", "extra cheese", "toast", "toasted"]

MORE_INFO = ["what is in", "whats in"]

RESPONSES = {
    # order
    "order": "order",
    "know what I want": "order",
    # more info
    "options": "more",
    "what": "more", 
    "choices": "more",
    "menu": "more",
    # answer yes
    "yes": "yes",
    "yeah": "yes",
    "yup": "yes",
    "sure": "yes",
    # answer no
    "no": "no",
    "nope": "no",
    
    "dont": "hold",
    "do not": "hold",
    # hold or remove
    "hold": "hold",
    "remove": "hold",
    "without": "hold",
    # add
    "want": "add",
    "add": "add",
    "and": "add",
    "with": "add",
    # different
    "different": "substitute", 
    "substitute": "substitute", 
    "other": "substitute",
    # blt
    "blt": "blt", 
    # anna's spicy turkey
    "anna": "anna", 
    "annas": "anna", 
    "spicy": "anna", 
    # mom's healthy lunch
    "mom": "mom", 
    "moms": "mom", 
    "healthy": "mom", 
    "lunch": "mom", 
    # dad's ham and cheese
    "dad": "dad", 
    "dads": "dad", 
    # bread
    "bread": "bread",
    "white": "white", 
    "wheat": "wheat", 
    "gluten": "gluten-free",
    # meat
    "meat": "meat",
    "bacon": "bacon", 
    "turkey": "turkey", 
    "chicken": "chicken", 
    "ham": "ham", 
    #veggies
    "veggies": "veggies",
    "vegetables": "veggies",
    "lettuce": "lettuce", 
    "tomato": "tomato", 
    "spinach": "spinach", 
    "cucumber": "cucumber", 
    # cheese
    "cheese": "cheese",
    "provolone": "provolone",
    "gouda": "gouda", 
    "cheddar": "cheddar", 
    # spread
    "spread": "spread",
    "sauce": "spread",
    "chipotle": "chipotle", 
    "vinegarette": "vinegarette", 
    "mustard": "mustard", 
    # mayo
    "mayo": "mayo", 
    "mayonnaise": "mayo",
    # gluten-free
    "gluten":"gluten-free", 
    "gluten free":"gluten-free", 
    "glutenfree": "gluten-free",
    # extra meat
    "double": "extra", 
    "extra": "extra", 
    # toasted
    "toast": "toasted", 
    "toasted": "toasted"
    }