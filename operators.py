# 1)Arithmetic Operators

# Write a program to add two numbers without using the + operator.

a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
sum = a-(-b)
print(sum)


# Write a program to find the remainder of two numbers.

num1 = int(input("Enter a number:"))
num2 = int(input("Enter b number:"))

rem = num1%num2
print(rem)

# Write a program to calculate the square and cube of a number using operators.

num = int(input("Enter the number:"))

print(f"Square of {num} is {num**2}")
print(f"Cube of {num} is {num**3}")


# Write a program to swap two numbers using arithmetic operators only.

num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
print("----Before Swap----")
print(f'num1 : {num1}')
print(f'num2 : {num2}')

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("----After Swap----")
print(f'num1 : {num1}')
print(f'num2 : {num2}')


# Write a program to check whether a number is divisible by both 3 and 5.

num = int(input("Enter the number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by both 3 and 5")

# #2) Assignment Operators

# Write a program to update a variable using +=, -=, *=, and /= operators.

a = int(input("Enter the number: "))
print("Initial value:", a)
a += 1
print("After += 1:", a)
a -= 1
print("After -= 1:", a)
a *= 2
print("After *= 2:", a)
a /= 2
print("After /= 2:", a)

# Write a program to calculate the total bill amount using assignment operators.

idly = int(input("Enter the Idly cost:"))
vada = int(input("Enter the Vada cost:"))
dosa = int(input("Enter the Dosa cost:"))
total_bill = 0
total_bill += idly
total_bill += vada
total_bill += dosa
print(f'Total bill {total_bill}')

# Write a program to increase a salary by 10% using assignment operators.

salary = int(input("Enter the salary: "))
salary += salary * 10 / 100
print(f"Salary after 10% increase: {salary}")

# 3) Comparison Operators

# Write a program to compare two numbers and print the greater number.

num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))

if num1>num2:
    print(f'{num1} is greater number')
elif num2 > num1:
    print(f"{num2} is the greater number")
else:
    print("Both numbers are equal")

# Write a program to check whether two numbers are equal or not.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print(f"{num1} and {num2} are equal")
else:
    print(f"{num1} and {num2} are not equal")

# Write a program to check whether a person is eligible to vote.

age = int(input("Enter the Age:"))
if age>=18:
    print("Person is eligible to vote.")
else:
    print("Person is not eligible to vote.")


# Write a program to find the maximum of three numbers using comparison operators.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the maximum")
elif num2 >= num3:
    print(f"{num2} is the maximum")
else:
    print(f"{num3} is the maximum")


# # 4) Logical Operators

# Write a program to check whether a number lies between 10 and 50.

num = int(input("Enter the number:"))

if num >=10 and num <= 50:
    print(f'{num} lies between 10 and 50')
else:
    print(f'{num} not lies between 10 and 50')


# Write a program to check whether a year is a leap year using logical operators.

year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# Write a program to validate login using username and password.

username = input("Set username: ")
password = input("Set password: ")

in_username = input("Enter username: ")
in_password = input("Enter password: ")

if username == in_username and password == in_password:
    print("Login successful")
else:
    print("Login failed")



# Write a program to check whether a student passed all subjects.

sub1 = int(input("Enter Subject 1 marks: "))
sub2 = int(input("Enter Subject 2 marks: "))
sub3 = int(input("Enter Subject 3 marks: "))

if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    print("Student passed all subjects")
else:
    print("Student failed")


# 5) Conditional (Ternary) Operator

# Write a program to find the largest of two numbers using the conditional operator.

num1 = int(input("Enter the Number1:"))
num2 = int(input("Enter the Number2:"))
if num1>num2:
    print(f'{num1} is largest')
else:
    print(f'{num2} is largest')


# Write a program to check whether a number is even or odd using the conditional operator.

num = int(input("Enter the number: "))

result = "Even" if num % 2 == 0 else "Odd"
print(result)

# Write a program to assign grade based on marks using the conditional operator.

marks = int(input("Enter the marks: "))

grade = "Pass" if marks >= 35 else "Fail"
print(grade)


# 6) Membership Operators

# Write a program to check whether an element exists in a list.

list = ['a','b','c','d','e']
element = input("Enter the element:")
if element in list:
    print(f'{element} exists in a list')
else:
    print(f'{element} exists not in a list')


# Write a program to check whether a character is present in a string.

text = input("Enter the string: ")
char = input("Enter the character to check: ")

if char in text:
    print(f"{char} is present in the string.")
else:
    print(f"{char} is not present in the string.")


# 7) Identity Operators

# Write a program to check whether two variables refer to the same object.

str1 = input("Enter the String:")
str2 = input("Enter the String:")

if str1 is str2:
    print("two variables refer to the same object")
else:
    print("two variables do not refer to the same object")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = 0

for i in range(num2):
    result = result + num1

print("Multiplication result:", result)