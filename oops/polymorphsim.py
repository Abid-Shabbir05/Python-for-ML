
# Polymorphism allows one method name to be used for different types of objects, and each object responds in its own way.
# Types of Polymorphism in Python
# Method Overriding (with inheritance) → Child class gives new meaning to the parent’s method.
# Method Overloading (not directly supported in Python, but can be simulated with default/variable arguments).
# Operator Overloading (e.g. + works for numbers, strings, lists).
class Animal_sound:
    def sound(self):
        return "Some Animal Sounds. "
    
class Dog_sound(Animal_sound):
    def sound(self):
        return "Bark Bark...."
    
class Cat_sound(Animal_sound):
    def sound(self):
        return "Meow Meow..."
    
animals = [Animal_sound(), Dog_sound(), Cat_sound()]

for s in animals:
    print(s.sound())



class Person:
    def info(self, name=None, age=None):
        return f"Person Info → Name: {name}, Age: {age}"

class Doctor(Person):   # Inheritance
    def info(self, name=None, age=None):   # Override with parameters
        return f"Doctor → Name: {name}, Age: {age}"

class Student(Person):  # Inheritance
    def info(self, name=None, age=None):   # Override with parameters
        return f"Student → Name: {name}, Age: {age}"


# Polymorphism in action
persons = [Person(), Doctor(), Student()]

for p in persons:
    print(p.info("Abid", 25))
    print(p.info("Ali", 20))



# You are asked to design a program for a transport system using polymorphism + inheritance + parameterized methods.

# Create a base class Vehicle with a method move(distance).

# Create three child classes:

# Car → overrides move(distance) (prints "Car moved {distance} km on road").

# Bike → overrides move(distance) (prints "Bike moved {distance} km on road").

# Airplane → overrides move(distance) (prints "Airplane flew {distance} km in air").

# Put objects of these classes in a list.

# Use a loop to call move() on each object with different distances.


       

# class Vehicle:
#     def move(self, distance):
#         return "Vehicle moving with the specific distance"

# class Car(Vehicle):
#     def move(self, distance):
#         return f"Car moved {distance} km on the road"

# class Bike(Vehicle):
#     def move(self, distance):
#         return f"Bike moved {distance} km on the road"

# class Bus(Vehicle):
#     def move(self, distance):
#         return f"Bus moved {distance} km on the road"

# # Empty list
# Vehicles = []

# # Add one Vehicle
# for d in range(1):
#     Vehicles.append(Vehicle())

# # Add 3 Cars
# for d in range(3):
#     Vehicles.append(Car())

# # Add 5 Bikes
# for d in range(5):
#     Vehicles.append(Bike())

# # Add 1 Bus
# for d in range(1):
#     Vehicles.append(Bus())

# # Now loop through all objects
# for v in Vehicles:
#     print(v.move(50))

# or=====

class Vehicle:
    def move(self, distance):
        return f"Vehicle moved {distance} km"

class Car(Vehicle):
    def move(self, distance):
        return f"Car moved {distance} km on the road"

class Bike(Vehicle):
    def move(self, distance):
        return f"Bike moved {distance} km on the road"

class Bus(Vehicle):
    def move(self, distance):
        return f"Bus moved {distance} km on the road"

# Create a list of different vehicles
vehicles = [
    Car(),
    Bike(),
    Bus(),
    Vehicle()
]

# Call move() on each vehicle
distances = [50, 150, 100, 200]

for v, d in zip(vehicles, distances):
    print(v.move(d))
