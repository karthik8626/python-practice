'''1️⃣ Dictionary Practice — Store Student Data

Write a program that stores one student using a dictionary.

Example structure:

student = {
    "name": "Rahul",
    "age": 20,
    "course": "AIML"
}

Print output like:

Name: Rahul
Age: 20
Course: AIML

Goal: get comfortable with key → value access.

2️⃣ Function + Dictionary

Write a function:

def print_student(student):

The function should print all the values from the dictionary.

Example call:

print_student(student)

Goal: combine functions + dictionaries.

3️⃣ List of Dictionaries

Create a list that stores multiple students.

Example:

students = [
 {"name":"Rahul","age":20},
 {"name":"Ankit","age":21}
]

Loop through the list and print each student.

Goal: understand data structures inside each other.

4️⃣ Small Logic Problem

Given:

marks = {
 "math": 90,
 "physics": 85,
 "cs": 95
}

Find the average marks.

Output:

Average: 90

Goal: iterate dictionary values.

📌 After Completing

Push to GitHub as:

day10_dictionary_practice.
'''


student={}
student["name"]=input("enter student name")
student["age"]=int(input("enter ur age"))
student["course"]=input("enter the course")

for i in student:
    print(i,":",student[i])


def stu(student):
    for i in student:
        print(i,":",student[i])


stu(student)



students = [
    {"name": "Rahul", "age": 20},
    {"name": "Ankit", "age": 21}
]

for student in students:
    for key in student:
        print(key, ":", student[key])
    print()




avg=0
total=0
marks={}
marks["math"]=int(input("enter marks in math"))
marks["ns"]=int(input("enter marks in ns"))
marks["ps"]=int(input("enter marks in ps"))
for i in marks:
    total+=marks[i]
   
avg=total/len(marks)

print(avg)


