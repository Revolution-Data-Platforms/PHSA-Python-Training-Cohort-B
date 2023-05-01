import numpy as np

# Exercise 1
a = np.arange(1, 21)
print(a)
print(a.shape)
print(a.size)
print(a.dtype)
print()

# Exercise 2
random_array = np.random.randint(1, 101, (5, 5))
print(random_array)
print()

# Exercise 3
identity_matrix = np.eye(4)
print(identity_matrix)
print()

# Exercise 4
A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))
print("A:", A)
print("B:", B)
print("A + B:", A + B)
print("A - B:", A - B)
print("A * B:", A * B)
print()

# Exercise 5
linspace_array = np.linspace(0, 10, 20)
print(linspace_array)
print()

# Exercise 6
random_array = np.random.randint(1, 51, (6, 6))
print(random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard deviation:", np.std(random_array))
print()

# Exercise 7
array1D = np.arange(1, 17)
array2D = array1D.reshape(4, 4)
print(array2D)
print()

# Exercise 8
array5x5 = np.random.randint(1, 26, (5, 5))
print(array5x5)
subarray3x3 = array5x5[1:4, 1:4]
print(subarray3x3)
print()

# Exercise 9
array = np.random.randint(1, 20, (5, 5))
print("Original array:", array)
array[array > 10] = 0
print("Modified array:", array)
print()

# Exercise 10
array10x10 = np.random.randint(1, 101, (10, 10))
normalized_array = (array10x10 - np.mean(array10x10)) / np.std(array10x10)
print(normalized_array)
print()

# Exercise 11
A = np.random.randint(1, 21, 10)
B = np.random.randint(1, 21, 10)
euclidean_distance = np.linalg.norm(A - B)
print("A:", A)
print("B:", B)
print("Euclidean distance:", euclidean_distance)
print()

# Exercise 12
array = np.random.randint(1, 100, 20)
sorted_indices = np.argsort(array)[-5:]
top5_values = array[sorted_indices]
print("Array:", array)
print("Top 5 values:", top5_values)
print("Indices:", sorted_indices)
print()

# Exercise 13
array3x3 = np.random.randint(1, 10, (3, 3))
determinant = np.linalg.det(array3x3)
eigenvalues = np.linalg.eigvals(array3x3)
print("Array:", array3x3)
print("Determinant:", determinant)
print("Eigenvalues:", eigenvalues)
print()

# Exercise 14
array5x5 = np.random.randint(1, 26, (5, 5))
print("Original array:", array5x5)
sorted_array = np.sort(array5x5, axis=1)
print("Sorted array:", sorted_array)
print()

# Exercise 15
A = np.random.randint(1, 6, (2, 2))
B = np.random.randint(1, 6, (2, 2))

print("A:")
print(A)
print("B:")
print(B)

matrix_product = np.matmul(A, B)
elementwise_product = A * B

print("Matrix product:")
print(matrix_product)

print("Element-wise product:")
print(elementwise_product)
