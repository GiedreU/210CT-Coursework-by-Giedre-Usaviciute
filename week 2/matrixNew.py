def createMatrix(n,k):
    matrix = [[k for x in range(n)]for y in range(n)]
    return matrix

def matrixAddition(matrix1, matrix2, n):
    addMatrix = createMatrix(n,0)
    for i in range(n):
        for j in range(n):
            addMatrix[i][j] = matrix1[i][j]+matrix2[i][j]
    return addMatrix

def matrixSub(matrix1, matrix2, n):
    matrixSub = createMatrix(n,0)
    for i in range(n):
        for j in range(n):
            matrixSub[i][j] = matrix1[i][j]-matrix2[i][j]
    return matrixSub

def matrixMulti(matrix1, matrix2, n):
    matrixMulti = createMatrix(n,0)
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp = temp + matrix1[i][k]*matrix2[k][j]
            matrixMulti[i][j] = temp
    return matrixMulti
n=5  
matrixB = createMatrix(n,2)
matrixC = createMatrix(n,3)

matrixA = matrixSub(matrixMulti(matrixB,matrixC,n),matrixAddition(matrixAddition(matrixB,matrixC,n),matrixAddition(matrixB,matrixC,n),n),n)
print(matrixA)

