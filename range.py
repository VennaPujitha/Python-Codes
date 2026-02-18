# Range & Loop Questions

# Write a program to print numbers from 1 to 20 using range.

for i in range(1,21):
    print(i,end=' ')

# Write a program to print all even numbers between 1 and 50 using range.

for i in range(2,51,2):
    print(i,end=' ')

# Write a program to print all odd numbers between 1 and 50 using range.

for i in range(1,50,2):
    print(i,end=' ')

# Write a program to print numbers from 10 down to 1 using range.

for i in range(10,0,-1):
    print(i,end=' ')

# Write a program to print the first 10 multiples of 3 using range.

for i in range(1,11):
    print(3*i,end=' ')

# Write a program to sum all numbers from 1 to N using range.

N = int(input("Enter N: "))
total = 0

for i in range(1, N + 1):
    total += i  # shorthand for total = total + i

print("Sum of first", N, "natural numbers is:", total)

# Write a program to print a multiplication table of a given number using range.

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


# Write a program to print numbers divisible by 5 between 1 and 100 using range.

for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=' ')


# Write a program to print numbers from 1 to 20 skipping every 3rd number using range.

for i in range(1, 21):
    if i % 3 != 0:
        print(i, end=' ')


# Write a program to reverse a sequence of numbers from 20 to 1 using range.

for i in range(20,0,-1):
    print(i,end=' ')