# class Student:
#     name = "Abid"


# s1 = Student.name
# print(f"name of the student is: {s1}")


class Student:

    # University = "UObs"
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        print("from UoBs")
        

s1 = Student("Abid", "100")
print(f" {s1.name} got {s1.mark} % marks")

s2 = Student("Tanveer", "100")
print(f" {s2.name} got {s2.mark} % marks ")



class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


    def Drive(self,):
        print(f"drive the {self.color} {self.brand} car")

c1 = Car("Red", "Toyota")
c2 = Car("Black", "rollryce")
        
c1.Drive()
c2.Drive()