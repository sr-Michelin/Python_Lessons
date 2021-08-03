import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Створення директорії виводу
if not os.path.isdir(f'OUT'):
    os.mkdir(f'OUT')
if not os.path.isdir(f'OUT/plots'):
    os.mkdir(f'OUT/plots')

P = pd.read_excel('Task#2 statistical task.xlsx', sheet_name=1)
print(P.columns)

# Верхня межа для вибірки "yield"
N = 1.0

for y in ['f_r', 'yield', 'lost', 'reject']:
    # Побудова boxplot для знаходження колреляції між 'testSystem' та чисельними значеннями колонок
    P[P['yield'] <= N].boxplot(by='testSystem', column=y, grid=True, fontsize=10, figsize=(15, 7))
    plt.title(f'Task 2\nyield<={N}', fontsize=10)
    plt.suptitle('')

    plt.xlabel('testSystem')
    if y == 'f_r':
        plt.ylabel('finishedDate-releaseDate')
    else:
        plt.ylabel(y)

    plt.savefig(f'OUT/plots/testSystem_{y}_yield_l{N}.png')
    plt.show()
