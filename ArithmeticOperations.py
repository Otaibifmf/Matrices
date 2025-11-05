
#3x3 Matrix
A = [1, 4, 5,
     2, 5, 6,
     7, 2, 1]

B = [8, 5, 3, 
     9, 4, 2,
     1, 8, 0]

C = [0, 0, 0, 
     0, 0, 0,
     0, 0, 0]


# Creates a function
def Addition(X,Y):
    
    for i in range(9): # In range of 9 when Matrix is 3X3.
        C[i] = X[i] + Y[i]

def Subtraction(X,Y):

    for i in range(9):
        C[i] = X[i] - Y[i]




#Addition(A,B)
#print(C)


Subtraction(B,A)
print(C)
