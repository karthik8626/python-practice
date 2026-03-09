'''Problem 1 — Print Characters
Input: "python"

Output:
p
y
t
h
o
n
Problem 2 — Count Vowels
Input: "education"

Output:
5
Problem 3 — Reverse String
Input: "hello"

Output:
olleh

(No slicing)

Problem 4 — Count Letters
Input: "banana"

Output:
a = 3
Problem 5 — Check Palindrome

Example:

Input: "madam"

Output:
Palindrome
📈 Why Strings Matter

Later when working with:

NumPy

Pandas

you will process text data, c'''

name=input("enter name")
for i in name:
    print(i)

vowels="a","e","i","o","u"
count=0
name1=name.lower()
for i in name1:
    if i in vowels:
        count+=1
print("vowels count :",count)

n=len(name)
for i in range(n-1,-1,-1):
    print(name)
    break 

count=0
for i in range(len(name)-1):
    if name[i] == 'a':
        count+=1
print(count)


nam=""
for i in range(len(name)-1,-1,-1):
    nam+=name[i]
if nam==name:
    print("pandirome")
else:
    print("not")
print(nam)# the idea is to store the org str to a duplicate str and then compare both like if nam == name : print("panindromea")