import numpy as np

# problem 4-5-1
a = np.linspace(12, 24, 12, endpoint=False, dtype=int)
print(a)
print()

# problem 4-5-2
b = a.reshape(2, 6)
print(b)
print()

c = a.reshape(3, 4)
print(c)
print()

d = a.reshape(6, 2)
print(d)
print()

e = a.reshape(4, 3)
print(e)
print()

f = a.reshape(12, 1)
print(f)
print()

# problem 4-5-3
b = a.reshape(-1, 1)
print(b)
print()

c = a.reshape(-1, 2)
print(c)
print()

d = a.reshape(-1, 3)
print(d)
print()

e = a.reshape(2, -1)
print(e)
print()

f = a.reshape(3, -1)
print(f)
print()

# problem 4-5-4
# Не уверен в ответе, но думаю что массив из 12 строк нельзя назвать одномерным.

# problem 4-5-5
# честно говоря не очень ясно что делать. Более конкретное ТЗ бы надо...

# problem 4-5-6
a = np.linspace(20, 0, 10, endpoint=False, dtype=int)
print(a)

# Можно сделать это задание до конца, но о-о-очень много времени потратится.