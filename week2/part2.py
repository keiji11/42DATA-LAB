# # Create a dataset
# import numpy as np

# points = np.linspace(-5, 5)
# y1 = np.tanh(points) + .5
# y2 = np.sin(points) - .2

# # Create a canvas
# import matplotlib.pyplot as plt
# fig, axe = plt.subplots()

# # Add data to the axes
# axe.plot(points, y1, 'r-', label='y1')
# axe.plot(points, y2, 'b-', label='y2')

# # Show the figure
# plt.show()
import matplotlib.pyplot as plt

# 1. Create a matrix of random values of distribution of your choice
import numpy as np
matrix = np.random.choice(np.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
print(matrix)

# 2. Create a 1-dimensional array of 12 sequential numbers
array = np.arange(12)
# convert it to a 4x3 array
array = array.reshape(4, 3)

# 3. Write a function that creates an incremental array of dimension (1, n) with values between 0 and 1
def incremental_array(n):
    return np.linspace(0, 1, n)

arr = incremental_array(10)

# get m vectors and bind them together to create a matrix
# m = number of rows
# n = number of columns
m = 3
n = 4
matrix = np.random.rand(m, n)
fig, axe = plt.subplots()
for i in range(m):
    for j in range(n):
        matrix[i, j] = i + j
        axe.plot(matrix)

# plt.show()

# 4. Generate a 10x12 array and extract row 0-4 of columns 8-12
matrix = np.random.rand(10, 12)
row = matrix[0:5, 8:12]

