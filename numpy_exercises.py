#1)Use the following code for the questions below:
import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#2)How many negative numbers are there?
(a < 0).sum()

#3)How many positive numbers are there?
(a > 0).sum()

#4)If you were to add 3 to each data point, 
#how many positive numbers would there be?
plus_three = a + 3
(plus_three > 0).sum()

#5)If you squared each number, 
#what would the new mean and standard deviation be?
a_squared = a ** 2
np.average(a_squared)
a_squared.std()

#6)A common statistical operation on a dataset is centering. 
#This means to adjust the data such that the center of the data is at 0. 
#This is done by subtracting the mean from each data point. 
#Center the data set.
center = a - np.mean(a)

#7)Calculate the z-score for each data point. 
#Recall that the z-score is given by:
#Z = (x−μ)/σ
zscore = center/a.std()

#8)Copy the setup and exercise directions from More Numpy Practice 
#into your numpy_exercises.py and add your solutions.

import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
def product(list): #defining a function to take the product of all numbers in a list
    total = 1 #creating a running count called total
    for number in list: #for all numbers in a list
        total *= number #take the total and multiply it by the number in a list
    return total #return the product of all numbers in the list
product_of_a = product(a) #create a variable called product_of_a and run the product function with the list a
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [number ** 2 for number in a] #create a list that squares a number for all numbers in 'a'
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
def odds(list): #define a function called odd that takes in a list
    odd = [] #creating an empty list called odd 
    for number in list: #for all numbers in a list
        if number % 2 == 1: #if a number divided by 2 has a remainder of 1(odd number)
            odd.append(number) #then add that number to the list called odd
    return odd #return the odd list with only odd numbers
odds_in_a = odds(a) #creating a variable call odds_in_a that runs the odds function to find all the odd numbers in 'a'
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
def evens(list): #define a function called even that takes in a list
    even = [] #creating an empty list called even
    for number in list: #for all numbers in a list
        if number % 2 == 0: #if a number divided by 2 has a remainder of 0(even number)
            even.append(number) #then add that number to the list called even
    return even #return the even list with only even numbers
evens_in_a = evens(a) #creating a variable call evens_in_a that runs the evens function to find all the even numbers in 'a'
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

B = np.array([
    [3, 4, 5],
    [6, 7, 8]
])
B.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

B.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

B.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

B.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

B.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

np.square(B)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

B[B % 2 == 1]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

B[B % 2 == 0]


# Exercise 9 - print out the shape of the array b.
B.shape
# Exercise 10 - transpose the array b.
np.transpose(B)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(B,(1,6))
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(B,(1,6))
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
C = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
C.min()
C.max()
C.sum()
C.prod()
# Exercise 2 - Determine the standard deviation of c.
C.std()
# Exercise 3 - Determine the variance of c.
C.var()
# Exercise 4 - Print out the shape of the array c
C.shape
# Exercise 5 - Transpose c and print out transposed result.
tranc = np.transpose(C)
print(tranc)
# Exercise 6 - Get the dot product of the array c with c. 
C.dot(C)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
(C * tranc).sum()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
(C * tranc).prod()

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

D = np.array([
     [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
np.sin(D)
# Exercise 2 - Find the cosine of all the numbers in d
np.cos(D)
# Exercise 3 - Find the tangent of all the numbers in d
np.tan(D)
# Exercise 4 - Find all the negative numbers in d
D[(D < 0)]
# Exercise 5 - Find all the positive numbers in d
D[(D > 0)]
# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(D)
# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(D))
# Exercise 8 - Print out the shape of d.
D.shape
# Exercise 9 - Transpose and then print out the shape of d.
print(np.transpose(D))
# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(D,(9,2))