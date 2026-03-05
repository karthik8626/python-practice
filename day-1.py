print("hello world")
'''Program 2 — Sum of two numbers
Input 2 numbers and print sum.
Program 3 — Simple calculator
Add
Subtract
Multiply
Divide
Program 4 — Age calculator
Input birth year
Output current age.2
Program 5 — Even or Odd
Input a number
Check if even or odd.'''
num1=int(input("enter number"))
num2=int(input("enter number"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

num=int(input("enter number to know even or odd"))
if num % 2==0:
    print("even")
else:
    print("odd")
    
year=int(input("enter birth year"))
curyear=int(input("enter current year"))
age=curyear-year
print(age)
