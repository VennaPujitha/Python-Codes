# 🔹 Basic String Programs

# Write a program to read a string and print it.

text = input("Enter the string: ")
print(text)

# Write a program to find the length of a string.

text = input("Enter the string: ")
length = len(text)
print("Length of the string:", length)


# Write a program to convert a string to uppercase.

text = input("Enter the Text: ")
print(text.upper())

# Write a program to convert a string to lowercase.

text = input("Enter the Text: ")
print(text.lower())

# Write a program to reverse a string.

text = input("Enter the text: ")
print(text[::-1])

# Write a program to check whether a string is empty or not.

text = input("Enter the text: ")

if text == "":
    print("Empty string")
else:
    print("Not an empty string")


# 🔹 String Logic / Conditions

# Write a program to check whether a string is a palindrome.

text = input("Enter the String:")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Write a program to check whether a character is a vowel or consonant.

vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
char = input("Enter a character: ")

if char in vowels:
    print("Vowel")
else:
    print("Consonant")


# Write a program to count vowels in a string.

text = input("Enter the string: ")
vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)

# Write a program to count consonants in a string.

text = input("Enter the string: ")
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0

for char in text.lower():
    if char.isalpha() and char not in vowels:
        count += 1

print("Consonants count:", count)


# Write a program to check whether a string contains only alphabets.

text = input("Enter the string: ")

if text.isalpha():
    print("The string contains only alphabets")
else:
    print("The string does not contain only alphabets")


# Write a program to check whether a string contains digits.

text = input("Enter teh Number:")
if text.isdigit():
    print("The string contains only digits")
else:
    print("The string does not contain only digits")

# 🔹 Loop-based String Programs

# Write a program to count characters in a string using a loop.

count = 0
Text = input("Enter the String: ")
for char in Text:
    count = count + 1
print("Number of characters:", count)

# Write a program to count spaces in a string.

count = 0
Text = input("Enter the String: ")
for char in Text:
    if char.isspace():
        count = count + 1

print("Number of spaces:", count)


# Write a program to count words in a string.

text = input("Enter the string: ").strip()
count = 0

for char in text:
    if char == ' ':
        count += 1

if text:
    count += 1

print("Word count:", count)


# Write a program to print each character of a string on a new line.

text = input("Enter the String: ")
for char in text:
    print(char)


# Write a program to find frequency of each character in a string.

text = input("Enter the String: ")
checked = ""

for char in text:
    if char not in checked:
        print(char, ":", text.count(char))
        checked += char


# 🔹 String Comparison & Search

# Write a program to compare two strings.

text1 = input("Enter the String1: ")
text2 = input("Enter the String2: ")
if text1==text2:
    print("Same Strings")
else:
    print("Not Same Strings")

# Write a program to check whether a substring exists in a string.

text = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in text:
    print("Substring exists in the string")
else:
    print("Substring does not exist in the string")

# Write a program to find the first occurrence of a character.

text = input("Enter the string: ")
char = input("Enter the character: ")

if char in text:
    print("First occurrence index:", text.find(char))
else:
    print("Character not found")


# Write a program to find the last occurrence of a character.

text = input("Enter the string: ")
char = input("Enter the character: ")

if char in text:
    print("Last occurrence index:", text.rfind(char))
else:
    print("Character not found")


# #🔹 String Modification

# Write a program to replace a character in a string.

text = input("Enter the string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")

new_text = text.replace(old_char, new_char)
print("Updated string:", new_text)


# Write a program to remove spaces from a string.

text = input("Enter the string :")
new_text = "".join(text.split())
print("String without spaces:", new_text)

 # (OR)

text = input("Enter the string: ")
new_text = ""

for char in text:
    if char != " ":
        new_text += char

print("String without spaces:", new_text)


# Write a program to remove duplicate characters from a string.

string = input("Enter the string: ")
result = ""

for char in string:
    if char not in result:
        result += char

print("String after removing duplicates:", result)


# Write a program to remove vowels from a string.

text = input("Enter the string: ")
result = ""

for char in text:
    if char.lower() not in "aeiou":
        result += char

print("String after removing vowels:", result)



# Write a program to swap first and last characters of a string.

text = input("Enter the string: ")

if len(text) < 2:
    print("String is too short to swap")
else:
    new_text = text[-1] + text[1:-1] + text[0]
    print("After swapping:", new_text)



##🔹 Interview-Level String Questions

# Write a program to find the longest word in a string.

text = input("Enter the sentence: ")

words = text.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# Write a program to check whether two strings are anagrams.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")


# Write a program to capitalize the first letter of each word.

text = input("Enter the String: ")
print(text.title())


# Write a program to reverse words in a string.

text = input("Enter the string: ")

words = text.split()
reversed_words = words[::-1]

print("Reversed words:", " ".join(reversed_words))


# Write a program to count uppercase and lowercase letters separately.

text = input("Enter the string: ")

upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)