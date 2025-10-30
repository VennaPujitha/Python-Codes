# 1) Program to count and display factors of the given number.

# n=int(input("Enter the number:"))
# count=0
# for fact in range(1,n+1):
#     if n%fact==0:
#         print(fact,end=" ")
#         count+=fact
# print("Count is",count)


# 2) Program to check whether the given number is prime  number or not.

# fact=0
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         fact+=1
# if fact==2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")


# 3) Program to reverse the number.

# num=input("enter the number:")
# print(num[::-1])

# OR

# n=int(input("Enter the number:"))
# rev=''
# while n!=0:
#     r=n%10
#     n=n//10
#     rev=rev+str(r)
# print(rev)

# 4) Program to check given number is palindrome or not.

# n=input("Enter the number:")
# if n==n[::-1]:
#     print("Given number is palindrome")
# else:
#     print("Given number is not palindrome")

#OR

n=int(input("Enter the number:"))
n1=n
num=""
while n!=0:
    r=n%10
    n=n//10
    num=num+str(r)
if int(num)==n1:
    print("Palindrome")
else:
    print("not palindrome")

# 5) Program to check given number is Armstrong number or not.

# n=int(input("Enter the number:"))
# n1=n
# num=0

# while n!=0:
#     r=n%10
#     n=n//10
#     num=num+r**3
# print(num)

# if num==n1:
#     print("Armstong")
# else:
#     print("Not Armstorng")

# 6) Program to check given number is Perfect number or not.

#A Perfect number is a number that is equal to the sum of its proper divisors (excluding itself).

# n=int(input("Enter the number:"))

# sum=0

# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("Perfect")
# else:
#     print("Not perfect")

# 7) Program to print prime numbers up to a range.


# factors=0
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         factors+=1

# if factors==2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")


# 8) Program to print Armstrong numbers up to a range.

# num=input("Enter the number:")
# n1=num
# c=0

# for n in num:
#     n=int(n)
#     r=n%10
#     n=n//10
#     c=c+r**3
    
# print(c)

# c=str(c)

# if n1==c:
#     print("Armstong")
# else:
#     print("Not Armstorng")


# 9) Program to find sum of the first N natural numbers. 

# n=int(input("Enter the number:"))
# sum=n*(n+1)/2
# print(f"Sum of the first {n} natural numbers:{sum}")


# 10) Program to print multiplication table of given number.

# n=int(input("Enter the number:"))
# for i in range(1,11):
#     print(f"{n} X {i}={n*i}")




# 11)Program to check given 2 numbers are Twin primes or not.

# Ex: Twin primes: (3,5),(5,7), 7,11 and  2,3 and 2,4 not twins    


# a=int(input("Enter the numbers:"))
# b=int(input("Enter the numbers:"))

# a=a
# b=a+2
# if 
# print(f'({a}","{b})')


# factors=0
# n=int(input("Enter the number:"))
# for i in range(3,n+1):
#     if n%i==0:
#         factors+=1
#     # print(f'')

# if factors==2:
#     print(f"{n} is prime number")
#     print(f'{factors} {factors+2}')
# # else:
# #     print(f"{n} is not prime number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# check if first number is prime
count1 = 0
for i in range(1, a+1):
    if a % i == 0:
        count1 += 1

# check if second number is prime
count2 = 0
for i in range(1, b+1):
    if b % i == 0:
        count2 += 1

# twin prime condition
if count1 == 2 and count2 == 2 :
    print(f"({a}, {b}) are Twin Primes")
else:
    print(f"({a}, {b}) are NOT Twin Primes")
