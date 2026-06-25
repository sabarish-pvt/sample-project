# 1 Greeting program (while + function)

#def greet(name):
#    print("Hello, Welcome",name)
#while True:
#    name = input("Enter your name or enter exit to terminate: ")
#    if name.lower() == "exit":
#     print("ok.....")
#    break
#    greet(name)

# 2 Calculator using functions

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multi(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# a=int(input("Enter your first number: "))
# b=int(input("Enter your second number:"))
# op=input("Enter ur operation(+,-,*,/):")
# if op == "+":
#     print(add(a,b))
# elif op == "-":
#     print(sub(a,b))
# elif op == "*":
#     print(multi(a,b))
# elif op == "/":
#     print(div(a,b))
# else:
#     print("Invalid Operation")

# 3 Square and cube

# def square(n):
#     return n*n
# def cube(n):
#     return n*n*n
# num = int(input("Enter Number: "))
# print("Square = ",square(num))
# print("Cube = ",cube(num))

# 4 odd or even

# def check_number(n):
#     if n%2==0:
#         print(n,"is even!!")
#     else:
#         print(n,"is odd!!")
# num = int(input("Enter your Number:"))
# check_number(num)

# 5 Maximum of three numbers

# def maximum(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# print(maximum(10,50,20))

# 6 Grade Calculator

# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 50:
#         return "C"
#     else:
#         return "Fail"
# marks = int(input("Enter marks: "))
# print("Grade =", grade(marks))

# 7 args* shopping bill

# def bill(*items):
#     total = 0
#     for i in items:
#         total = total+i
#         print("Total bill: ",total)
# bill(20,100,500,399)

# 8 Average using *args

# def average(*numbers):
#     total = sum(numbers)
#     avg = total/len(numbers)
#     print("Average :",avg)
# average(10,20,30)

# 9 **kwargs student details

# def student(**details):
#     for key,value in details.items():
#         print(key,":",value)
# student(
#     name="Sabarish",
#     age=21,
#     course="Ai-Engineer"
# )

# 10 Lambda calc

# add = lambda a,b : a+b
# multi = lambda a,b : a*b
# print(add(2,5))
# print(multi(10,5))

# 11 Recursion print 1 to n

# def count(n):
#     if n==0:
#         return
#     count(n-1)
#     print (n)
# count(5)

# 12 Factorial using recursion

# def factorial(n):
#     if n==1:
#         return 1
#     return n* factorial(n-1)
# print(factorial(5))

