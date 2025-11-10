# 2D Array

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

E = [[3,2],
     [6,7],
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
    
    for row in Z:
        print(" ".join(f"{x:2}" for x in row))    
    return Z
        

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
    
    for row in Z:
        print(" ".join(f"{x:2}" for x in row))     
    return Z


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
 
    for row in Z:
        print(" ".join(f"{x:2}" for x in row))  
    return Z


def extractNumbers(input_string):
    nums = []
    current = ""

    for ch in input_string:
        if ch.isdigit() or ch == '-': # If num or negative num
            current += ch # Add current character to variable
        else:
            if current not in ("", "-"):
                nums.append(int(current)) # Enter values of current as integers
            current = ""


    if current not in ("", "-"):  # Adds the last number in the string
        nums.append(int(current))

    return nums                   


def generateIdentity(X):

    if(len(X[0]) != len(X)):
        print("Matrix must be a square.")
        return

    rows = len(X)
    cols = len(X[0])

    Z = [[0 for _ in range(cols)] for _ in range(rows)] 

    for i in range(rows):
        for j in range(cols):

            if (Z[i] == Z[j]):
                Z[i][j] = 1

            else:
                Z[i][j] = 0    

    for row in Z:
        print(" ".join(f"{x:2}" for x in row))     
    return Z     


def getAugmentedMatrix():
    Z = []
    print("Enter one System per line. Type 0 when finished.")

    while True:
        system = input("System: ").strip()
        if system == "0":
            break

        row = extractNumbers(system)
        Z.append(row)

    for row in Z:
        print(" ".join(f"{x:2}" for x in row))     
    return Z     


# What's next :hmmge:


# 1. Reduce matrix using row operators:
#       Multiply a row by a nonzero constant: R1 = cR1
#       Swap two rows: R1 = R1 <--> R2
#       Add a constant multiple of one row to another row: R1 = cR1 + R2

# 2. Invert Matrix
#       If rows=cols; square matrix, then matrix A may have an inverse.
#       Apply row operators on A to get Identity.
#       Stick A and I next to eachother 
#       Apply same row operators to the whole row including I to get A^-1

# 3. Echolen: 
#       Leading terms are nonzero.
#       Leading term is on the right of the one above it.
#       If there exists a row of zeros, there must not be a row above it.
#       Back substitution to get answer.
#   3.1 Reduced Echolen: Same rules apply except first; Leading terms must be 1.

