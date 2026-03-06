'''Program 1 — Print numbers 1 to 10

Output:

1
2
3
4
5
...
10

Use a for loop.

Program 2 — Sum of numbers 1 to N

Example:

Input:

5

Output:

15

Because:

1+2+3+4+5
Program 3 — Multiplication Table

Example:

Input:

5

Output:

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
Program 4 — Even numbers from 1–50

Output:

2 4 6 8 10 ...

Hint:

Use %.

Program 5 — Count digits in a number

Example:

Input:

12345

Output:

5

Hint:

Use a while loop.

⭐ Bonus Challenge (Optional but Very Good)

Print this pattern:

*
**
***
****
*****

Hint:

Use nested loops.'''

for i in range(1,11):
    print(i)

num=int(input("enter number"))
num2=0
for i in range(0,num+1):
    num2+=i
print(num2)

num3=int(input("eneter number for mulitpication"))
for i in range(1,11):
    print(num3,"X",i,"=",num3*i)

for i in range(1,51):
    if i %2==0:
        print(i)
    
num8=int(input("enter the digit to know the count"))
count=0
while num8>0:
    count+=1
    num8=num8//10
print(count)


num6=int(input("enter the height of pyramid"))
for i in range(1,num6+1):
        for j in range(i):
            print("*",end="")
        print()