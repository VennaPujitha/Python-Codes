# TUPLE – INTERVIEW LEVEL CODING QUESTIONS

# Write a program to create a tuple and print all its elements.

tup = (10,20,30)
for i in tup:
    print(i)

# Write a program to find the length of a tuple.

tup = (1,2,3,4,5)
print(len(tup))

# (OR)

tup = (1,2,3,4,5)
count = 0
for i in tup:
    count = count + 1
print(count)

# Write a program to find the maximum and minimum elements in a tuple.

tup = (1,3,5,7,9)
print(max(tup))
print(min(tup))

#(OR)

tup = (1, 3, 5, 7, 9)

maximum = tup[0]
minimum = tup[0]

for i in tup:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Maximum:", maximum)
print("Minimum:", minimum)

# Write a program to count the occurrence of an element in a tuple.

tup = (1,2,3,4,2,2,5,6)
print(tup.count(2))

# (OR)

tup = (1, 2, 3, 4, 2, 4, 2, 5, 4, 6)
x = int(input("Enter the X Value:"))
count = 0

for i in tup:
    if i == x:
        count += 1

print("Count:", count)

# Write a program to find the index of an element in a tuple.

tup = (10, 20, 30, 40, 50)
print(tup.index(20))

# Write a program to check whether an element exists in a tuple.

tup = (2, 4, 6, 8, 10)
x = 2
found = False

for i in tup:
    if i == x:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")

# Write a program to convert a list into a tuple.

lst = [1,3,5,7,9]
print(tuple(lst))

# Write a program to convert a tuple into a list.

tup = (2,4,6,8)
print(list(tup))

# Write a program to unpack a tuple into individual variables.

tup = (10, 20, 30)

a, b, c = tup

print(a)
print(b)
print(c)


# Write a program to swap two values using tuple unpacking.

a = 10
b = 20

a,b =b, a
print(f"a = {a}")
print(f"b = {b}")

# Write a program to find the sum of elements in a tuple.

tup = (1,2,3,4,5)
print(sum(tup))

# (OR)

tup = (10,20,30,40)
total = 0
for i in tup:
    total = total + i
print(total)

# Write a program to find the largest and smallest elements in a tuple without using max() and min().

tup = (10, 20, 30, 40, 50)

largest = tup[0]
smallest = tup[0]

for i in tup:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)

# Write a program to count even and odd numbers in a tuple.

tup = (1,2,3,4,5,6,7)
even = ()
odd = ()
for i in tup:
    if i%2 == 0:
        even = even + (i,)
    else:
        odd = odd + (i,)

print(even)
print(odd)

# Write a program to check whether a tuple is empty.

tup = ()

if not tup:
    print("Tuple is empty")
else:
    print("Tuple is not empty")

# Write a program to reverse a tuple.

tup = (2,4,6,8,10)
print(tup[::-1])

# Write a program to concatenate two tuples.

tup1 = (1,3,5)
tup2 = (2,4,6)
add = tup1 + tup2
print(add)

#(OR)

tup1 = (1,3,5)
tup2 = (2,4,6)

result = tup1
for i in tup2:
    result = result + (i,)

print(result)

# Write a program to find common elements between two tuples.

tup1 = (1,3,5,2,4,6)
tup2 = (2,4,6)

common = ()

for i in tup1:
    if i in tup2:
        common = common + (i,)
print(common)

# Write a program to remove duplicate elements from a tuple.

tup = (1,2,2,4,3,6,1,7)
remove_dup = ()
for i in tup:
    if i not in remove_dup:
        remove_dup = remove_dup + (i,)
print(remove_dup)

# Write a program to find the second largest element in a tuple.

tup = (3, 4, 5, 9, 6, 7, 8)

sorted_tup = sorted(tup)   
second_largest = sorted_tup[-2]

print(f"Second largest element : {second_largest}")

# Write a program to check whether a tuple is a palindrome.

tup = (1,2,3,2,1)

if tup == tup[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Write a program to create a tuple of numbers and find their product.

tup = (1,2,3,4,5)
product = 1
for i in tup:
    product = product * i
print(product)

# (OR)

tup = ()
product = 1
for i in tup:
    product *= i
print(product)

# Write a program to find the frequency of each element in a tuple.

tup = (9, 7, 4, 2, 7)
checked = ()

for i in tup:
    if i not in checked:
        print(i, ":", tup.count(i))
        checked += (i,)

# Write a program to sort a tuple in ascending order.

tup = (40, 20, 30, 10, 50)
sorted_tup = tuple(sorted(tup))
print(sorted_tup)

# Write a program to sort a tuple in descending order.

tup = (40, 20, 30, 10, 50)
sorted_tup = tuple(sorted(tup, reverse=True))
print(sorted_tup)

# Write a program to slice a tuple into two halves.

tup = (1, 2, 3, 4, 5, 6)

mid = len(tup) // 2

first_half = tup[:mid]
second_half = tup[mid:]

print("First half:", first_half)
print("Second half:", second_half)

# Write a program to create a nested tuple and access inner elements.

tup = (1, 2, (3, 4, 5), 6)

print(tup[2])       
print(tup[2][1])     

# Write a program to flatten a nested tuple.

tup = (1, 2, (3, 4), 5)

flat = ()

for i in tup:
    if type(i) == tuple:
        for j in i:
            flat += (j,)
    else:
        flat += (i,)

print(flat)

# Write a program to find the index of an element without using index().

tup = (10, 20, 30, 40, 50)
x = 30

position = -1

for i in range(len(tup)):
    if tup[i] == x:
        position = i
        break

print("Index:", position)

# Write a program to check whether all elements in a tuple are unique.

tup = (1, 2, 3, 4, 5)

unique = True

for i in tup:
    if tup.count(i) > 1:
        unique = False
        break

if unique:
    print("All elements are unique")
else:
    print("Duplicates found")

# Write a program to demonstrate tuple immutability.

tup = (1, 2, 3)

tup[0] = 10   # --> TypeError: 'tuple' object does not support item assignment