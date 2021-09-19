import numpy as np
import pandas as pd
import time

P = pd.read_csv('adult.data', sep=',')

# 1
print(len(P[P['sex'] != 'Male']) / len(P) * 100, '%')

# 2
print(np.mean(P[P['sex'] != 'Male']['age']), 'років')
print(P[P['sex'] != 'Male'].age.mean(), 'років')

# 3
print(len(P[(P['native-country'] == 'Germany') & (P['salary'] == '>50K')]) /
      len(P[P['native-country'] == 'Germany']) * 100, '%')

print(P.pivot_table(['age', 'capital-loss'], ['race'], aggfunc='mean'))
