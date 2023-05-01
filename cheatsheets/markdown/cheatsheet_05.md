# Cheatsheet 05: NumPy and Matplotlib

## NumPy

### Installation
#### pip
```python
pip install numpy
```
#### conda
```python
conda install numpy
```

### Importing NumPy
```python
import numpy as np
```

### Creating arrays

```python
a = np.array([1, 2, 3])
b = np.zeros((3, 3))
c = np.ones((3, 3))
d = np.eye(3)
e = np.arange(0, 10, 2)
f = np.linspace(0, 1, 5)
```

### Array operations
```python
sum = a + b
difference = a - b
product = a * b
division = a / b
dot_product = np.dot(a, b)
```

### Array manipulation
```python
reshape = a.reshape((3, 1))
transpose = a.T
concatenate = np.concatenate((a, b), axis=0)
```

### Array indexing and slicing
```python
element = a[0]
slice = a[1:3]
```

### Basic statistics
```python
mean = np.mean(a)
median = np.median(a)
std_dev = np.std(a)
```

### Linear algebra:python
```python
determinant = np.linalg.det(a)
inverse = np.linalg.inv(a)
eigenvalues, eigenvectors = np.linalg.eig(a)
```

## Matplotlib

### Installation

#### pip
```python
pip install matplotlib
```

#### conda
```python
conda install matplotlib
```

### Importing Matplotlib
```python
import matplotlib.pyplot as plt
```

### Basic plotting
```python
plt.plot(x, y)
plt.show()
```

### Scatter plot
```python
plt.scatter(x, y)
plt.show()
```

### Histogram
```python
plt.hist(data, bins=10)
plt.show()
```

### Bar chart
```python
plt.bar(x, height)
plt.show()
```

### Customizing plots
```python
plt.title("Plot Title")
plt.xlabel("x-axis Label")
plt.ylabel("y-axis Label")
plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.xticks(np.arange(min_x, max_x, step))
plt.yticks(np.arange(min_y, max_y, step))
```

### Legends and labels
```python
plt.plot(x, y, label='Line Label')
plt.legend()
```

### Saving plots
```python
plt.savefig('filename.png', dpi=300)
```

Remember to combine the appropriate customizations and plot types to create the desired visualization.
