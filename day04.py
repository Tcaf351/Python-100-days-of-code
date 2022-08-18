# Randomisation and Python Lists
import random

random_integer = random.randint(1, 10) # range from 1-10
# print(random_integer)


# Lists 
#They are like arrays in JavaScript
fruits = ["Cherry", "Apple", "Pear"]

fruits[1] = "Mango"

fruits.append("Olive")

print(fruits)

fruits.extend(["Orange", "Blueberry", "Raspberry"]) #extends takes 1 argument, multiple items will need to be in a list (array)

print(fruits)

