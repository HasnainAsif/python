########################### Basics with Game Start ############################
# import random
# # from random import choice
# # from random import choice as my_choice

# def get_choices():
#   player_choice = input("Enter a choice: rock, paper, scissors: ")
#   options = ['rock','paper','scissors']
#   computer_choice = random.choice(options)
#   choices = {"player": player_choice, "computer": computer_choice}
#   return choices

# def check_win(player, computer):
#   print(f"You chose {player}, computer chose {computer}")
#   if(player == computer):
#     return "It's a tie!!!"
#   if(player == "rock"):
#     if(computer == "paper"):
#       return "Paper covers rock. You lose!!!"
#     else:
#       return "Rock smashes scissors. You win!!!"
#   elif(player == "paper"):
#     if(computer == "scissors"):
#       return "Scissors cut paper. You lose!!!"
#     else:
#       return "Paper covers rock. You win!!!"
#   elif(player == "scissors"):
#     if(computer == "rock"):
#       return "Rock smashes scissors. You lose!!!"
#     else:
#       return "Scissors cut paper. You win!!!"

# choices = get_choices()
# p_choice = choices["player"]
# c_choice = choices["computer"]

# result = check_win(p_choice, c_choice)
# print(result)
########################### Basics with Game End ############################

###### DATA TYPES
# complex from complex number
# bool for booleans
# str from strings
# int for integers
# float for float numbers
# dict for dictionaries -- like JSON Object in js
# list for lists -- like array in js
# tuple for tuples - immuteable array
# set for sets
# range from ranges

### DIFFERENT WAYS TO PRINT
# var1 = 'Hello'
# var2 = 'World'
# print("Hello World")
# print("Hello", "World", sep=",,,", end="!\n")

## f-string printing
# print(f"Here is {var1} {var2}")

## format printing
# print("Here is {} {}".format(var1, var2))
# print("Here is {0} {1}".format(var1, var2))

## print using sys.stdout.write()
# import sys
# sys.stdout.write("Hello World\n")

## Multi line printing
# print("""Here is
#       Multi line
#       printing""")
# print(f"""Here is
#       Multi line f-string
#       printing, {var1}""")

## Print to a file
# with open("./basic-practice/output.txt", "w") as file:
#     print("Hello World", file=file)

# ## print by using custom __str__ method in class
# class Person:
#   def __init__(self, name):
#     self.name = name
#   def __str__(self):
#     return f"Person: {self.name}"
# person = Person("Roger")
# print(person) # __str__ method


### CHECK TYPES OF VARIABLES
# name = "John"
# print(type(name))
# print(type(name) == str)
# print(type(str(29)) == str)

# print(isinstance(name, str))
# print(isinstance(2, float))
# print(isinstance(2.9, float))
# print(isinstance("20", int))

# ### Variables parsing
# print(isinstance(float(2), float))
# print(isinstance(int("20"), int))

### CONDITIONS
# a = 5
# b = 6
# c = False
# if(a < b and a != 0):
#   print("true")

# if(a > b or (not c)):
#   print("working")

# print([] or 'hey')
# print(False or [])

# print(False and [])

### TERNARY OPERATOR - From simple to ternary
# def is_adult(age):
#   if age > 18:
#     return True
#   else:
#     return False

# def is_adult2(age):
#   return True if age > 18 else False

# print(is_adult2(123))

###################### DATA TYPES
### STRING
## Multiline strings
# print("""Its a
#   multiline
# string
# """)

# print("hey".upper())
# print("hEy".lower())
# print("hey".title())

# print("hey".islower())
# print("hey".isupper())
# print("Hey".istitle())

# print("asd".isalpha())
# print("asd123".isalnum())
# print("2.3".isdecimal())
# print("28212".isdecimal())

# print(len("asd"))

# name = "beau"
# print("ea" in name)
# print(f"string with index: {name[1]}, {name[-1]}")
# print(f"string slicing: {name[1: 3]}, {name[1:]}, {name[: 3]}, {name[-2:]}")

