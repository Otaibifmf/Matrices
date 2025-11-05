#User Matrix

rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
size = rows * cols

U = [0] * size # Populates array sized by user with zeros


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
def Addition(X,Y,Z):
    
     for i in range(size): 
          Z[i] = X[i] + Y[i]
     print(Z)


def Subtraction(X,Y,Z):

     for i in range(size):
          Z[i] = X[i] - Y[i]
     print(Z)


