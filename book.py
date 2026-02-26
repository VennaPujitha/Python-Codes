#1) Create a class Book:

# title
# author
# price

# Create method:
# is_expensive()
# Return True if price > 500 else False give me answers


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def is_expensive(self):
        if self.price > 500:
            return True
        else:
            return False


# Creating object
b1 = Book("Python Basics", "John", 650)
b2 = Book("C Programming", "David", 400)

# Checking if books are expensive
print(b1.title, "is expensive:", b1.is_expensive())
print(b2.title, "is expensive:", b2.is_expensive())