# 🧩 SET – INTERVIEW LEVEL CODING QUESTIONS
# Write a program to create a set and print all its elements.

s = {2,3,4,5}
for i in s:
    print(i, end=" ")

# Write a program to add elements to a set.

s = {2,4,6}
s.add(1)
print(s)

# (OR)

s = {1,3,5}
s.update([2,4,8])
print(s)

# Write a program to remove an element from a set.

s = {10,20,30}
s.remove(20)
print(s)

# (OR)
s = {10,20,30}
s.discard(20)
print(s)

# Write a program to check whether an element exists in a set.

s = {2, 3, 4, 5, 6}
element = int(input("Enter the Element: "))

if element in s:
    print("Element in set")
else:
    print("Element not in set")

# Write a program to find the length of a set.

s = {10,20,30,40,50}
print(f"length of a set : {len(s)}")

# (OR)

s = {10,20,30,40,50}
count = 0
for i in s:
    count = count + 1
print("Length of set:", count)


# Write a program to remove duplicate elements from a list using a set.

s = [2,3,4,5,6,2,3,7,8]

print(set(s))

# Write a program to find the union of two sets.

s1 = {1,2,3,7}
s2 = {2,5,7,3}
print(s1 | s2)

# (OR)

s1 = {1,2,3,7}
s2 = {2,5,7,3}
print(s1.union(s2))

# Write a program to find the intersection of two sets.

s1 = {1,2,3,7}
s2 = {2,5,7,3}
print(s1 & s2)

# (OR)

s1 = {1,2,3,7}
s2 = {2,5,7,3}
print(s1.intersection(s2))

# Write a program to find the difference between two sets.

s1 = {1,2,6,3,7}
s2 = {2,5,7,3}
print(s1 - s2)

# (OR)

s1 = {1,2,3,7}
s2 = {2,5,7,3}
print(s1.difference(s2))


# Write a program to find the symmetric difference between two sets.

s1 = {1,2,3,7}
s2 = {2,5,7,3}
print(s1 ^ s2)

# (OR)

s1 = {1,2,3,7}
s2 = {2,5,7,3}
print(s1.symmetric_difference(s2))

# Write a program to check whether one set is a subset of another.

s1 = {1,2,3}
s2 = {1,2,3,4,5,6,7}

print(s1.issubset(s2))

# Write a program to check whether one set is a superset of another.

s1 = {1,2,3}
s2 = {1,2,3,4,5,6,7}

print(s2.issuperset(s1))

# Write a program to check whether two sets are disjoint.

s1 = {1,2}
s2 = {3,4,6}

print(s1.isdisjoint(s2))

# Write a program to find common elements among three sets.

s1 = {1,2,3}
s2 = {2,3,5}
s3 = {3,5,6,2}

print(s1 & s2 & s3)

# Write a program to find unique elements from two sets.

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 ^ s2)   

# Write a program to convert a list into a set and back to a list.

lst = [1,2,3,3,4]

s = set(lst)
new_lst = list(s)

print(new_lst)


# Write a program to remove all elements from a set.

s = {15,20,35}
s.clear()
print(s)

# Write a program to copy one set into another.

s1 = {3,7,9,2}
s2 = s1.copy()

print(s2)

# Write a program to iterate through a set using a loop.

s = {10,20,30}

for i in s:
    print(i)


# Write a program to count the number of unique words in a sentence using a set.

sentence = "python is easy and python is powerful"

words = sentence.split()
unique_words = set(words)

print("Unique words:", len(unique_words))


# Write a program to find duplicate elements in a list using sets.

lst = [1,2,3,2,4,1]

duplicates = set()
seen = set()

for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)

# Write a program to compare two sets for equality.

s1 = {1,2,3}
s2 = {3,2,1}

print(s1 == s2)


# Write a program to demonstrate that sets are unordered.

s = {5,1,3,2}
print(s)


# Write a program to create a set of even numbers from 1 to 50.

even = {i for i in range(1,51) if i % 2 == 0 }
print(even)


# Write a program to create a set of characters from a string.

s = "python"

char_set = set(s)
print(char_set)

# Write a program to find elements present in one set but not in another.

s1 = {1,2,3,4}
s2 = {3,4}

print(s1 - s2)

# Write a program to store multiple frozensets inside a set.

fs1 = frozenset({1,2})
fs2 = frozenset({3,4})

s = {fs1, fs2}

print(s)

# Write a program to use a frozenset as a dictionary key.

fs = frozenset({1,2})

d = {fs: "value"}

print(d)

# Write a program to check whether a set is empty.

s = set()

if not s:
    print("Set is empty")

# Write a program to demonstrate the immutability of a frozenset 

fs = frozenset({1, 2, 3})

# fs.add(4)  --> Error 