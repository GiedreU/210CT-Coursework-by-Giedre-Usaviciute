MATRIX_ADDITION(matrix1, matrix2, n, m)
    matrixAdded <- [n][m] // create matrix size of n, m
    FOR i<-0 TO length(n)
        FOR j<-0 TO length(m)
            matrixAdded[i][j] <- matrix1[i][j]+matrix2[i][j]
    RETURN matrixAdded

MATRIX_SUB(matrix1, matrix2, n, m)
    matrixSub <- [n][m] // create matrix size of n, m
    FOR i<-0 TO length(n)
        FOR j<-0 TO length(m)
            matrixSub[i][j] <- matrix1[i][j]-matrix2[i][j]
    RETURN matrixSub

MATRIX_MULTI(matrix1,matrix2,n,m)
    multiMatrix <- [n][m] // create matrix size of n, m
    FOR i<-0 TO length(n) 
        FOR j<-0 TO length(m)
            sum = 0
            FOR k<-0 TO length(m)
                sum <- sum + matrix1[i][k]*matrix[k][j]
            multiMatrix[i][j] <- sum
    RETURN multiMatrix
