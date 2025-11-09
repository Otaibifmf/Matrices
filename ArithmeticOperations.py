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


# from user
system = "5x -6y = 1" 


def getAugmentedMatrix(eq):
    print(extractNumbers(eq))




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

getAugmentedMatrix(system)

# What's next :hmmge:

# 1. Get Augmented Matrix from system:
#       5x - 6y = 1
#       6x - 5y = 10
#       Will become: [[5, -6, 1],
#                    [6, -5, 10]]

# 2. Reduce matrix using row operators:
#       Multiply a row by a nonzero constant: R1 = cR1
#       Swap two rows: R1 = R1 <--> R2
#       Add a constant multiple of one row to another row: R1 = cR1 + R2

# 3. Invert Matrix
#       If rows=cols; square matrix, then matrix A may have an inverse.
#       Apply row operators on A to get Identity.
#       Stick A and I next to eachother 
#       Apply same row operators to the whole row including I to get A^-1

# 4. Echolen: 
#       Leading terms are nonzero.
#       Leading term is on the right of the one above it.
#       If there exists a row of zeros, there must not be a row above it.
#       Back substitution to get answer.
#   4.1 Reduced Echolen: Same rules apply except first; Leading terms must be 1.

