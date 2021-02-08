README

Step 1:

BLT : 
white bread
bacon
lettuce, tomato
mayo

Anna's Spicy: 
wheat bread
turkey
lettuce
provolone cheese
chipotle

Mom's Healthy Lunch: 
gluten-free bread
chicken
spinach, tomato, cucumber
gouda cheese
vinegarette

Dad's:
wheat bread
ham
lettuce, tomato
cheddar cheese
mustard

Bread options:
white
wheat
gluten-free

Meat options: 
chicken
ham
turkey
bacon

Veggie options:
lettuce
tomato
spinach
cucumbers

Cheese options:
cheddar
provolone
gouda

Sauce options:
mayo
chipotle
vinegarette
mustard

Extras:
toast
extra meat
extra cheese

Exceptions: 
remove any option from the sandwich


Step 2:
MENU : options, choices, menu, what

YES : yes, yeah, yup, sure

NO : no, nope

HOLD : dont, hold, remove, without

ADD : add, and, with

SUBSTITUTE : different, substitute, other

BLT : blt

ANNA'S SPICY TURKEY : anna, annas, spicy

MOM'S HEALTHY LUNCH : mom, moms, healthy, lunch

DAD'S : dad, dads

VEGGIES : veggies, vegetables

SPREAD : spread, sauce

MAYO : mayo, mayonnaise

GLUTEN-FREE : gluten, glutenfree

EXTRA : double, extra

TOASTED : toast, toasted

Everything but keywords are ignored.

Hold the mayo is just looking for a hold equivalent one or two words ahead of whatever you want to exclude.


Step 3:
I used python3. It can be run from main in the sandwich.py file. All input is following prompts.

sandwich.py is the main file where you can chat with the program.

functions.py are just a list of functions to check if the order is correct, display the order, display the menu, etc.

menu.py holds all the infomation about the menu as constants called in the functions file.

constants.py contains all the dictionary to fetch keywords.


Step 4:
Example 1:
 
Welcome! You look hungry. 
Well I can't see you, but you are here so I am going to assume you are hungry. Or maybe someone asked you to order 
them a sandwich becuase they are hungry. Anyway. . .


Would you like to see a menu?   yeah sure

Menu:

We have our BLT, which is of course bacon, lettuce and tomato 
        on white bread with a touch of mayo.

Anna's Spicy comes with thin sliced turkey, provolone cheese, 
        lettuce and some of our signature chipotle sauce all on our very popular wheat bread.

Mom's Healthy Lunch sandwich is gluten-free bread, chicken, spinach, tomato, 
        cucumber, smoked gouda cheese and a splash of vinegarette.

Dad's sandwich is ham and cheddar with lettuce, tomato and mustard on wheat bread.




Which sandwich would you like? (You can modify any sandwich element later.)   anna's spicy on gluten free bread


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: turkey
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: 
extras: no extras



Do you still want that on gluten-free bread? We have other options.   yes


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: turkey
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: 
extras: no extras



Do you still want the turkey?   
We have bacon, turkey, chicken, ham
   add bacon


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: 
extras: no extras



Do you still want the lettuce?
We have lettuce, tomato, spinach, cucumber
   yes


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: 
extras: no extras


Do you still want the provolone
We have provolone, gouda, cheddar
   yes


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: 
extras: no extras


Do you still want the chipotle spread?
We have mayo, chipotle, vinegarette, mustard
   yes


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: 
extras: no extras


Any extras? Double meat? Double cheese?   extra cheese


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: 
extras: extra cheese


Should we toast that sandwich? yes please


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: toasted
extras: extra cheese


Is that all?  yes


Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: toasted
extras: extra cheese




Your current order is: 

name: Anna's Spicy
bread: gluten-free
meat: ['turkey'], bacon
veggies: lettuce
cheese: provolone
spread: chipotle
toasted: toasted
extras: extra cheese


Example 2:
 
Welcome! You look hungry. 
Well I can't see you, but you are here so I am going to assume you are hungry. Or maybe someone asked you to order 
them a sandwich becuase they are hungry. Anyway. . .


Would you like to see a menu?   no


Which sandwich would you like? (You can modify any sandwich element later.)   blt


Your current order is: 

name: BLT
bread: white
meat: bacon
veggies: lettuce, tomato
cheese: 
spread: mayo
toasted: not toasted
extras: no extras



Do you still want that on white bread? We have other options.   no

Which bread would you like instead?   
We have white, wheat, gluten-free
   wheat


Your current order is: 

name: BLT
bread: wheat
meat: bacon
veggies: lettuce, tomato
cheese: 
spread: mayo
toasted: not toasted
extras: no extras



Do you still want the bacon?   
We have bacon, turkey, chicken, ham
   no

Which meat would you like instead?   
We have bacon, turkey, chicken, ham
   chicken and turkey


Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: 
spread: mayo
toasted: not toasted
extras: no extras



Do you still want the lettuce, tomato?
We have lettuce, tomato, spinach, cucumber
   yes


Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: 
spread: mayo
toasted: not toasted
extras: no extras


