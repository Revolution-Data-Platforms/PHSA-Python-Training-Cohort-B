import numpy as np


def get_matrix(name):
    print(f"\nEnter matrix {name}:")
    matrix = []
    while True:
        row = input().split()
        if not row:
            break
        matrix.append(list(map(int, row)))
    return np.array(matrix)


print("Matrix Manipulation\n")

matrix_a = get_matrix("A")
matrix_b = get_matrix("B")

print(f"\nMatrix A:\n{matrix_a}")
print(f"\nMatrix B:\n{matrix_b}")

if matrix_a.shape != matrix_b.shape:
    print("\nError: Matrices have different dimensions.")
else:
    matrix_sum = matrix_a + matrix_b
    matrix_diff = matrix_a - matrix_b
    matrix_prod = matrix_a.dot(matrix_b)
    matrix_transpose = matrix_a.transpose()

    print(f"\nMatrix A + B:\n{matrix_sum}")
    print(f"\nMatrix A - B:\n{matrix_diff}")
    print(f"\nMatrix A * B:\n{matrix_prod}")
    print(f"\nMatrix A transpose:\n{matrix_transpose}")
