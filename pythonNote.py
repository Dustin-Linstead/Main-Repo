#use the hashtag to make notes
print("hello there")

#Variables:
#in JS, a variable needs to be listed as "var =", while Python lets you simply declare one and assign a value to it.
#The system recognises strings with good old fashioned quotation marks ("").
name = "Dustin"

#Naming conventions
#Variable names are 100% arbitrary to the computer, but its easy for code to get messy for the coder reading it. 
#snake case.
    #this means all lower case names, with underscores for spacing
    #as opposed to Camel casing in other languages, where there's no spacing, and you capatalize first letters.
    #Depending on where you work or your comfort, Either method is valid, AS LONG ARE YOU ARE CONSISTENT
grilled_cheese_sandwiches = "Yummy"
#its most effective for variable names to describe what values they hold.

#Data Types

#Primitive

    #String
        #"Dustin"
        #"Pizza"
        #'General Kenobi!'
        #(its important to note, you can use either single or double quotes to form a string of text, but if you need to use punctuation, be sure to use the opposite of whatever you used to form the string.)
        #"Dustin's"
        #'Hank"s'
    #interger
        #whole numbers
        #1
        #42
        #729
    #boolean
        #TRUE and FALSE
    #float(decimals)
        #3.2
        #3.14159
        #98.6
#Most data can be catergorized into these four types. This is why there are called "primitives", because they form the basics and fundamentals of data entry.

#Composite - Collection, Data structure
#These data types hold other data

    #Lists - arrays
        #l = []
        #some_list = ["Dustin", more_data, 45, ["Hello There", "General Kenobi!"]]
        #Like JavaScript arrays, Python lists are indexed, starting from position 0. So to call for a certain index, 
        # you use "some_list[1]". To access a nested list, you use "some_list[3-0]".
        # To add to a list, you use the ".append" function
        # "some_list.append('hello)"
        # Tuple -- a rare list that is imutable - that is, a list that can't be changed once the values are set
    #Dictonary
        #An unordered -NonIndexed
        #Key - Value pairs
        #ALL KEYS ARE STRINGS
        #"some_dict = {
        # 'name: 'Dustin Linstead'
        # 'age: 30"

#Conditionals

#You do not need parenthesis in Python. However, INDENTATION IS REQUIRED TO START A CODE BLOCK IN PYTHON. 
    #if age > 13:
        #print("You are old enough")
    #ALSO: unlike JS or CSS, ADDING A SEMICOLON (;) TO YOUR PYTHON WILL BREAK YOUR CODE
    #Instead of "if", "else if", and "else", you use "if", "elif", and "else".
    #your operaters are >, <, ==, !=, "none" (in place of "null"), ! ("not"), || ("or"), and && ("and").
    #Other operands include:
        #"and"	Checks that each expression on the left and right are both True	(1 <= 2) and (2 <= 3) => True
        #(1 <= 2) and (2 >= 3) => False
        #(1 >= 2) and (2 >= 3) => False
        #"or"	Checks if either the expression on the left or right is True	(1 <= 2) or (2 >= 3) => True
        #(1 <= 2) or (2 <= 3) => True
        #(1 >= 2) or (2 >= 3) => False
        #"not"	Reverses the true-false value of the operand	not True => False
        #not False => True
        #not 1 >= 2 => True
        #not 1 <= 2 => False
        #not (1 <= 2 and 2 >= 3)  => True
        #not 1 <= 2 and 2 >= 3 => False

#Printing Strings
name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

#using the + means you have to add spacing yourself between the end of the string and the +

#Literal String Interpolation
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#The .format method
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# % formatting
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

#Built-in String Methonds

#The following is a list of commonly used string methods:
#string.upper(): returns a copy of the string with all the characters in uppercase.
#string.lower(): returns a copy of the string with all the characters in lowercase.
#string.count(substring): returns number of occurrences of substring in string.
#string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
#string.find(substring): returns the index of the start of the first occurrence of substring within string.
#string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
#string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
#string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

#Common Functions

#If we're ever unsure of a value or variable's data type, we can use the type function to find out. For example:
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>


#For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can use the len function to get the length:
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

#Type Casting or Explicit Type Conversion
#We may find ourselves wanting to change a value's data type from one type to another. For example, in the Hello World assignment, trying to print a string plus a number resulted in a TypeError. Python doesn't know how to add a string and a number, but it can add two strings together, so if we can cast the number as a string, then we will be able to "add" the two values together, like so:
print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