Do you still want the 
We have provolone, gouda, cheddar
   add provolone


Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: [], provolone
spread: mayo
toasted: not toasted
extras: no extras


Do you still want the mayo spread?
We have mayo, chipotle, vinegarette, mustard
   yes


Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: [], provolone
spread: mayo
toasted: not toasted
extras: no extras


Any extras? Double meat? Double cheese?   no


Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: [], provolone
spread: mayo
toasted: not toasted
extras: 


Should we toast that sandwich? yes


Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: [], provolone
spread: mayo
toasted: toasted
extras: 


Is that all?  yes


Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: [], provolone
spread: mayo
toasted: toasted
extras: 




Your current order is: 

name: BLT
bread: wheat
meat: chicken, turkey
veggies: lettuce, tomato
cheese: [], provolone
spread: mayo
toasted: toasted
extras: 


Example 3:
Welcome! You look hungry. 
Well I can't see you, but you are here so I am going to assume you are hungry. Or maybe someone asked you to order them a sandwich becuase they are hungry. Anyway. . .


Would you like to see a menu?   nope


Which sandwich would you like? (You can modify any sandwich element later.)   dad's


Your current order is: 

name: Dad's
bread: wheat
meat: ham
veggies: lettuce, tomato
cheese: cheddar
spread: mustard
toasted: 
extras: no extras



Do you still want that on wheat bread? We have other options.   I want white bread


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: lettuce, tomato
cheese: cheddar
spread: mustard
toasted: 
extras: no extras



Do you still want the ham?   
We have bacon, turkey, chicken, ham
   yes


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: lettuce, tomato
cheese: cheddar
spread: mustard
toasted: 
extras: no extras



Do you still want the lettuce, tomato?
We have lettuce, tomato, spinach, cucumber
   add spinach


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: ['lettuce', 'tomato'], spinach
cheese: cheddar
spread: mustard
toasted: 
extras: no extras


Do you still want the cheddar
We have provolone, gouda, cheddar
   no   

Which cheese would you like instead?   
We have provolone, gouda, cheddar
   cheddar


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: ['lettuce', 'tomato'], spinach
cheese: cheddar
spread: mustard
toasted: 
extras: no extras


Do you still want the mustard spread?
We have mayo, chipotle, vinegarette, mustard
   yes


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: ['lettuce', 'tomato'], spinach
cheese: cheddar
spread: mustard
toasted: 
extras: no extras


Any extras? Double meat? Double cheese?   double meat


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: ['lettuce', 'tomato'], spinach
cheese: cheddar
spread: mustard
toasted: 
extras: extra meat


Should we toast that sandwich? nope


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: ['lettuce', 'tomato'], spinach
cheese: cheddar
spread: mustard
toasted: not toasted
extras: extra meat


Is that all?  yes


Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: ['lettuce', 'tomato'], spinach
cheese: cheddar
spread: mustard
toasted: not toasted
extras: extra meat




Your current order is: 

name: Dad's
bread: white
meat: ham
veggies: ['lettuce', 'tomato'], spinach
cheese: cheddar
spread: mustard
toasted: not toasted
extras: extra meat

Example 4:
Welcome! You look hungry. 
Well I can't see you, but you are here so I am going to assume you are hungry. Or maybe someone asked you to order 
them a sandwich becuase they are hungry. Anyway. . .


Would you like to see a menu?   yes

Menu:

We have our BLT, which is of course bacon, lettuce and tomato 
        on white bread with a touch of mayo.

Anna's Spicy comes with thin sliced turkey, provolone cheese, 
        lettuce and some of our signature chipotle sauce all on our very popular wheat bread.

Mom's Healthy Lunch sandwich is gluten-free bread, chicken, spinach, tomato, 
        cucumber, smoked gouda cheese and a splash of vinegarette.

Dad's sandwich is ham and cheddar with lettuce, tomato and mustard on wheat bread.




Which sandwich would you like? (You can modify any sandwich element later.)   mom's


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: chicken
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: 
extras: no extras



Do you still want that on gluten-free bread? We have other options.   yes


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: chicken
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: 
extras: no extras



Do you still want the chicken?   
We have bacon, turkey, chicken, ham
   I want bacon


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: 
extras: no extras



Do you still want the spinach, tomato, cucumber?
We have lettuce, tomato, spinach, cucumber
   yes


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: 
extras: no extras


Do you still want the gouda
We have provolone, gouda, cheddar
   yes


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: 
extras: no extras


Do you still want the vinegarette spread?
We have mayo, chipotle, vinegarette, mustard
   yes


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: 
extras: no extras


Any extras? Double meat? Double cheese?   no


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: 
extras: 


Should we toast that sandwich? no


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: not toasted
extras: 


Is that all?  yes


Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: not toasted
extras: 




Your current order is: 

name: Mom's Healthy Lunch
bread: gluten-free
meat: ['chicken'], bacon
veggies: spinach, tomato, cucumber
cheese: gouda
spread: vinegarette
toasted: not toasted
extras: 



Example 4 added bacon instead of replacing it. The check meat function never removes anything unless the user says they don't want the meat they already have.