### BOOLEAN
# done = True
# print(type(done) == bool)

# book_1_read = True
# book_2_read = False
# read_any_book = any([book_1_read, book_2_read]) # like Array.some in JS
# read_all_book = all([book_1_read, book_2_read]) # like Array.every in JS
# print(read_any_book)
# print(read_all_book)

# print(12 > 10 and 12 < 18)
# print(12 > 10 or 12 < 18)
# print(not 12 > 10)

### NUMBER
# num1 = 2 + 3j
# num2 = complex(2, 3)
# print(num1.real, num1.imag)
# print(num2.real, num2.imag)

# print(abs(-5.5))
# print(round(5.49))

### ENUMS
# # (for declaring constant variables)
# from enum import Enum

# class State(Enum):
#   INACTIVE = 0
#   ACTIVE = 1

# print(State.ACTIVE.value)
# print(State['ACTIVE'].value)
# print(State['ACTIVE'])
# print(State(1))

# print(list(State))
# print(len(State))

### USER INPUT
# print("Enter your age")
# age = input()
# print("Your age is " + age)

# age = input("Enter your age: ")
# print("Your age is " + age)

### LISTS
# dogs = ["Roger", 1, "Syd", True]

# print("Syd" in dogs)
# print(len(dogs))
# print(dogs.index('Syd'))

# print(dogs[1], dogs[-2])
# print("Slicing: ", dogs[1:3], " - " , dogs[:3])

# arr = [1,2,3,4,5,6,7,8]
# print("Slicing with step: ", arr[1:6:2]) # 2, 4, 6

## Replace or add items
# dogs[1] = 5
# dogs.append("asd") # like Array.push in JS
# dogs.extend(["dsa", 54]) # for concat two arrays
# dogs += [False, 6453] # for concat two arrays
# print(dogs)

## Delete items
# del dogs[1] # Delete element at 1st index
# del dogs[0:2] # Delete elements at 0 and 1 index
# dogs.remove(1)
# print(dogs.pop()) # remove last item
# print(dogs)

## Insert item in array
# dogs.insert(2, "items") # insert item on specific index
# print(dogs)

# dogs[1:1] = ["item1", "item2"] # append array into dogs[1]
# print(dogs)

# dogs[1:4] = ["item1", "item2"] # get dogs index 1,2,3 and replace with new array items
# print(dogs)

## Concatenate Lists
# myConcatenatedList = [1,2,3] + [2,3,4]
# print(myConcatenatedList)

# items = ["Roger", "bob", "Syd", "Quincy"]

# items.sort() # sort current array - sort changes original array
# print(items)

## Copy List
# itemsCopiedReference = items # Reference is copied
# itemsCopiedValue = items[:] # Value is copied
# itemsCopiedValueOtherway = list(items) # Value is copied
# itemsCopiedValue[0]=1
# itemsCopiedReference[1]=1
# print(itemsCopiedReference)
# print(itemsCopiedValue)
# print(items)

# items.sort(key=str.lower) # convert array to lowercase and sort
# print(items)

# sortedArray = sorted(items, key=str.lower) # convert array to lowercase and sort - donot change original array, instead return new array
# print("Original Array: \n", items)
# print("Sorted Array: \n",sortedArray)

### TUPLES - Immuteable array
# names = ("Roger", "Syd", "Asd")

# print(len(names))
# print("asd" in names)

# print(names.index("Roger"))
# print(names[0], names[-1])
# print(names[:2])

# print(sorted(names))

# newTuple = names + ("Tina", "Quinchy")
# print(newTuple)

### Dictionaries
# dog = { "name": "Roger", "age": 8, "height": 2 }

# print(dog["name"])

# dog["name"] = 'Syd'
# print(dog)

# print(dog.get("color", "brown")) # on retrieving, set default value if not exist

