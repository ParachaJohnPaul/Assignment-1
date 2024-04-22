import numpy as np
import matplotlib.pyplot as plt

def equation1(x):
    return x**2 - 10

def equation2(x):
    return x**3 + x - 100

def equation3(x):
    return x**10 - x**8 + x**2 - 8

def equation4(x):
    return x**4 + x**3 + x**2 + x - 1

def equation5(x):
    return (x**2 + x + 10) / (2*x)

def equation6(x):
    return np.sin(x) / (3 * x)

def equation7(x):
    return x**3 + 2*x**2 - 10*x + 3

def equation8(x):
    return np.cos(x) / (5 * x)

def equation9(x):
    return (x**3) / (2*x) - 10*x

def equation10(x):
    return (x + 2) * (x + 3) * (x - 4)

x = np.linspace(-10, 10, 400)  

y1 = equation1(x)
y2 = equation2(x)
y3 = equation3(x)
y4 = equation4(x)
y5 = equation5(x)
y6 = equation6(x)
y7 = equation7(x)
y8 = equation8(x)
y9 = equation9(x)
y10 = equation10(x)

plt.plot(x, y1, color='yellow', label='x^2 - 10')
plt.plot(x, y2, color='black', label='x^3 + x - 100')
plt.plot(x, y3, color='blue', label='x^10 - x^8 + x^2 - 8')
plt.plot(x, y4, color='red', label='x^4 + x^3 + x^2 + x - 1')
plt.plot(x, y5, color='pink', label='x^2 + x + 10 / (2*x)')
plt.plot(x, y6, color='violet', label='sin(x)/3x')
plt.plot(x, y7, color='orange', label='x**3 + 2*x**2 - 10*x + 3')
plt.plot(x, y8, color='magenta', label='np.cos(x) / (5 * x)')
plt.plot(x, y9, color='darkblue', label='(x**3) / (2*x) - 10*x')
plt.plot(x, y10, color='brown', label='(x + 2) * (x + 3) * (x - 4)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Equations')
plt.legend()


plt.grid(True)
plt.show()