# LIST – CODING QUESTIONS
# Write a program to create a list and print all its elements.

lst = [2,4,6,7]
for i in lst:
    print(i)

# Write a program to find the length of a list.

lst = [10,20,30,40,50]
print(len(lst))

# Write a program to find the sum of all elements in a list.

lst = [10,30,50]
print(sum(lst))

# Write a program to find the largest element in a list.

lst = [15,20,35,80,65,11]
print(max(lst))

# Write a program to find the smallest element in a list.

lst = [15,20,35,80,65,11]
print(min(lst))

# Write a program to count the number of elements in a list.

lst = [15,20,35,80,65,11]
count = 0
for i in lst:
    count = count + 1
print(count)

# Write a program to check whether an element exists in a list.

lst = [1,2,3]
x = 2
print(x in lst)

# Write a program to remove duplicate elements from a list.

lst = [2,4,6,8,2,8,3,7,9]
new = []
for i in lst:
    if i not in new:
        new.append(i)    
print(new)

# Write a program to sort a list in ascending order.

lst = [20,40,30,50,10]
lst.sort()
print(lst)

# Write a program to sort a list in descending order.

lst = [20,10,45,36,80]
lst.sort(reverse=True) 
print(lst)

# Write a program to reverse a list.

lst = [10,76,54,38]
lst.reverse()
print(lst)

# Write a program to copy one list into another list.

lst = [3,6,4,7,2]
new_list = lst.copy()
print(new_list)

# Write a program to merge two lists.

l1 = [1, 2]
l2 = [3, 4]
print(l1 + l2)

# Write a program to find the index of an element in a list.

lst = [3,9,4,2,6]
print(lst.index(4))

# Write a program to find the frequency of an element in a list.

lst = [2,4,6,8,2,5]
print(lst.count(4))

# Write a program to remove an element from a list using remove().

lst = [2,3,5,6]
lst.remove(3)
print(lst)

# Write a program to delete an element from a list using del.

lst = [1, 2, 3] 
del lst[1] 
print(lst)

# Write a program to remove and return the last element using pop().

lst = [1,2,3]
print(lst.pop())
print(lst)

# Write a program to clear all elements from a list.

lst = [1,2,3]
lst.clear()
print(lst)

# Write a program to find common elements between two lists.

a = [1,2,3,4,5]
b = [2,4,6,7,8]
common = []
for i in a:
    if i in b:
        common.append(i)
print(common)

# Write a program to find unique elements in a list.

lst = [1, 1, 2, 3] 
unique = [] 
for i in lst:
    if lst.count(i) == 1:
        unique.append(i) 
print(unique)

# Write a program to check whether a list is empty.

lst = []
print(len(lst) == 0)

# Write a program to find even numbers in a list.

lst = [1,2,3,4]
for i in lst:
    if i%2 == 0:
        print(i)

# Write a program to find odd numbers in a list.

lst = [1,2,3,4]
for i in lst:
    if i%2 != 0:
        print(i)

# Write a program to count positive and negative numbers in a list.

lst = [-1,2,-3,4,-5]
pos = 0
neg = 0
for i in lst:
    if i > 0:
        pos = pos + 1
    else:
        neg =neg + 1
print(f"count of positive : {pos}")
print(f"count of negative : {neg}")


# LIST – INTERVIEW LEVEL CODING QUESTIONS
# Write a program to remove duplicate elements from a list without using set().

lst = [10,20,35,10,25,30]
res = []
for i in lst:
    if i not in res:
        res.append(i)
print(res)

# Write a program to find the second largest element in a list.

lst = [10,20,30,25]
lst = list(set(lst))
lst.sort()
print(lst[-2])

# Write a program to find the second smallest element in a list.

lst = [10,15,30,25]
lst = list(set(lst))
lst.sort()
print(lst[1])

# Write a program to rotate a list to the left by n positions.

lst = [1, 2, 3, 4]
n = 2
print(lst[n:] + lst[:n])

# Write a program to rotate a list to the right by n positions.

lst = [1, 2, 3, 4]
n = 1
print(lst[-n:] + lst[:-n])

# Write a program to check whether a list is a palindrome.

lst = [1,2,1]
print(lst == lst[::-1])

# Write a program to find the intersection of two lists without using built-in functions.

a = [10,20,30]
b = [20,30,40]
res = []
for i in a:
    if i in b:
        res.append(i)
print(res)

# Write a program to find the union of two lists.

a = [1,2]
b = [2,3]
res = a.copy()
for i in b:
    if i not in res:
        res.append(i)
print(res)

# Write a program to split a list into two halves.

lst = [1,2,3,4]
mid = len(lst) //2
print(lst[:mid], lst[mid:])

# Write a program to count the frequency of each element in a list.

lst = [1,2,2,3]
checked = []
for i in lst:
    if i not in checked:
        print(i, ":", lst.count(i))
        checked.append(i)

# Write a program to find all pairs in a list whose sum is equal to a given number.

lst = [1,2,3,4]
s = 5
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == s:
            print(lst[i], lst[j])

# Write a program to move all zero elements to the end of the list.

lst = [0,1,0,3]
res = [i for i in lst if i != 0]
res = res+[0] * lst.count(0)
print(res)

# Write a program to move all negative numbers to one side of the list.

lst = [-1,2,-3,4]
res = [i for i in lst if i < 0] + [i for i in lst if i >=0]
print(res) 

# Write a program to flatten a nested list.

lst = [[1,2],[3,4]]
flat = []
for i in lst:
    for j in i:
        flat.append(j)
print(flat)

# Write a program to find the missing number in a list of consecutive numbers.

lst = [1,2,4,5]
n = 5
print(n*(n+1)//2 - sum(lst))

# Write a program to remove elements at even indexes from a list.

lst = [1,2,3,4]
print([lst[i] for i in range(len(lst)) if i %2 !=0])

# Write a program to replace all negative numbers in a list with zero.

lst = [-1,2,-3]
print([0 if i <0 else i for i in lst])

# Write a program to find the longest sublist of consecutive numbers.

lst = [1,2,3,5,6]

longest = []
current = [lst[0]]

for i in range(1, len(lst)):
    if lst[i] == lst[i-1] + 1:
        current.append(lst[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [lst[i]]

if len(current) > len(longest):
    longest = current

print(longest)


# Write a program to check whether two lists are equal without using ==.

a = [1,2]
b = [1,2]
print(len(a) == len(b) and all(a[i] == b[i] for i in range(len(a))))

# Write a program to remove an element from a list at a given index.

lst = [1,2,3]
index = 1
del lst[index]
print(lst)

# Write a program to find the maximum product of two elements in a list.

lst = [1,10,2,6]
lst.sort()
print(lst[-1]*lst[-2])

# Write a program to reverse a list without using reverse() or slicing.

lst = [10,20,30]
res = []
for i in lst:
    res.insert(0,i)
print(res)

# Write a program to find common elements in three lists.

a = [1,2,3]
b = [2,3]
c = [3,2]
print([i for i in a if i in b and i in c])

# Write a program to separate even and odd numbers into two different lists.

lst = [1,2,3,4]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even, odd)

# Write a program to count how many times each element appears in a list using a loop.

lst = [1,2,2,3]
checked = []
for i in lst:
    if i not in checked:
        print(i, lst.count(i))
        checked.append(i)