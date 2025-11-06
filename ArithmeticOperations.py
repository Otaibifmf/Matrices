# User Matrix

rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
size = rows * cols
UserMatrix = [0] * size # Populates array sized by user with zeros

# TwoDUserMatrix = [[0] * rows for _ in range(rows)]

# 2D Array, 3x3 Matrix

TwoDArray1 = [[1,2,3],
              [4,5,6],
              [7,8,9]]

TwoDArray2 = [[9,8,7],
              [6,5,4], 
              [3,2,1]]

# 3x3 Matrix
A = [1, 4, 5,
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

    # How do I loop this?
    # Doen't work when matrices are not the same size

    Z[0] = X[0][0] * Y[0][0] + X[0][1] * Y[1][0] + X[0][2] * Y[2][0] # Multiplying First Row by First Column
    Z[1] = X[0][0] * Y[0][1] + X[0][1] * Y[1][1] + X[0][2] * Y[2][1] # Multiplying First Row by Second Column
    Z[2] = X[0][0] * Y[0][2] + X[0][1] * Y[1][2] + X[0][2] * Y[2][2] # Multiplying First Row by Third Column

    Z[3] = X[1][0] * Y[0][0] + X[1][1] * Y[1][0] + X[1][2] * Y[2][0] # Multiplying Second Row by First Column
    Z[4] = X[1][0] * Y[0][1] + X[1][1] * Y[1][1] + X[1][2] * Y[2][1] # Multiplying Second Row by Second Column 
    Z[5] = X[1][0] * Y[0][2] + X[1][1] * Y[1][2] + X[1][2] * Y[2][2] # Multiplying Second Row by Third Column 

    Z[6] = X[2][0] * Y[0][0] + X[2][1] * Y[1][0] + X[2][2] * Y[2][0] # Multiplying Third Row by First Column
    Z[7] = X[2][0] * Y[0][1] + X[2][1] * Y[1][1] + X[2][2] * Y[2][1] # Multiplying Third Row by Second Column
    Z[8] = X[2][0] * Y[0][2] + X[2][1] * Y[1][2] + X[2][2] * Y[2][2] # Multiplying Third Row by Third Column

    print(Z)

