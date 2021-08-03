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
testSystem_ = sorted(list(set(P['testSystem'])))
# print(P.columns)

# Верхня межа для вибірки "yield"
N = [0.9, 1.0]

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
        plt.show()

    print(f'\nКореляції Пірсона для межі "yield" <= {n}:')
    print(f'P_corr(yield, f_r): {np.corrcoef(P[P["yield"] <= n]["yield"], P[P["yield"] <= n]["f_r"])[0][1]} '
          f'- ймовірна')
    print(f'P_corr(yield, lost): {np.corrcoef(P[P["yield"] <= n]["yield"], P[P["yield"] <= n]["lost"])[0][1]}')
    print(f'P_corr(yield, reject): {np.corrcoef(P[P["yield"] <= n]["yield"], P[P["yield"] <= n]["reject"])[0][1]} '
          f'- надто очевидна')
    print(f'P_corr(reject, lost): {np.corrcoef(P[P["yield"] <= n]["reject"], P[P["yield"] <= n]["lost"])[0][1]}')

print(f'\nСтатистики тестових с-м для значення "yield" <= {N[1]}')
pp_yield = [i for i, j in P[P['yield'] <= N[1]].groupby(['testSystem', 'yield'])]
yield_q_75 = []
for t in range(len(testSystem_)):
    d_pp = {testSystem_[t]: [j for i, j in pp_yield if i == testSystem_[t]]}
    yield_q_75.append(np.quantile(list(d_pp.values())[0], q=.75))
    print(
        f'{testSystem_[t]}: min = {round(min(list(d_pp.values())[0]), 3)}, '
        f'max = {round(max(list(d_pp.values())[0]), 3)}, '
        f'mean = {round(float(np.mean(list(d_pp.values())[0])), 3)}, '
        f'std = {round(float(np.std(list(d_pp.values())[0])), 3)}, '
        f'q_25 = {round(np.quantile(list(d_pp.values())[0], .25), 3)}, '
        f'q_75 = {round(np.quantile(list(d_pp.values())[0], .75), 3)}')