#Another example may be receiving a string input from a user that we want to treat as a number:
total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

#For Loops

#For Loops with Range
#If we want to iterate through numbers, we can use Python's for loop and range function.

#for x in range(0, 10, 1)
    #what to do in each iteration

#Notice that range takes 3 arguments. The first value is where the loop should begin, the second value is where the loop should end (exclusive), and the third value is how to increment the iterator.

#The range function actually comes with a few shortcuts. If we know the increment is going to be plus one, we can actually just ignore the third argument. Furthermore, if we know the increment is going to be positive one and the loop starts at 0, we can also leave off the first argument. In other words, each of the following will result in exactly the same loop:
    #for x in range(0, 10, 1):
#for x in range(0, 10):	# increment of +1 is implied
#for x in range(10):	# increment of +1 and start at 0 is implied
#Note that if you need to specify an increment other than +1, all three arguments are required.
#for x in range(0, 10, 2):
    #print(x)
# output: 0, 2, 4, 6, 8
#for x in range(5, 1, -3):
    #print(x)
# output: 5, 2

#If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value, but if we are not interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly!

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

#Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary.
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

#That means if we want the values of our dictionary, we might do something like this:
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

#Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. Test these out to get a better understanding:
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

#While loops are another way of looping while a certain condition is true.

#Remember this for loop?
for count in range(0,5):
    print("looping - ", count)

#We can rewrite it as a while loop:
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

#The basic syntax for a while loop looks like this:
#while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

#Loop Control

#We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

#When you want finer control over your loops, use the following statements to do so.

#Break
#The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be #used in both while and for loops.

#The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop.

#When loops are nested, a break will only exit from the innermost loop.

#The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.

#The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.

#Lambda functions
#Another type of function mentioned earlier is the anonymous function. Simply put, an anonymous function is a function without a name. In Python, anonymous functions are created with the lambda keyword. These functions are used for various purposes:

#they are handy in situations where we only need to use the function once
#they are lightweight when we need to break down complex tasks into small, specific tasks
#they are convenient as arguments to functions that require functions as parameters

#Earlier, we defined the square() function that takes in one parameter (num), squares it and then returns it:

#def square(num):
    #x = num ** 2
    #return x

#Now we can rewrite this function as an anonymous (nameless) lambda function:

#lambda num: num ** 2

#This means "here is an anonymous (nameless) function that takes one argument, called num, and returns num**2.

#What if you wanted to create an anonymous (nameless) function that takes two arguments and returns the sum of the two arguments?

#lambda num1, num2: num1+num2copy
#This means "here is an anonymous (nameless) function that takes two arguments: num1, and num2; and returns num1+num2.

#A lambda could be:

#an element in a list:

# create a new list, with a lambda as an element
#my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
#print(my_list[2]) # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
#my_list[2](5)

#passed to another function as a callback:

# define a function that takes one input that is a function
#def invoker(callback):
    # invoke the input pass the argument 2
    #print(callback(2))
#invoker(lambda x: 2 * x)
#invoker(lambda y: 5 + y)

#stored in a variable:

#add10 = lambda x: x + 10 # store lambda expression in a variable
#add10(2)  # returns 12
#add10(98) # returns 108

#returned by another function:

#def incrementor(num):
    #start = num
    #return lambda x: num + x

#Lambdas & Other Functions
#Sometimes when you invoke a function, one of the arguments may need to be a function. This is where lambdas come in handy - a place where you might not want to declare a completely new function with the def keyword. For example, let's talk about the map function which takes in a function and a list as parameters, then applies the function to each element in the list and returns a map object, which can be easily converted to a list. One way we could do this is like this:

# create a list
#my_arr = [1,2,3,4,5]
# define a function that squares values
#def square(num):
    #return num ** 2
# invoke map function
#print(list(map(square, my_arr)))

#The output is:

#[1,4,9,16,25]

#This way is fine and works, but let's say we never use the square function again in our program. Defining a function simply for that purpose is not quite necessary, which is why lambdas are useful when we only need a function once. This way we don't need to define a function and unnecessarily consume memory and complicate our code, just to produce the same result:

#my_arr = [1,2,3,4,5]
#print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a lambda as the first argument