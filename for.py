# FOR LOOP – BASIC CODING QUESTIONS

#  Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i, end=" ")

#  Write a program to print even numbers between 1 and 50.

for i in range(2,51,2):
    print(i, end=" ")

   # (OR)

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

#  Write a program to print odd numbers between 1 and 50.

for i in range(1,50,2):
    print(i, end=" ")

    # (OR)

for i in range(1,50):
    if i%2 !=0:
        print(i, end=" ")

#  Write a program to find the sum of first n natural numbers.

n = int(input("Enter the Number:"))
total = 0

for i in range(1,n+1):
    total = total+i
print(f"sum of first {n} natural numbers is {total}")

#  Write a program to find the factorial of a number using for loop.

number = int(input("Enter the number:"))
fact = 1

for i in range(1,number+1):
    fact = fact*i

print(f"{number} factorial is {fact}")

#  Write a program to reverse a number using for loop.

number = int(input("Enter the number: "))
reverse = 0

for i in range(len(str(number))):
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number is:", reverse)

#  Write a program to count digits in a number.

number = int(input("Enter the number: "))
count = 0

for i in range(len(str(number))):
    digit = number % 10
    number = number // 10
    count = count+1

print("Count digits in a number", count)

#  Write a program to print multiplication table of a given number.

n = int(input("Enter the number: "))

print(f"Multiplication table of {n}:")

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

#  Write a program to check whether a number is prime using for loop.

num = int(input("Enter the Number: "))
fact = 0

for i in range(1, num + 1):
    if num % i == 0:
        fact += 1

if fact == 2:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")

#  Write a program to print Fibonacci series up to n terms.

n = int(input("Enter the Number of terms: "))

a = 0
b = 1

print("Fibonacci Series:", end=" ")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# INTERVIEW LEVEL FOR LOOP QUESTIONS

#  Write a program to print star pattern (pyramid).

n = int(input("Enter the Number: "))

for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()

#  Write a program to print number pattern.

n = int(input("Enter the Number: "))

for row in range(1,n+1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

#  Write a program to check Armstrong number using loop.

num = int(input("Enter a number: "))
temp = num
total  = 0

while temp > 0:
    digit = temp % 10
    total  = total  + digit ** 3
    temp =temp// 10

if total  == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is Not an Armstrong Number")

 #(OR)

num = int(input("Enter a number: "))
temp = num
total = 0

digits = len(str(num))

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is Not an Armstrong Number")

# Write a program to find all prime numbers between 1 and 100.

for num in range(1, 101):
    fact = 0
    for i in range(1, num + 1):
        if num % i == 0:
            fact += 1
    if fact == 2:
        print(num, end=" ")

#  Write a program to find the longest word in a sentence using loop.

sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word is:", longest)