# print(dog.pop("name")) # Delete name from dog
# print(dog)

# print(dog.popitem()) # Delete last entry from dog
# print(dog)

# print("age" in dog) 
# print(len(dog)) 

# print(dog.keys())
# print(list(dog.keys()), "\n")
# print(dog.values())
# print(list(dog.values()), "\n")
# print(dog.items())
# print(list(dog.items()))

# dog["favourite food"] = "Meat"
# print(dog)

# dog_copy = dog.copy()
# del dog["name"]
# print(dog, " \n", dog_copy)

### SETS - Immutable
# set1 = {"Roger", "Syd"}
# set2 = {"Syd"}

# print(list(set1))

# intersection = set1 & set2
# union = set1 | set2
# diff = set1 - set2 # Diff b/w sets
# print(intersection, union, diff)

# isSet1SuperSet = set1 > set2 # Is set1 contains all elements of set2
# isSet2SuperSet = set1 < set2 # Is set2 contains all elements of set1
# print(isSet1SuperSet, isSet2SuperSet)

### FUNCTIONS

## Builtin functions -- max, min, round, len, int, str, float, bool, print, type, help, sorted etc...
# help(max) # to get help on a function
# ?max # In IPython Shell, its same as help(max)

# import builtins
# print(dir(builtins)) # returns all builtins method names

## Methods on different types are available. Like upper, capitalize, lower, count, index are available for strings. append, remove, reverse, index, count for list etc...
# mystr = "MyString"
# print(mystr.upper()) # Way to call a method

# def hello(name = "Hasnain"):
#   print("Hello " + name)

# hello()
# hello("ads")

# def hello1(name):
#   if (not name):
#     return
  
#   return name, 8, 'Yes'

# print(hello1(False)) # return nothing
# print(hello1("asd"))

## Flexible Arguments in a function
# def add_all(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(add_all(2,3,4))

# def print_all(**kwargs):
#     for key, value in enumerate(kwargs):
#         print(key," : ", value)
# print_all(a='1',b='2',c='3')

### VARIABLE SCOPE

## change value of a globally declared variable, inside a function
# var1 = 10
# def my_func():
#     global var1 # By defining it here, we can now update value of globally declared var1.
#     var1 = 20
#     print(var1)
# my_func()
# print(var1) # if we comment "global var1", then var1 will return 10 here

## Outer variable is accessible inside of function
# age = 8
# def test():
#   print(age)
# print(age) # 8
# test() # 8


## a function inside of another function, cannot be accessibel outside of that function
# def talk(phrase):
#   def say(word):
#     print(word)
#   words = phrase.split(" ")
#   for word in words:
#     say(word)
# talk("I am going to buy the milk")

# def count():
#   count = 0
#   def increment():
#     nonlocal count # nonlocal is required for accessing parent variables, even after parent execution has ended.
#     count += 1
#     print(count)
#   increment()
#   print(count) # value of count updated in parent scope also, because we use "nonlocal count" in increment(child) function. "nonlocal" behaviour is same for parent function, as "global" for global scoped variables.
# count()


### CLOSURES

# count(parent) function's variable count is accessible in increment(child) function, even after count(parent) function has stopped its execution - thats what make closure

# def count():
#   count = 0 # closure in increment function
#   variable = 'value' # not a closure in increment funtions
#   def increment():
#     nonlocal count # nonlocal is required for accessing parent variables
#     count += 1
#     return count
#   return increment
# increment = count()
# print(increment.__closure__) # check, closure un increment function
# print(increment.__closure__ is not None) # check if increment function contains any closure
# no_of_closures = len(increment.__closure__)
# print("No of closure variables: ", no_of_closures)
# print("Closure values: ", [increment.__closure__[i].cell_contents for i in range(no_of_closures)])
# print(increment())
# print(increment())
# print("Check again Closure values: ", [increment.__closure__[i].cell_contents for i in range(no_of_closures)])
# print(increment())

