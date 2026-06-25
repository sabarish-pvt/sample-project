students = {}


def add_student():

    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    students[name] = marks

    print("Student added")


def show_students():

    for name,marks in students.items():
        print(name, marks)



def find_grade():

    name = input("Enter student name: ")

    marks = students[name]

    if marks >= 90:
        print("A")

    elif marks >=75:
        print("B")

    elif marks >=50:
        print("C")

    else:
        print("Fail")



while True:

    print("\n1.Add")
    print("2.Show")
    print("3.Grade")
    print("4.Exit")


    choice = input("Choose: ")


    if choice=="1":
        add_student()

    elif choice=="2":
        show_students()

    elif choice=="3":
        find_grade()

    elif choice=="4":
        break

    else:
        print("Wrong choice")