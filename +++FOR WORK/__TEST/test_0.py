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
    """Даний loop перебирає значення меж "yield" для побудови boxplot і виводу статистик"""
    # ------------------------------------------------------------
    # Графічне відображення кореляції між 'finishedDate-releaseDate' та "yield"
    # (на повній картині можна замітити проміжок "yield"[0.9, 0.95], у якому виміри проводилися за умови
    # 'finishedDate-releaseDate <0 (-20, 0). "Розпорошення" значень даного типу (у ліву сторону) слабо спостерігається у
    # вибірці із більшим "yield". Це наштовхує на те, що зменшення "yield" може залежати від finishedDate-releaseDate')
    P[P['yield'] <= n].plot.scatter(x='f_r', y='yield', color='black', alpha=0.6, linewidth=.2, figsize=(15, 7))
    plt.title(f'Task 2: finishedDate-releaseDate\nyield<={n}', fontsize=10)
    plt.grid()
    plt.xlabel('finishedDate-releaseDate')
    plt.ylabel('yield')

    if n == N[0]:
        plt.savefig(f'plots/low_yield/f_r_yield_l{n}.png')
    else:
        plt.savefig(f'plots/full_yield/f_r_yield_l{n}.png')
    # ------------------------------------------------------------
    # Серед усіх систем, на яких проводилося тестування, найбільш підозрілою є "System5"
    # (кількість викидів у негативну сторону "finishedDate-releaseDate",
    # загублених мікросхем - "lost" = "input" - "output" - "reject",
    # найнижчий вихід "yield")

    for y in ['yield', 'lost', 'reject', 'f_r']:
        """Перебір усіх можливих числових колонок, значення яких є інформативними (на мою думку, звісно)"""
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
            # у випадку низького виходу виводиться тільки "System5"
            plt.savefig(f'plots/low_yield/testSystem_{y}_yield_l{n}.png')
        else:
            plt.savefig(f'plots/full_yield/testSystem_{y}_yield_l{n}.png')
        # plt.show() # сховано для більш корректного виводу (у директорії за "yield")

    print(f'\nКореляції Пірсона для межі "yield" <= {n}:')
    print(f'P_corr(yield, finishedDate-releaseDate): '
          f'{np.corrcoef(P[P["yield"] <= n]["yield"], P[P["yield"] <= n]["f_r"])[0][1]} - ймовірна')
    print(f'P_corr(yield, lost): {np.corrcoef(P[P["yield"] <= n]["yield"], P[P["yield"] <= n]["lost"])[0][1]}')
    print(f'P_corr(reject, lost): {np.corrcoef(P[P["yield"] <= n]["reject"], P[P["yield"] <= n]["lost"])[0][1]}')

print(f'\nСтатистики тестових с-м для значення "yield" ("yield" <= {N[1]}):')
pp_yield = [i for i, j in P[P['yield'] <= N[1]].groupby(['testSystem', 'yield'])]
for t in range(len(testSystem_)):
    d_pp = {testSystem_[t]: [j for i, j in pp_yield if i == testSystem_[t]]}
    print(
        f'{testSystem_[t]}: min = {round(min(list(d_pp.values())[0]), 3)}, '
        f'max = {round(max(list(d_pp.values())[0]), 3)}, '
        f'mean = {round(float(np.mean(list(d_pp.values())[0])), 3)}, '
        f'std = {round(float(np.std(list(d_pp.values())[0])), 3)}, '
        f'q_25 = {round(np.quantile(list(d_pp.values())[0], .25), 3)}, '
        f'q_75 = {round(np.quantile(list(d_pp.values())[0], .75), 3)}')

# Вивід статистик для тестових станцій
print(f'\nСтатистики тестових с-м для значення "finishedDate-releaseDate" ("yield" <= {N[1]}):')
pp_f_r = [i for i, j in P[P['yield'] <= N[1]].groupby(['testSystem', 'f_r'])]
for t in range(len(testSystem_)):
    d_pp = {testSystem_[t]: [j for i, j in pp_f_r if i == testSystem_[t]]}
    print(
        f'{testSystem_[t]}: min = {round(min(list(d_pp.values())[0]), 3)}, '
        f'max = {round(max(list(d_pp.values())[0]), 3)}, '
        f'mean = {round(float(np.mean(list(d_pp.values())[0])), 3)}, '
        f'std = {round(float(np.std(list(d_pp.values())[0])), 3)}, '
        f'q_25 = {round(np.quantile(list(d_pp.values())[0], .25), 3)}, '
        f'q_75 = {round(np.quantile(list(d_pp.values())[0], .75), 3)}')

input('\nPress enter to exit...')
