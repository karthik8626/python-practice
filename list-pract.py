'''1️⃣ Find Largest Number in a List

Example:

numbers = [4, 7, 2, 10, 5]

Output:

10
2️⃣ Count Even Numbers in a List

Example:

[2,5,8,11,14]

Output:

3
3️⃣ Reverse a List

Example:

[1,2,3,4]

Output:

[4,3,2,1]
'''
li=[]
n=int(input("enter the list size"))
value=0
for i in range(1,n+1):
    value=int(input('enter the value'))
    li.append(value)

print(li)
m=li[0]
for i in li:
    if  m < i:
        m=i
print("largest", m)

count=0
for i in li:
    if i%2==0:
        count+=1
print("even count",count)

l=[]
for i in range(n-1,-1,-1):
    l.append(li[i])

print(l)