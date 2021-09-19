import pandas as pd

# ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race',
# 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
P = pd.read_csv('adult.data', sep=',')

print(P.pivot_table(['age', 'hours-per-week', 'capital-loss', 'salary'], ['education'], aggfunc='max'))
