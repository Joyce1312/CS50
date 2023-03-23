#Imports the whole CS50.py file
import CS50
#Loops 10 times to find the first 10 squares starting from 0
for i in range(10):
    print(f"The square of {i} is {CS50.square(i)}")

#Another way to import functions
#From the CS50.py file import the square function
from CS50 import square
#Loops 10 times to find the first 10 squares starting from 0
for i in range(10):
    print(f"The square of {i} is {square(i)}")