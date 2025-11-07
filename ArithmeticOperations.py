# User Matrix

rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
size = rows * cols
UserMatrix = [0] * size # Populates array sized by user with zeros. Size 9

TwoDUserMatrix = [[0] * cols for _ in range(rows)] # Size 3

# 2D Array, 3x3 Matrix

TwoDArray1 = [[1,2,3], # Size 3
              [4,5,6],
              [7,8,9]]

TwoDArray2 = [[9,8,7], # Size 3
              [6,5,4], 
              [3,2,1]]

# 3x3 Matrix
A = [1, 4, 5, # Size 9
     2, 5, 6,
     7, 2, 1]

B = [8, 5, 3, 
     9, 4, 2,
     1, 8, 0]

# 2x2 Matrix
D = [1, 4,
     7, 9]

E = [9, 2,
     3, 5]

# Creates a function
def Addition(X,Y,Z): # Takes three arrays
    if(len(X) == len(Y) == len(Z)): # If size of all arrays are equal then proceed else quit
        for i in range(size): 
            Z[i] = X[i] + Y[i]
        print(Z)
    else:
     print("Martices must be the same size")      


def Subtraction(X,Y,Z):
    if(len(X) == len(Y) == len(Z)):
        for i in range(size): 
            Z[i] = X[i] - Y[i]
        print(Z)
    else:
     print("Martices must be the same size")     


def DotProduct(X,Y,Z):
    for i in range(rows):
       for j in range(cols):
          for k in range(cols):
             Z[i][j] += X[i][k] * Y[k][j] # Works with 2D 3x3 Matrix
 
    print(Z)


DotProduct(TwoDArray1,TwoDArray2,TwoDUserMatrix)

# After getting a loop for DotProduct, make addition and subtraction use twodarrays


