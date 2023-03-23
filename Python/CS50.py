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
#Loops 6 times (Loops starts counting from one)
for i in range(6):
    print(i)
#Loops each names in the names array
for name in names:
    print(names)
#Loops each character in fName string variable
for character in fName:
    print(character)
