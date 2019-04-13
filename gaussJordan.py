import numpy
import time


def swap(A, X, i):
    j = i
    while A[j][i] == 0 and j < len(A):
        j += 1
    if j < len(A):
        for k in range(0, len(A)):
            tmp = A[j][k]
            A[j][k] = A[i][k]
            A[i][k] = tmp
        tmp = X[i]
        X[i] = X[j]
        X[j] = tmp
        return True
    else:
        return False


def gauss_jordan(A, X):
    for i in range(0, len(A)):
        if A[i][i] == 0:
            if not swap(A, X, i):
                return X
        if A[i][i] != 1:
            divider = A[i][i]
            for j in range(0, len(A)):
                A[i][j] /= divider
            X[i] /= divider
        for j in range(0, len(A)):
            multi = -A[j][i]
            if j != i:
                for k in range(0, len(A)):
                    A[j][k] += multi * A[i][k]
                X[j] += multi * X[i]
    return X


n = 500
A = numpy.random.random((n, n))
X = numpy.random.random(n)

start = time.time()
R = gauss_jordan(A, X)
end = time.time()

start1 = time.time()
R2 = numpy.linalg.solve(A, X)
end1 = time.time()

print(end - start)
print(end1 - start1)

print(R)
print(R2)


