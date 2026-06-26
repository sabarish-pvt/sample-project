# import math
# import random
# import datetime

# # modules

# print("square of 5 is: ",math.sqrt(5))
# print("factorial of 25 is: ",math.factorial(25))
# print("Pi value",math.pi)
# print("Random number:", random.randint(1, 10))
# today = datetime.datetime.now()
# print("Today: ", today)

#Exception handling

# try:
#     x=int(input("Enter a number: "))
#     print("100 divisible by",x,"=",100/x)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please enter a number")
# except Exception as e:
#     print("Error:", e)
# else:
#     print("No error happened")
# finally:
#     print("Finished")

#Class and object

# class Student:
#     def __init__(self,name,age):
#         self.name=name,
#         self.age=age
#     def display(self):
#         print("Student name: ",self.name)
#         print("Student age: ",self.age)
# s1=Student("Sabarish", 21)
# s1.display()
        