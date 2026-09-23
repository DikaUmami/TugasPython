#Python has a set of built-in methods that you can use on strings.
#ote: All string methods return new values. They do not change the original string.

# ==========================================================
# Contoh Penggunaan String Methods di Python
# ==========================================================

# capitalize() -> Converts the first character to upper case
x = "hello world"
print(x.capitalize())

# casefold() -> Converts string into lower case
x = "HELLO WORLD"
print(x.casefold())

# center() -> Returns a centered string
x = "hello"
print(x.center(20, "*"))

# count() -> Returns the number of times a specified value occurs
x = "I love apples, apples are my favorite fruit"
print(x.count("apples"))

# encode() -> Returns an encoded version of the string
x = "Hello World"
print(x.encode())

# endswith() -> Returns True if the string ends with the specified value
x = "Hello, welcome to my world."
print(x.endswith("world."))

# expandtabs() -> Sets the tab size of the string
x = "H\te\tl\tl\to"
print(x.expandtabs(2))

# find() -> Searches the string for a specified value and returns the position
x = "Hello, welcome to my world."
print(x.find("welcome"))

# format() -> Formats specified values in a string
x = "My name is {}, I am {} years old."
print(x.format("John", 36))

# format_map() -> Formats specified values in a string (menggunakan dictionary)
person = {"name": "John", "age": 36}
x = "My name is {name}, I am {age} years old."
print(x.format_map(person))

# index() -> Searches the string for a specified value and returns the position
x = "Hello, welcome to my world."
print(x.index("welcome"))

# isalnum() -> Returns True if all characters are alphanumeric
x = "Company12"
print(x.isalnum())

# isalpha() -> Returns True if all characters are in the alphabet
x = "CompanyX"
print(x.isalpha())

# isascii() -> Returns True if all characters are ascii characters
x = "Company123"
print(x.isascii())

# isdecimal() -> Returns True if all characters are decimals
x = "1234"
print(x.isdecimal())

# isdigit() -> Returns True if all characters are digits
x = "565543"
print(x.isdigit())

# isidentifier() -> Returns True if the string is a valid identifier
x = "Demo"
print(x.isidentifier())

# islower() -> Returns True if all characters are lower case
x = "hello world!"
print(x.islower())

# isnumeric() -> Returns True if all characters are numeric
x = "565543"
print(x.isnumeric())

# isprintable() -> Returns True if all characters are printable
x = "Hello! Are you #1?"
print(x.isprintable())

# isspace() -> Returns True if all characters are whitespaces
x = "   "
print(x.isspace())

# istitle() -> Returns True if the string follows the rules of a title
x = "Hello, And Welcome To My World!"
print(x.istitle())

# isupper() -> Returns True if all characters are upper case
x = "THIS IS NOW!"
print(x.isupper())

# join() -> Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# ljust() -> Returns a left justified version of the string
x = "hello"
print(x.ljust(20, "*"))

# lower() -> Converts a string into lower case
x = "Hello World"
print(x.lower())

# lstrip() -> Returns a left trim version of the string
x = "     banana     "
print(x.lstrip())

# maketrans() -> Returns a translation table to be used in translations
x = "Hi Sam!"
mytable = str.maketrans("S", "P")
print(x.translate(mytable))

# partition() -> Returns a tuple where the string is parted into three parts
x = "I could eat bananas all day"
print(x.partition("bananas"))

# replace() -> Returns a string where a specified value is replaced
x = "I like bananas"
print(x.replace("bananas", "apples"))

# rfind() -> Searches the string for a specified value, returns the LAST position
x = "Mi casa, su casa."
print(x.rfind("casa"))

# rindex() -> Searches the string for a specified value, returns the LAST position
x = "Mi casa, su casa."
print(x.rindex("casa"))

# rjust() -> Returns a right justified version of the string
x = "hello"
print(x.rjust(20, "*"))

# rpartition() -> Returns a tuple where the string is parted into three parts (dari kanan)
x = "I could eat bananas all day, bananas are my favorite"
print(x.rpartition("bananas"))

# rsplit() -> Splits the string at the specified separator, and returns a list
x = "apple, banana, cherry"
print(x.rsplit(", "))

# rstrip() -> Returns a right trim version of the string
x = "     banana     "
print(x.rstrip())

# split() -> Splits the string at the specified separator, and returns a list
x = "welcome to the jungle"
print(x.split())

# splitlines() -> Splits the string at line breaks and returns a list
x = "Thank you for the music\nWelcome to the jungle"
print(x.splitlines())

# startswith() -> Returns True if the string starts with the specified value
x = "Hello, welcome to my world."
print(x.startswith("Hello"))

# strip() -> Returns a trimmed version of the string
x = "     banana     "
print(x.strip())

# swapcase() -> Swaps cases, lower case becomes upper case and vice versa
x = "Hello My Name Is PETER"
print(x.swapcase())

# title() -> Converts the first character of each word to upper case
x = "Welcome to my world"
print(x.title())

# translate() -> Returns a translated string
x = "Hi Sam!"
mytable = str.maketrans("S", "P")
print(x.translate(mytable))

# upper() -> Converts a string into upper case
x = "Hello World"
print(x.upper())

# zfill() -> Fills the string with a specified number of 0 values at the beginning
x = "50"
print(x.zfill(10))