### OBJECTS
# each primitive and non-primitive type is actually an object

# age = 8
# print(age.real)
# print(age.imag)
# print(age.bit_length())

# items = [1,4]
# items.append(2)
# print(items)
# print(id(items))

### LOOPS

## While loop
# count = 0
# while(count < 10):
#   print('The condition is True', count)
#   count += 1

# print("After the loop")

## For loop
# items = ["beau", "syd", "quincy"]

# for item in items:
#   print(item)

# #for index, item in enumerate(items): # its same as below
# for [index, item] in enumerate(items):
#   print(index, item) 

##range(10, 20, 2) // 10 is starting, 20 is ending, 2 is increment
# for item in range(10, 20, 2):
#   print(item)

## break, continue
# items = [1, 2, 3, 4, 5]

# for item in items:
#   if item % 2 == 0:
#     continue
#   print('odd number: ' + str(item))

# for item in items:
#   if item == 3:
#     break
#   print('breakable: ' + str(item))

## Iterating a dictionary
# dict = {
#     "key1": "val1",
#     "key2": "val2",
#     "key3": "val3",
# }
# for key, value in dict.items():
#     print(key, value)

### CLASSES

# class Animal:
#   def walk(self):
#     print("Walking...")
# # Animal is inherited in  Dog
# class Dog(Animal):
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
  
#   def bark(self):
#     print("Woof!")

# roger = Dog("Roger", 8)
# print(roger.name, roger.age)
# roger.bark()
# roger.walk()

# class WithoutMethods:
#   pass

### MODULES

# import dog
# dog.bark()

# from dog import bark
# bark()

## import file from a folder
# from lib import dog
# dog.bark()

# from lib.dog import bark
# bark()

## commonly used libraries
# math for math utilities
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operation System Utilities
# random for randum number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLs

# import math
# print(math.ceil(4.3), math.floor(4.3), math.sqrt(4))

# from math import sqrt
# print(sqrt(4))

### ACCEPTING ARGUMENTS FROM CLI

# import sys
# print(sys.argv)
# print("Hey: ", sys.argv[1])

## NOT IN WORKING CONDITION
# import argparse

# parser = argparse.ArgumentParser(
#   description = "This program prints the name of dogs"
# )
# print(parser)

# parser.add_argument('-c', '--color', metavar='color', choices = {"red", "yellow"} required=True, help='the color to search for')

# args = parser.parse_args()
# print(args.color)

### LAMBDA FUNCTIONS
## Must have argument and return value
## Single line function

# multiply = lambda a, b: a * b
# print(multiply(5, 3))

### MAP, FILTER, REDUCE

## MAP
# numbers = [1, 2, 3, 4]
# def double(num):
#   return num * 2
# double = map(double, numbers)
# print(list(doubleItems))

## Better way of above
# double = lambda num: num * 2
# doubleItems = map(double, numbers)
# print(list(doubleItems))

## More Better way of above
# doubleItems = map(lambda num: num * 2, numbers)
# print(list(doubleItems))

## FILTER
# numbers = [1, 2, 3, 4]
# def isEven(num):
#   return num % 2 == 0
# evenNumbers = filter(isEven, numbers)
# print(list(evenNumbers))

## Better way
# evenNumbers = filter(lambda num: num % 2 == 0, numbers)
# print(list(evenNumbers))

## REDUCE

# monthDetail = [
#   {
#     "type":"Dinner",
#     "price": 80
#   },
#   {
#     "type":"Car repair",
#     "price": 120
#   },
# ]
# sum = 0
# for entry in monthDetail:
#   sum += entry['price']
# print(sum)

## Simple way to add expenses
# expenses = [
#   ('Dinner', 80),
#   ('Car repair', 120)
# ]
# sum = 0
# for expense in expenses:
#   sum += expense[1]
# print(sum)

