# 2D Array, 3x3 Matrix

A = [[7,5,3],
     [1,0,8],
     [4,8,2]]

B = [[6,1,4],
     [5,8,2],
     [9,7,3]]

C = [[1,6],
     [2,7]]

D = [[3,8],
     [4,9]]


# Creates a function
def Addition(X,Y): # Takes two arrays
    if(len(X) != len(Y)): # If size of arrays are not equal quit
        print("Matrices must be the same size.")
        return
    
    rows = len(X) # Gets number of rows
    cols = len(X[0]) # Gets number of columns

    Z = [[0 for _ in range(cols)] for _ in range(rows)]  # Result array is same size of X, filled with zeros

    for i in range(rows):
        for j in range(cols):
            Z[i][j] = X[i][j] + Y[i][j]
    print(Z)            
        


def Subtraction(X,Y):
    if(len(X) != len(Y)): 
        print("Matrices must be the same size.")
        return
    
    rows = len(X)
    cols = len(X[0])

    Z = [[0 for _ in range(cols)] for _ in range(rows)]  

    for i in range(rows):
        for j in range(cols):
            Z[i][j] = X[i][j] - Y[i][j]
    print(Z)    


def DotProduct(X,Y):
    # Check if matrices are compatible
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


