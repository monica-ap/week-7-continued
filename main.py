from random import randint
from random import shuffle
from random import choice
  # random
  # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
  #show you two useful functions for now.
print("random")
dice1=randint(1,7)
dice2=randint(1,7)
print(f"dice1: {dice2}")
print(f"dice2: {dice1}")
rolledDoubles= dice1==dice2
if rolledDoubles:
   print("you rolled doubles")
else: print("not doubles")

#create a way to roll snakes
if dice1 and dice2==1:
  print("you rolled snake eyes")
else: print("you did not roll snake eyes")

#practice with shuffle
my_list= range(1,51)
print("my new list")
print(list(my_list))
my_list= list(my_list)
shuffle(my_list)
print(my_list)

new_list=randint(1,201)
print("new list")
print(new_list)
if new_list %2 ==0:
  print("number is even")
else: print("number is odd")

color=["red","blue","pink","purple"]
random_color= choice(color)
print(f"random color is {random_color}")