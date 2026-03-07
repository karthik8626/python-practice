'''Program 1 — Create and Print List

Create a list of 5 numbers and print all elements using a loop.

Example:

Input list: [5,10,15,20,25]

Output:
5
10
15
20
25
Program 2 — Sum of List

Example:

numbers = [5,10,15,20]

Output:
50

Use a loop.

Program 3 — Largest Number in List

Example:

numbers = [8,3,15,2,10]

Output:
15

Do not use built-in max().
Use logic with loops.

Program 4 — Count Even Numbers

Example:

numbers = [2,5,8,11,14]

Output:
3

Because 2, 8, 14 are even.

Program 5 — Reverse a List

Example:

numbers = [1,2,3,4]

Output:
4 3 2 1

Use a loop.

⭐ Bonus (Very Useful)

Take 5 numbers from user input and store them in a list.

Example:

Enter number: 5
Enter number: 8
Enter number: 3
Enter number: 10
Enter number: 7

Then print the list.'''



ar=[5,10,15,20,25]
n=len(ar)
for i in range(n):
    print(ar[i])

j=0
numbers = [5,10,15,20]
for i in numbers:
    j+=i
print("the sum of numbers[5,10,15,20]is :" ,j)

number1 = [8,3,15,2,10]
for i in number1:
    if number1[0]<i:
        number1[0]=i
print(number1[0])

count=0
number2 = [2,5,8,11,14]
for i in number2:
    if i %2==0:
        count+=1
print(count)



arr=[]
value=0
n=int(input("enter the length of list"))
for i in range(n):
    value=int(input("enter the values"))
    arr.append(value)
print(arr)


'''Problem 1

Take 5 numbers from user input and store them in a list.

Print the list.

Problem 2

Find the second largest number in a list.

Example:

[10,4,8,20,15]

Output:

15
Problem 3

Remove all even numbers from a list.

Example:

[1,2,3,4,5,6]


Output:

[1,3,5]
One Important Thing

You are doing so'''

arr=[]
n=int(input("enter the size of list"))
for i in range(n):
    value=int(input("enter the value: "))
    arr.append(value)
print(arr)


a=[1,2,3,4,5,6]
n=len(a)
for i in a:
    if i %2==0:
        continue
    else:
        print(i)


