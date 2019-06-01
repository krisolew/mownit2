import numpy as np


def gausse_elimination(n, A, B):
    xmult = 0
    sum = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            xmult = A[j][i] / A[i][i]

            for k in range(i+1, n):
                A[j][k] = A[j][k] - (xmult)*A[i][k]

            B[j] = B[j] - (xmult)*B[i]

    X = [0, 0, 0]

    X[n-1] = B[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = B[i]
        for j in range(i+1, n):
            sum = sum - A[i][j]*X[j]
        X[i] = sum/A[i][i]
    return X


def gausse_elimination_with_pivoting(n, A, B, T):
    xmult = 0
    rmax = 0
    smax = 0
    r = 0
    S = np.zeros((1, n))
    j = 0

    for i in range(0, n):
        T[i] = i
        smax = 0
        for j in range(0, n):
            smax = max(smax, abs(A[i][j]))
        S[0][i] = smax

    for k in range(0, n-1):
        rmax = 0
        for i in range(k, n):
            r = abs(A[T[i]][k]/S[0][T[i]])
            if r > rmax:
                rmax = r
                j = i
        tmp = T[j]
        T[j] = T[k]
        T[k] = tmp

        for i in range(k+1, n):
            xmult = A[T[i]][k] / A[T[k]][k]
            #A[T[i]][k] = xmult
            for j in range(k+1, n):
                A[T[i]][j] = A[T[i]][j] - xmult*A[T[k]][j]

    for k in range(0, n-1):
        for i in range(k+1, n):
            B[T[i]] = B[T[i]] - (A[T[i][k]] * B[T[k]])

    X = [0, 0, 0]

    X[n - 1] = B[T[n-1]] / A[T[n-1]][n - 1]
    for i in range(n - 2, -1, -1):
        sum = B[T[i]]
        for j in range(i + 1, n):
            sum = sum - A[T[i]][j] * X[j]
        X[i] = sum / A[T[i]][i]
    return X


n = 3
A = [[2, 3, 4], [1, 2, 3], [5, 7, 7]]
A1 = [[2, 3, 4], [1, 2, 3], [5, 7, 7]]
B = [8, 9, 10]
B1 = [8, 9, 10]

L = [0, 1, 2]

X = gausse_elimination(n, A, B)
print(X)
X1 = gausse_elimination_with_pivoting(n, A1, B1, L)
print(X1)



