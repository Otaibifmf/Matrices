# 2D Array, 3x3 Matrix

TwoDArray1 = [[1,2,3], # Size 3
              [4,5,6],
              [7,8,9]]

TwoDArray2 = [[9,8,7], # Size 3
              [6,5,4], 
              [3,2,1]]

TwoDArray3 = [[1,6],
              [2,7]]

TwoDArray4 = [[3,8],
              [4,9]]

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
def Addition(X,Y): # Takes two arrays
    if(len(X) == len(Y)): # If size of both arrays are equal
        Z = [0] * len(X) # Result array is same size of X, filled with zeros
        for i in range(len(X)): 
            Z[i] = X[i] + Y[i] 
        print(Z)
    else:
     print("Martices must be the same size")      


def Subtraction(X,Y):
    if(len(X) == len(Y)):
        Z = [0] * len(X)
        for i in range(len(X)): 
            Z[i] = X[i] - Y[i]
        print(Z)
    else:
     print("Martices must be the same size")     


def DotProduct(X,Y):
    # Check if matrix are compatible
    if len(X[0]) != len(Y):
           print("The dimension aren't compatible for multiplication")
           return

    rows = len(X) # Gets number of rows in matrix X
    cols = len(Y[0]) # Gets number of columns in matrix Y
    inner = len(X[0])

    # Empty result matrix with size based on X&Y filled with zeros 
    Z = [[0 for _ in range(cols)] for _ in range(rows)] 

    for i in range(rows):
       for j in range(cols):
          Z[i][j] = 0
          for k in range(inner):
             Z[i][j] += X[i][k] * Y[k][j] 
 
    print(Z)


#DotProduct(TwoDArray1,TwoDArray2)
