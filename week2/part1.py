import numpy as np

# Create an array of ten zeros
a = np.zeros(10)
print(a)
print("")
# Create an array of ten ones
b = np.ones(10)
print(b)
print("")
# Create an array of integers from 10 to 50
c = np.arange(10, 51)
print(c)
print("")
# Create an array of all the even integers from 10 to 50
d = np.arange(10, 51, 2)
print(d)
print("")
# Create a 3x3 identity matrix
e = np.eye(3)
print(e)
print("")
# Generate a random number between 0 and 1
f = np.random.random(1)
print(f)
print("")
# Create the following matrix:
# array([0. , 0.11111111, 0.22222222, 0.33333333, 0.44444444, 0.55555555,
# 0.66666667, 0.77777778, 0.88888889, 1. ])
g = np.linspace(0, 1, 10)
print(g)
print("")


