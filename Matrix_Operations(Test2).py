import random

class Matrix:
    def __init__(self, matrix1_row, matrix1_column, matrix2_row, matrix2_column, user_input):
        if(user_input == 1):
            self.matrix1 = [[random.randint(0, 9) for _ in range(matrix1_column)]for _ in range(matrix1_row)]
            self.matrix2 = [[random.randint(0, 9) for _ in range(matrix2_column)]for _ in range(matrix2_row)]
            
        else:
            self.matrix1 = [[int(input(f"Enter value for element ({i1+1}, {j1+1})")) for j1 in range(matrix1_column)] for i1 in range(matrix1_row)]
            self.matrix2 = [[int(input(f"Enter value for element ({i2+1}, {j2+1})")) for j2 in range(matrix2_column)] for i2 in range(matrix2_row)]

        self.i1 = matrix1_row
        self.i2 = matrix2_row
        self.j1 = matrix1_column
        self.j2 = matrix2_column
        
        print("Matrix 1:")
        for row in self.matrix1:
            print(row)
        print("Matrix 2:")
        for row in self.matrix2:
            print(row)
        
        if(matrix1_row == matrix2_row and matrix1_column == matrix2_column):
            print("Matrix addition and subtraction: True")  #This means that you can do both of them 
            print("Matrix multiplication: True")

        elif(matrix1_column == matrix2_row):
             print("Matrix addition and subtraction: False") #This means that you can do only multi and substraction
             print("Matrix multiplication1: True")

        else:
            print("NOTE: You can't do any calculations on matrices")   

    def Addition(self):
        if self.i1 != self.i2 or self.j1 != self.j2:
            print("Addition is not possible due to mismatched size")
            return None            
        
        new_matrix = [[0 for _ in range(self.j1)]for _ in range(self.i1)]
        for i in range(self.i1):
            for j in range(self.j1):
                new_matrix[i][j] = self.matrix1[i][j] + self.matrix2[i][j]

        print("Result of Addition")
        for row in new_matrix:
            print(row)
        return new_matrix
    
    def Subtraction(self):
        if self.i1 != self.i2 or self.j1 != self.j2:
            print("Substraction is not possible due to mismatched size")
            return None            
        
        new_matrix = [[0 for _ in range(self.j1)]for _ in range(self.i1)]
        for i in range(self.i1):
            for j in range(self.j1):
                new_matrix[i][j] = self.matrix1[i][j] - self.matrix2[i][j]

        print("Result of Subtraction")
        for row in new_matrix:
            print(row)
        return new_matrix
    
    def Multiplication(self):
        if self.j1 != self.i2:
            print("Multiplication is not possible due to mismatched size")
            return None            
        
        new_matrix = [[0 for _ in range(self.j2)]for _ in range(self.i1)]
        for i in range(self.i1):
            for j in range(self.j2):
                for k in range(self.j1):                    
                    new_matrix[i][j] += self.matrix1[i][k] * self.matrix2[k][j]

        print("Result of Multiplication")
        for row in new_matrix:
            print(row)
        return new_matrix

print("Welcome to the Matrix Operations\nWould you choose your option(1 or 2):\n1: Set randomly\n2: Set manually")
user_input = input()
if(user_input == "1"):
    matrix = Matrix(3, 3, 3, 3, 1)  #For the default row/column size(recommended) and '1' is the user input
    matrix.Addition()
    matrix.Subtraction()
    matrix.Multiplication()

elif(user_input == "2"):
    i1, i2, j1, j2 = map(int, input("Enter the rows/columns of matrix1/2 -> ").split()) #For example, 2 3 3 4
    if(i1 not in range(1, 10) or i2 not in range(1, 10) or j1 not in range(1, 10) or j2 not in range(1, 10)):
        print("Wrong size, the size of matrices must be include 1 to 9")
        sys.exit()

    matrix = Matrix(i1, i2, j1, j2, 2) #User inputs
    matrix.Addition()
    matrix.Subtraction()
    matrix.Multiplication()

else:
    print("Wrong input, try again:(")
    sys.exit()