## Better way
# from functools import reduce
# expenses = [
#   ('Dinner', 80),
#   ('Car repair', 120)
# ]
# sum = reduce(lambda acc, cur: acc + cur[1] , expenses, 0)
# print(sum)

### RECURSION
# def factorial(val):
#   if(val == 1): return 1
#   return val * factorial(val - 1)
# print(factorial(5))
# print(factorial(4))


### DOCSTRINGS

# # Example #1
# import inspect
# def increment(n):
#   """-------Increment a number by 1---------"""
#   return n + 1
# help(increment)
# # print(inspect.getdoc(increment))
# # print(increment(2))


## Example #2
## For module documentation
# """Dog module

# This module does... bla bla bla and provide the following classes:

# -Dog
# ...
# """
# class Dog():
#   """A class representing a dog"""
#   def __init__(self, name, age):
#     """Initialize a new dog"""
#     self.name = name
#     self.age = age
  
#   def bark(self):
#     """Let the dog bark"""
#     print("Woof!")
# help(Dog)


## Type Annotations
# count: int = 0

# def increment(n: int) -> int:
#   return n + 1
# increment(1)

### EXCEPTIONS

## Exception handler Syntax
# try:
#   #some lines of code
# except <ERROR1>:
#   # handler <ERROR1>
# except <ERROR2>:
#   # handler <ERROR2>
# else:
#   # no exceptions were raised, the code ran successfully
# finally:
#   # do something in any case

## Handle generic exception
# def func(n):
#     try:
#       result = 2 ** n
#       print(result)
#     except:
#       print('Argument can only be number')
# func("asd")


## Handle type specific Exception
# try:
#   result = 2/0
# except ZeroDivisionError:
#   print('Cannot divide by zero')
# finally:
#   result = 1

# print(result)

## Raise exception
# try:
#   raise Exception('An Error!')
# except Exception as error:
#   print(error)

## Class Exception
# class DogNotFoundException(Exception):
#   print('inside')
#   pass

# try:
#   raise DogNotFoundException()
# except DogNotFoundException:
#   print('Dog not found!!!')

### Exception Handling with 'with'
## Without 'with'
# filename = '/Users/flavio/test.txt'
# try:
#   file = open(filename, 'r')
#   content = file.read()
#   print(content)
# except FileNotFoundError:
#   print('File not found')
# finally:
#   file.close()

## With 'with'
# filename = '/Users/flavio/test.txt'
# with open(filename, 'r') as file:
#   content = file.read()
#   print(content)

## PIP (package manager)
# URL: https://pypi.org/

# python -m pip install <package_name> // if below commands will not work, then use this one

## Install a package
# pip install <package_name> # pip install requests

## Upgrade a package
# pip install -U <package_name>

## Delete a package
# pip uninstall <package_name>

## Information about package
# pip show <package_name>

### List Compressions
# numbers = [1, 2, 3, 4, 5]

# number_powers_2 = [n**2 for n in numbers]
# print(number_powers_2)

# # Using Map
# num_powers_2 = list(map(lambda n: n**2 ,numbers))
# print(num_powers_2)

# # Simple Way
# numbers_pow_2 = []
# for n in numbers:
#   numbers_pow_2.append(n**2)
# print(numbers_pow_2)

### POLYMORPHISM
## Functions contain same names but in different classes
# class Dog:
#   def eat(self):
#     print('Dog Eating')

# class Cat:
#   def eat(self):
#     print('Cat Eating')

# animal1 = Dog()
# animal2 = Cat()

# animal1.eat()
# animal2.eat()

### OPERATOR OVERLOADING
# class Dog:
#   # the dog class
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __gt__(self, other):
#     return True if self.age > other.age else False

# roger = Dog('Roger', 8)
# syd = Dog('Syd', 7)

# print(roger > syd)

# __lt__() respond to the < operator
#  __eq__() respond to the == operator
# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator
# ... and many more
