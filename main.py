import matplotlib.pyplot as plt
import numpy as np

# Define the mathematical functions
def f(x):
    return x**2

def g(x):
    return np.sin(x)

# Set up the plot
x = np.linspace(-10, 10, 100) # x values to plot
plt.plot(x, f(x), label='f(x) = x^2')
plt.plot(x, g(x), label='g(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphing Calculator')
plt.legend()

# Display the plot
plt.show()
