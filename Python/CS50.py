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