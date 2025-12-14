# What is random module?
# A built-in Python module.
# Used to generate random numbers and make random selections.
# Works with integers, floats, and sequences (lists, tuples, strings, etc.).
# Very useful in games, simulations, cryptography, ML (e.g., dataset shuffling, train/test split).
import random
print(random.random()) #used to generate a random float number less the one

print(random.randint(1, 10)) #it generate the any random integer in a given range

print(random.randrange(0, 20, 2)) # it will retrun any random number with spacific gap in a give range 
# Random even number between 0 and 18

print(random.uniform(0, 5)) # return a random float in range

itmes = ["Apple", "Orange", "Banana", ]
print(random.choice(itmes)) # use to select random item from the sequnce

itmes = ["Apple", "Orange", "Banana", "Watermelon", "pomegurnate"]
print(f"choices = {random.choices(itmes, k=2)}") #Picks multiple items (with replacement).
print(f"sample = {random.sample(itmes, 2)}") #Selects unique random items (no repetition).

# random.shuffle()
# Randomly shuffles a list in place.
# Useful for dataset shuffling before train/test split.
data = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(data)# mixing things up
print(data)

