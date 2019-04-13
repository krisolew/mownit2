def gausse_elimination(n, A, B, X):
    xmult = 0
    sum = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            xmult = A[j][i] / A[i][i]

            for k in range(i+1, n):
                A[j][k] = A[j][k] - (xmult)*A[i][k]

            B[j] = B[j] - (xmult)*B[i]

    X[n-1] = B[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = B[i]
        for j in range(i+1, n):
            sum = sum - A[i][j]*X[j]
        X[i] = sum/A[i][i]
    return X


def gausse_elimination_with_pivoting(n, A, B):
    xmult = 0
    rmax = 0
    smax = 0
    r = 0
    S = [0,0,0]
    j = 0

    for i in range(0, n):
        B[i] = i
        smax = 0
        for j in range(0,n):
            smax = max(smax,abs(A[i][j]))
        S[i] = smax

    for k in range(0, n-1):
        rmax = 0
        for i in range(k, n):
            r = abs(A[B[i]][k]/S[B[i]])
            if r > rmax:
                rmax = r
                j = i
        tmp = B[j]
        B[j] = B[k]
        B[k] = tmp

        for i in range(k+1, n):
            xmult = A[B[i]][k]/A[B[k]][k]
            A[B[i]][k] = xmult
            for j in range(k+1, n):
                A[B[i]][j] = A[B[i]][j] - xmult*A[B[k]][j]


n = 3
A = [[2, 3, 4], [1, 2, 3], [5, 7, 7]]
A1 = [[2, 3, 4], [1, 2, 3], [5, 7, 7]]
B = [8, 9, 10]
X = [0, 0, 0]

L = [0, 1, 2]

X = gausse_elimination(n, A, B, X)
print(X)
gausse_elimination_with_pivoting(n, A1, L)
print(A1)
print("")
print(L)



