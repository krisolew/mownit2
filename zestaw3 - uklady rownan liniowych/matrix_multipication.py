import numpy as np


def multiply_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        print("Wrong dimensions of matrices")

    first_dimension = A.shape[0]
    second_dimension = B.shape[1]
    num_of_elements = A.shape[1]
    C = np.zeros((first_dimension, second_dimension))

    for i in range(0, first_dimension):
        for j in range(0, second_dimension):
            sum = 0
            for k in range(0, num_of_elements):
                sum += A[i][k] * B[k][j]
            C[i][j] = sum

    return C


A = np.array([[1, 2, 3], [3, 2, 1]])
B = np.array([[2, 1], [3, 1], [1, 2]])

C = multiply_matrices(A, B)
print(C)

