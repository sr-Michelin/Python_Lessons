import numpy as np
import matplotlib.pyplot as plt

n = 100


def func(x):
    return x ** 5


ax = np.linspace(-1, 1, 10)
ay = [func(x) for x in ax]
ay_ = [func(x) - np.random.random(n) for x in ax]
ay__ = [func(x) + np.random.random(n) for x in ax]

plt.figure(figsize=(5, 4))

plt.xticks(np.linspace(-1, 1, 5))

plt.scatter(ax, ay, c='k', alpha=.9)
plt.plot(ax, ay_, c='r', alpha=.5)
plt.plot(ax, ay__, c='b', alpha=.5)
plt.savefig('out.jpg')
plt.show()
