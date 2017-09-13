import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from pylab import imshow,show
#Mandelbrot Set
#Note to self: want to do itereation for each value of c on the grid, if result of iteration is less than 2, its in set

N = 100
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)
z = 0
for i in range(1,4):
    c = complex(x[i], y[i])
    while True:
        z = z**2 + c
        if np.absolute(z) > 2:
            break
print z
