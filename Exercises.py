import numpy as np
from matplotlib.pyplot import subplots

x = np.array([[1,2,3,4,5,6]])
print(x)
x_y = x.reshape((2,3))
print(x_y)
x_y[0,0] = 10
print(x_y)
print(x)

""" Operations with tuple outcomes """

# Shape
print(x_y.shape)

# Dimension
print(x_y.ndim)

# Transpose
print(x_y.T)

""" Other operation """

# Square root
print(np.sqrt(x))
print(x**0.5)

# Square
print(x**2)


""" Probability """

# Normal distribution
r_x = np.random.normal(loc=0, scale=1, size=50)
print(r_x)

# Normal distribution in diferent location
r_y = r_x + np.random.normal(loc=100, scale=1, size=50)
print(r_y)

# Correlation matrix
print(np.corrcoef(r_x, r_y))


# Generate the same result
rng = np.random.default_rng(101)
r_x1 = rng.normal(loc=101, scale=1, size=10)
rng = np.random.default_rng(101)
r_x2 = rng.normal(loc=101, scale=1, size=10)
print(r_x1)
print(r_x2)


""" Mathematical applications """
rng = np.random.default_rng(3)
y = rng.standard_normal(10)
# Mean
print(np.mean(y), y.mean())
# Variance
print(np.var(y), y.var(), np.mean((y-y.mean())**2))



""" Example """
seed = np.random.default_rng(3)
matrix = seed.normal(loc=0, scale=1, size=30)
matrix_reshape = matrix.reshape((10,3))
print(matrix_reshape)
print(f'Mean:\n {matrix_reshape.mean(axis=0)} u')
print(f'Variance:\n {matrix_reshape.var()} u*u')
print(f'Standard deviation:\n {matrix_reshape.std()} u')


fig, ax = subplots(figsize=(8,8))
x = rng.standard_normal(100)
y = rng.standard_normal(100)
ax.scatter(x,y, 'o')