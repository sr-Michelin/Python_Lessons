import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('GG4.dat', sep='\s+', header=None)
data = pd.DataFrame(data)

x = data[0]
y = data[1]

'''plt.title('GG4.dat')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(which = 'major')
plt.plot(x, y, linewidth=0.5, color='black')
plt.show()'''

fig, ax = plt.subplots()
plt.title('GG4.dat')
plt.xlabel('x')
plt.ylabel('f(x)')
ax.plot(x, y, linewidth=0.5, color='black')
ax.grid(color='black', linewidth=0.5, linestyle='--')

plt.savefig('GG4')
plt.show()