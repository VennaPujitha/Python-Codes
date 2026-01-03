# 1) Decision Making Statements / Conditional Statements
# i) if

# Write a program to check whether a number is positive.

number = int(input("Enter the Number:"))
if number>0:
    print(f'{number} is positive')

# Write a program to print “Welcome” if a user enters the correct PIN.

pin = int(input("Set the PIN: "))
entered_pin = int(input("Enter the PIN: "))

if pin == entered_pin:
    print("Welcome")

# Write a program to check whether a number is divisible by 7.

number = int(input("Enter the number: "))

if number % 7 == 0:
    print(f"{number} is divisible by 7")

# ii) if-else

# Write a program to check whether a number is even or odd.

num = int(input("Enter the number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Write a program to check whether a person is eligible to vote.

age = int(input("Enter the Age:"))

if age>=18:
    print('person is eligible to vote')
else:
    print('person is not eligible to vote.')

# Write a program to compare two numbers and print the greater one.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater")
elif num2 > num1:
    print(f"{num2} is greater")
else:
    print("Both numbers are equal")


# iii) Nested if

# Write a program to validate ATM withdrawal using PIN and balance.

pin = 12345
balance = 5000

enter_pin = int(input("Enter the Pin:"))

if pin==enter_pin:
    amount = int(input("Enter the amount:"))

    if amount<=balance:
        print('Withdrwal successful') 
    else:
        print('Insufficient balance') 
else:
    print('Incorrect pin')  


# Write a program to check college admission based on marks and certificates.

required_marks = 500
required_certificate = "AI"

entered_marks = int(input("Enter the marks: "))

if entered_marks >= required_marks:
    entered_certificate = input("Enter the certificate: ")
    if entered_certificate == required_certificate:
        print("Admission successful")
    else:
        print("Certificate not matched")
else:
    print("Insufficient marks")


# Write a program to check login using username and password with role validation.

username = "Pujitha"
password = 12345
role = "admin"

enter_username = input("Enter username: ")

if enter_username == username:
    enter_password = int(input("Enter password: "))
    if enter_password == password:
        enter_role = input("Enter role: ")
        if enter_role == role:
            print("Login successful with role access")
        else:
            print("Role mismatch")
    else:
        print("Wrong password")
else:
    print("Wrong username")


# iv) if-elif-else

# Write a program to print grade based on marks.

marks = int(input("Enter teh Marks:"))

if marks>=90:
    print('Grade: A')
elif marks>=80:
    print('Grade: B')
elif marks>=70:
    print('Grade: C')
elif marks>=50:
    print('Grade: D')
elif marks>=35:
    print('Grade: E')
else:
    print('Grade: F')


# Write a program to display traffic signal actions.

signal = input("Enter the signal: ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")


# Write a program to find the largest of three numbers.

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
num3 = int(input("Enter Number3: "))

if num1 == num2 == num3:
    print("All three numbers are equal")
elif num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest")
elif num2 >= num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")


# 🔹 2) Looping Statements / Iterative Statements
# i) while

# Write a program to print numbers from 1 to 10 using while loop.

n = 1
while n <= 10:
    print(n, end=" ")
    n += 1


# Write a program to reverse a number using while loop.

n = int(input("Enter the Number: "))
rev = 0
while n !=0:
    r=n%10
    rev = rev*10+r
    n=n//10
print(f'Reverse a Number: {rev}')

# Write a program to count digits in a number using while loop.

n = int(input("Enter the Number: "))
count = 0

while n!=0:
    r=n%10
    count = count+1
    n=n//10

print("Number of digits:", count)

# ii) for

# Write a program to print all elements in a list using for loop.

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

# Write a program to calculate the sum of first N natural numbers.

n = int(input("Enter the number: "))

total = 0
for i in range(1, n + 1):
    total = total + i

print("Sum of first", n, "natural numbers is:", total)



# Write a program to print a multiplication table.

n = int(input("Enter the Number:"))

for i in range(1, 11):
    print(n,"X",i,"=",n*i)

# 🔹 3) Jumping Statements / Transfer Statements
# i) break

# Write a program to stop loop execution when a number equals 5.

n = 4  # Start number

while True:
    print(n)
    if n == 5:
        print("Loop stopped as number equals 5")
        break
    n += 1


# Write a program to exit loop when user enters a negative number.

while True:
    n = int(input("Enter a number: "))
    if n < 0:
        print("Negative number entered. Exiting loop.")
        break
    else:
        print("You entered:", n)



# ii) continue

# Write a program to skip even numbers from 1 to 20.

n= 1

while n<=21:
    if n%2==0:
        n=n+1
        continue
    print(n)
    n=n+1



# Write a program to skip a specific username from a list.

usernames = ['puji', 'lavanya', 'kala', 'venky']

for user in usernames:
    if user == "puji":
        continue
    print(user)


# iii) pass

# Write a program with an empty if block using pass.

n = 1

if n < 0:
    pass  

print(n)

# Write a program with a function definition using pass.

def fun():
    pass
fun()


# 🔥 Bonus Interview Question

# Write a program that uses if, loop, break, and continue in a single program.

n = 0

while n < 10:
    n = n + 1
    
    if n % 2 == 0:
        continue  # skip even numbers
    
    print("Odd number:", n)
    
    if n == 7:
        print("Reached 7, stopping loop")
        break
