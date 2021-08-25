# problem 1-1
import numpy as np

a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

print("Initial matrix as:\n" + str(a) + "\n")

mean_a = np.mean(a, axis=0)

print("Mean a is: " + str(mean_a))

# problem 1-2
a_centered = np.subtract(a, mean_a)
print("\nCentered matrix:\n" + str(a_centered) + "\n")

# problem 1-3
a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])
print("\nMatrix a centred sp :" + str(a_centered_sp) + "\n")
print("\nMatrix a centred sp divided by N-1 :" + str(a_centered_sp/4) + "\n")

# problem 1-4
t_a = a.transpose()
print("\nMatrix a covariation is: \n" + str(np.cov(t_a)))
print("So. Answer is correct.")
