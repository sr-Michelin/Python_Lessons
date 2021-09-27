import numpy as np
import matplotlib.pyplot as plt

with open('ea.CT+.txt') as file:
    row_data = file.readlines()

row_data_1 = []
for d in row_data:
    row_data_1.append(d.split(sep='\n')[0].split(sep='   '))

data = []
for i in row_data_1:
    data.append([float(i[0]), float(i[1])])

arr = np.array(data)

plt.figure(figsize=(7, 5))
plt.scatter(arr[:, 0], arr[:, 1], s=20, edgecolors='black', c='w')

plt.xticks([2, 4, 6, 8, 10])
plt.yticks([0, 2, 4, 6])

plt.title(r'$(C_{2}H_{5}NH_{3})_{2}CuCl_{4}$')
plt.xlabel('Photon energy (eV)')
plt.ylabel(r'Absorption coefficient $(x10^{5})$')
plt.show()
