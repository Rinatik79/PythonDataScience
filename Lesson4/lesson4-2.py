import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 51)
f = np.cos(t)

plt.plot(t, f, 'g')
plt.title('График f(t)')
plt.xlabel('Значения t')
plt.ylabel('Значения f')
plt.axis([0.5, 9.5, -2.5, 2.5])

plt.show()
