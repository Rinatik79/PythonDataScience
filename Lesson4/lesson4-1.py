import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7.]

# %matplotlib inline - doesn't work in Pycharm
plt.plot(x, y)
plt.show()

plt.scatter(x, y)
plt.show()
