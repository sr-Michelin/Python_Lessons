import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Створення директорії виводу
if not os.path.isdir(f'plots'):
    os.mkdir(f'plots')
if not os.path.isdir(f'plots/low_yield'):
    os.mkdir(f'plots/low_yield')
if not os.path.isdir(f'plots/full_yield'):
    os.mkdir(f'plots/full_yield')

P = pd.read_excel('Task#2 statistical task.xlsx', sheet_name=1)
print(P.columns)

# Верхня межа для вибірки "yield"
N = [.9, 1.0]

for n in N:
    for y in ['f_r', 'yield', 'lost', 'reject']:
        # Побудова boxplot для знаходження колреляції між 'testSystem' та чисельними значеннями колонок
        P[P['yield'] <= n].boxplot(by='testSystem', column=y, grid=True, fontsize=10, figsize=(15, 7))
        plt.suptitle('')

        plt.xlabel('testSystem')
        if y == 'f_r':
            plt.title(f'Task 2: finishedDate-releaseDate\nyield<={n}', fontsize=10)
            plt.ylabel('finishedDate-releaseDate')
        else:
            plt.ylabel(y)
            plt.title(f'Task 2: {y}\nyield<={n}', fontsize=10)

        if n == N[0]:
            plt.savefig(f'plots/low_yield/testSystem_{y}_yield_l{n}.png')
        else:
            plt.savefig(f'plots/full_yield/testSystem_{y}_yield_l{n}.png')
        # plt.show()




