#print("Hello,World!")

#Input Function can prompt the user for an input
name = input("Name: ")

#Print Function
#When + is used with strings it is called string concatenation
print("Hello," + name)

#F strings (AKA Formatted Strings)
print(f"Hello, {name}")

#Conditions (if statements)
#Casting String into integer
num = int(input("Number: "))
if num > 0:
    print("Num is positive")
elif num < 0:
    print("Num is negative")
else:
    print("Num is zero")

#Sequences
fName = "Joyce"
#Will take the first letter (Starts counting from 0)
print(fName[0])

#Data Structures
#List/Arrays (sequence of mutable (changable) values)
names = ["Harry", "Ron", "Hermione", "Ginny"]
print (names)
print(names[2])
#Append function addeds a new value to the end of the list/array
names.append("Draco")
#Sort function sorts the list/array in alphabetical order
names.sort()
#Tuple (sequence of immutable (not changeable) values)
coordinateX = 10.0
coordinateY = 20.0
#Example of a Tuple
#Tuples uses paraentheses
coordinate = (10.0, 20.0)
#set (Collection of unique values)
#Create empty set
s = set()
#Add function adds elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
#Remove function removes elements from the set
s.remove(2)
#Even if you have the same value more than once the value will only appear once in the set
print(s)
#len function will give you the length of a sequence (Tells you the number of thing in list, string, set, & etc)
print(f"The set has {len(s)} elements.")
#dict(AKA Dictionary) (Collection of key - value pairs)
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
#Adding a key - value pair to the dict
houses["Hermione"] = "Gryffindor"
#The square bracket helps to loop up values
print(houses["Harry"])

#Loops (For loops and While loops)
#For loops (Loops for a set number of times)
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
#Loops 6 times (Loops starts counting from zero)
for i in range(6):
    print(i)
#Loops each names in the names array
for name in names:
    print(names)
#Loops each character in fName string variable
for character in fName:
    print(character)

#Functions
#Create a function to find the square of any number
#Functions always starts with def (define the function)
def square(x):
    return x * x

#Object-Oriented Programming
#Classes (Template for a type of object)
#When creating a class always start with class, then name of the class followed by ()
class Point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2
#Create a new point
p = Point(2,8)
#Prints the x and y value
print(p.x)
print(p.y)
#Creating a class for airline to check if they are at capacity
class Flight():
    #Finds the capacity of a flight
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    #Adds new passengers 
    def add_passenger(self, name):
        #This means the same as if self.open_seats == 0
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    #Checks how many open seats there are 
    def open_seats(self):
        return self.capacity - len(self.passengers)
#Create a new flight
flight = Flight(3)
people = ["Harry", "Ron", "Ginny", "Hermione"]
#Loop through the people list to add them as a passenger
for person in people:
    success = flight.add_passenger(person)
    #if success is true print that the person is added successfully
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No avaiable seats for {person}")

#Decorators (A way to modify functions (Adding additional behavior to the function))
"""
The idea is that a decorator is going to be a functioon that takes a 
function of input and returns a modified version of that function as output
"""
"""
Create a function that moodifies another function by announcing that function is 
about to run and that the function is completed running
"""
#This function will return a new function
def announce(f):
    #This function wraps up function f with some additional behavior, so this is often called the wrapper function
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper
#Add the announce decorator
#@ symbol means to add a decorator
@announce
def hello():
    print("Hello, World!")
hello()

#lambda (More efficient way to represent functions)
hogwarts = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
#Create a function that tells sort how to sort the list of dict
def f(people):
    return people["name"]
#Using a key it tells sort to sort the list of dict by the names
hogwarts.sort(key = f)
#Another way to create a function to tell sort how to sort the list of dict
hogwarts.sort(key = lambda people: people["names"])
print(hogwarts)