def createMatrix(n,k):
    matrix = [[k for x in range(n)]for y in range(n)]        #(n^2)
    return matrix                                            #(1)

def matrixAddition(matrix1, matrix2, n):
    addMatrix = createMatrix(n,0)                            #(n^2, because BigO notation for create matrix function is O(n^2) )
    for i in range(n):
        for j in range(n):
            addMatrix[i][j] = matrix1[i][j]+matrix2[i][j]    #(n^2)
    return addMatrix                                         #(1)

def matrixSub(matrix1, matrix2, n):
    matrixSub = createMatrix(n,0)                            #(n^2, because BigO notation for create matrix function is O(n^2) )
    for i in range(n):
        for j in range(n):
            matrixSub[i][j] = matrix1[i][j]-matrix2[i][j]    #(n^2)
    return matrixSub

def matrixMulti(matrix1, matrix2, n):
    matrixMulti = createMatrix(n,0)                          #(n^2, because BigO notation for create matrix function is O(n^2) )
    for i in range(n):
        for j in range(n):
            temp = 0                                         #(n^2)
            for k in range(n):
                temp = temp + matrix1[i][k]*matrix2[k][j]    #(n^3)
            matrixMulti[i][j] = temp                         #(n^3)
    return matrixMulti                                       #(1)

def scalarMultiplication(num, matrix,n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[i][j]*num                  #(n^2)
    return matrix                                            #(1)

n=5  
matrixB = createMatrix(n,2)
matrixC = createMatrix(n,3)
# A=B*C–2*(B+C)
matrixA = matrixSub(matrixMulti(matrixB,matrixC,n),scalarMultiplication(2,matrixAddition(matrixB,matrixC,n),n),n)
print(matrixA)
'''BigO notation for createMatrix is O(n^2), because of for loop and nested for loop;
matrixAddition is O(n^2), because of for loop and nested for loop;
matrixSub is O(n^2),  because of for loop and nested for loop;
matrixMulti is O(n^3),  because of for loop and nested for loop and nested loop in nested loop;
scolarMultiplication is O(n^2),  because of for loop and nested for loop;.
