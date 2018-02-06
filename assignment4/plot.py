import numpy as np
import matplotlib.pyplot as plt
from integrator import integrate
from test_integrator import integral_of_exponential_function

n = 100
x = np.linspace(0, n, n)

lst = []
for i in range(1, n+1):
    lst.append(integrate(integral_of_exponential_function, 0, 1, i))

for i in range (len(lst)):
    print(lst[i])

myArray = np.asarray(lst)

plt.plot(x, myArray, 'o', label='Test function')
#plt.bar(x[:-1], lst[1:], (0-1/n), color="blue", fill=False, align="edge")
plt.axhline(y=1/3, color = 'r', linestyle='-', label='Expected value')
plt.xlabel('N')
plt.ylabel('Value')

plt.legend()
plt.savefig('quadratic_error.png')
plt.show()
