'''Problem 1 — Student Dictionary

Create a dictionary:

name
age
course

Print all values.

Problem 2 — Add New Key

Start with:

{"name":"Rahul","age":20}

Add:

"city": "Hyderabad"

Print dictionary.

Problem 3 — Print Keys and Values

Given:

{"a":10,"b":20,"c":30}

Print:

a 10
b 20
c 30
Problem 4 — Sum Dictionary Values

Given:

{"a":5,"b":10,"c":15}

Output:

30
Problem 5 — Count Characters in String

Example:

Input: "banana"

Output:

b:1
a:3
n:2

Hint: use dictionary to store counts.'''

dic={
}
dic["name"]=input("enter ur name")
dic["age"]=int(input("enter ur age"))
dic["course"]=input("enter the course name")
print("name of student is: ",dic["name"],"age of student is: ",dic["age"],"course of student is: ",dic["course"])

dic["year"]=int(input("enter the year "))
print(dic)

for key in dic:
    print(key,":",dic[key])
'''
ad={
}
ad["nu"]=int(input("enter num1"))
ad["nu1"]=int(input("enter num2"))
ad["nu2"]=int(input("enter num3"))
count=0
print(nu+nu1+nu2)'''
count=0
ad={"a":5,"b":10,"c":15}
for kei in ad:
    count+=ad[kei]
print(count)

count = {}

name = input("enter word: ")

for ch in name:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)