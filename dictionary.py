#  DICTIONARY – BASIC CODING QUESTIONS
# Write a program to create a dictionary and print all key–value pairs.

d = {"name": "Ravi", "age": 25, "city": "Hyderabad"}

for key, value in d.items():
    print(key, ":", value)

# Write a program to find the length of a dictionary.

d = {"a": 1, "b": 2, "c": 3}
print(len(d))

# Write a program to access the value of a given key.

d = {"name": "Ravi", "age": 25}
print(d["name"])

# Write a program to add a new key–value pair to a dictionary.

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)

# Write a program to update the value of an existing key.

d = {"a": 1, "b": 2}
d["a"] = 100
print(d)

# Write a program to delete a key from a dictionary using del.

d = {"a": 1, "b": 2}
del d["a"]
print(d)

# Write a program to remove a key using pop().

d = {"a": 1, "b": 2}
d.pop("b")
print(d)

# Write a program to check whether a key exists in a dictionary.

d = {"a": 1, "b": 2}

if "a" in d:
    print("Key exists")
else:
    print("Key not found")

# Write a program to print all keys of a dictionary.

d = {"a": 1, "b": 2}
print(d.keys())

# Write a program to print all values of a dictionary.

d = {"a": 1, "b": 2}
print(d.values())

#  DICTIONARY – INTERVIEW LEVEL CODING QUESTIONS

# Write a program to iterate through a dictionary using a loop.

d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(key, d[key])


# Write a program to count the frequency of each character in a string using a dictionary.

text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

# Write a program to count the frequency of words in a sentence using a dictionary.

sentence = "apple banana apple mango banana apple"
words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

# Write a program to find the key with the maximum value in a dictionary.

d = {"a": 10, "b": 50, "c": 20}

max_key = max(d, key=d.get)
print(max_key)

# Write a program to find the key with the minimum value in a dictionary.

d = {"a": 10, "b": 50, "c": 20}

min_key = min(d, key=d.get)
print(min_key)

# Write a program to merge two dictionaries.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)

# Write a program to remove duplicate values from a dictionary.

d = {"a": 1, "b": 2, "c": 1, "d": 3}

result = {}
for key, value in d.items():
    if value not in result.values():
        result[key] = value

print(result)


# Write a program to create a dictionary from two lists (keys list and values list).

keys = ["a", "b", "c"]
values = [1, 2, 3]

d = dict(zip(keys, values))
print(d)

# Write a program to sort a dictionary by keys.

d = {"b": 2, "a": 1, "c": 3}

sorted_d = dict(sorted(d.items()))
print(sorted_d)

# Write a program to sort a dictionary by values.

d = {"a": 3, "b": 1, "c": 2}

sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)

#  ADVANCED / LOGIC-BASED QUESTIONS

# Write a program to swap keys and values in a dictionary.

d = {"a": 1, "b": 2, "c": 3}

swapped = {v: k for k, v in d.items()}
print(swapped)

# Write a program to find common keys between two dictionaries.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

common = d1.keys() & d2.keys()
print(common)


# Write a program to check whether two dictionaries are equal without using ==.

d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}

if len(d1) != len(d2):
    print("Not Equal")
else:
    equal = True
    for key in d1:
        if key not in d2 or d1[key] != d2[key]:
            equal = False
            break
    print("Equal" if equal else "Not Equal")

# Write a program to create a nested dictionary and access inner values.

student = {
    "name": "Ravi",
    "marks": {"math": 90, "science": 85}
}

print(student["marks"]["math"])

# Write a program to flatten a nested dictionary.

d = {"a": 1, "b": {"c": 2, "d": 3}}

flat = {}

for key, value in d.items():
    if isinstance(value, dict):
        for k, v in value.items():
            flat[k] = v
    else:
        flat[key] = value

print(flat)

# Write a program to group elements having the same keys.

data = [
    {"a": 1, "b": 2},
    {"a": 3, "b": 4},
    {"a": 5, "b": 6}
]

result = {}

for d in data:
    for key, value in d.items():
        if key not in result:
            result[key] = []
        result[key].append(value)

print(result)

# Write a program to find the sum of all values in a dictionary.

d = {"a": 10, "b": 20, "c": 30}
print(sum(d.values()))

# Write a program to remove keys with empty values.

d = {"a": 1, "b": "", "c": None}

result = {k: v for k, v in d.items() if v}
print(result)

# Write a program to create a dictionary using dictionary comprehension.

d = {x: x*x for x in range(1, 6)}
print(d)

# Write a program to count how many times each element appears in a list using a dictionary.

lst = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)
