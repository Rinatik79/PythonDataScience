import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 51)
y1 = x ** 2
y2 = 2 * x + .5
y3 = -3 * x - 1.5
y4 = np.sin(x)

fig, ax = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(8, 6)

ax[0][0].plot(x, y1)
ax[0][0].set_title('График y1')
ax[0][0].set_xlim([-5, 5])

ax[0][1].plot(x, y2)
ax[0][1].set_title('График y2')

ax[1][0].plot(x, y3)
ax[1][0].set_title('График y3')

ax[1][1].plot(x, y4)
ax[1][1].set_title('График y4')

fig.subplots_adjust(wspace=0.3, hspace=0.3)
plt.show()
