#User Matrix

rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
size = rows * cols

UserMatrix = [0] * size # Populates array sized by user with zeros


#3x3 Matrix
A = [1, 4, 5,
     2, 5, 6,
     7, 2, 1]

B = [8, 5, 3, 
     9, 4, 2,
     1, 8, 0]

#2X2 Matrix
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


Addition(D,E,UserMatrix)
