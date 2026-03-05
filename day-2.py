'''Program 1 — Positive / Negative

Input number
Check whether it is positive or negative

Program 2 — Largest of Two Numbers

Input two numbers
Print which one is larger.

Program 3 — Voting Eligibility

Input age

Rules:

age ≥ 18 → Eligible

else → Not eligible

Program 4 — Grade Calculator

Input marks

90+  → A
75+  → B
50+  → C
<50  → Fail
Program 5 — Simple Login System
username = "admin"
password = "1234"

User inputs username and password.
If correct → Login successful
Else → Invalid credentials'''

num=int(input("enter number to know it is +ve or -ve: "))
if num>0:
    print("positive")
else:
    print("negative")

num1=int(input("enter 1st num: "))
num2=int(input("enter 2nd num: "))
if num1>num2:
    print("larget",num1)
else:
    print("largest",num2)

age=int(input("enter ur age to know eligible to vote or not: "))
if age >= 18:
    print("Eligible")
else:
    print(" not Eligible")

grade=int(input("enter ur marks to know grade: "))
if grade>90:
    print("A")
elif grade > 75 and grade <=90:
    print("B")
elif grade > 50 and grade <= 75:
    print("C")
else:
    print("fail")

username = "admin"
password = "1234"
un=input("enter the username: ")
pas=input("enter password: ")

if username == un and password == pas:
    print("login successfull")
else:
    print("failed login")