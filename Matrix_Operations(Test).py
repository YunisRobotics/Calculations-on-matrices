import random

print("Fill row/column info for the matrix 1 and matrix 2: ")
a1 = int(input("Matrix1 Row -> "))
b1 = int(input("Matrix1 Column -> "))
matrix1 = [[0 for _ in range(b1)] for _ in range(a1)]
a2 = int(input("Matrix2 Row -> "))
b2 = int(input("Matrix2 Column -> "))
matrix2 = [[0 for _ in range(b2)] for _ in range(a2)]
print("Please, fill the numbers to matrix 1 and matrix 2")
for i in range(a1):
    for j in range(b1):
        matrix1[i][j] = random.randint(0,9)

for i in range(a2):
    for j in range(b2):
        matrix2[i][j] = random.randint(0,9)


print(matrix1)
print(matrix2)
