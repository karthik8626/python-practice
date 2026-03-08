def add(a,b):
    print(a+b)
a=int(input("1st number"))
b=int(input("2nd number"))
c=int(input("3rd number"))
add(a,b)

'''
2️⃣ Function to find largest of three numbers

Example:

largest(4,9,2)

Output:

9
3️⃣ Function to count even numbers in a list

Example list:

[2,5,8,11,14]

Output:

3
4️⃣ Function to sum elements of a list

Example:

[5,10,15]

Output:

30
Goal for Day 5

Understand:

def
return
function parameters

Once you learn functions, your code will start looking like real programs instead of long scripts.

When you finish Day 5, send your code and I’ll review it.'''

def largest(a,b,c):
    if a>b and a>c:
        print("largest",a)
    elif b>a and b>c:
        print("largest",b)
    else:
        print("largest",c)
largest(a,b,c)

ar=[2,5,8,11,14]
def ev (ar):
    count=0
    for i in ar:
        if i%2==0:
            count+=1
    print(count)
ev(ar)

n=int(input("enter the size of list to sum them"))
arr=[]
value=0
for i in range(n):
    value=int(input("enter the vaalue in list"))
    arr.append(value)
print(arr)

def ls(arr):
    sum=0
    for i in arr:
        sum+=i
    print(sum)

ls(arr)