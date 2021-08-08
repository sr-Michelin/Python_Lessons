import numpy as np
import pandas as pd
import datetime

# Налаштування стандартного виводу таьлиць:
pd.set_option('display.max_columns', 7)  # кількість колонок без ...
pd.set_option('display.max_rows', 7)  # кількість стовчиків без ...
pd.set_option('precision', 2)  # кількість знаків після коми

# Зчитування із csv - формату
Frame = pd.read_csv('CSV1.csv', header=0, sep=';')
print(Frame, '\n')

print('Новий рядок')
Frame = Frame.append({'Name': 'Max', 'Sname': 'Varynyca'}, ignore_index=True)  # Новий рядок
Frame = Frame.append({'Name': 'Yaryna', 'Sname': 'Ostapchuk'}, ignore_index=True)
print(Frame, '\n')

print('Новий стовпець')
Frame['Birth'] = ['04.11.1998'] + ['01.01.1999'] * 3 + ['14.05.1999']  # Новий стовпець
Frame['Sex'] = [None] * 4 + ['Female']
Frame['course'] = [6] + [4] + [6] + [4] + [6]
print(Frame, '\n')

'---------------new------------------'
print('\tЗаповнення пустих значень {None} новими {Male}')
Frame.fillna('Male', inplace=True)  # Заповнення пустих значень {None} новими {'Male'}
print(Frame, '\n')

print('Зміна типу подачі дати')
Frame.Birth = Frame.Birth.apply(pd.to_datetime)  # Зміна типу подачі дати
print(Frame, '\n')

Frame.to_csv('CSV_new.csv', header=True, index=None, sep=';')

print('Тип обєкта')
print(Frame.dtypes, '\n')  # Тип обєкта

print('Повна інформація')
print(Frame.info(), '\n')  # Повна інформація

print('Вивід стовця як масива')
print(Frame.Sex, '\n')  # Вивід стовця як масива

print('Вивід стовця як таблиці')
print(Frame[['Sex']].head(2), '\n')  # Вивід стовця як таблиці - "Series"
print(Frame['Sex'].head(2), '\n')  # Вивід стовця як таблиці - "Frame"

print('Вивід перших двох рядків т-ці')
print(Frame.head(2), '\n')  # Вивід перших двох рядків т-ці
# або print(Frame[:2])
print('Вивід двох останіх рядків т -ці')
print(Frame[-2:], '\n')  # Вивід двох останіх рядків т -ці

print('Розширеий вивід бажаних стовців і рядків (за назвами )')
print(Frame.loc[[0, 2], ['Name', 'Sex']], '\n')  # Розширеий вивід бажаних стовців і рядків (за назвами)
print('Розширеий вивід бажаних стовців і рядків (за номерами)')
print(Frame.iloc[[0, 2], [0, 3]], '\n')  # Розширеий вивід бажаних стовців і рядків (за номерами)

print('Сортування по даті через {import datetime}')
print(Frame[Frame.Birth >= datetime.datetime(1998, 4, 11)], '\n')  # Сортування по даті через {import datetime}

print('Обєднання умов виведення т-ці')
print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) & (Frame.Sex == 'Male')],
      '\n')  # 'i' - oбєднання умов виведення т-ці

print('Або')
print(Frame[(Frame.Birth < datetime.datetime(1998, 4, 11)) | (Frame.Sex == 'Female')],
      '\n')

print('Опис таблиці (статка)')
print(Frame.describe(), '\n')  # min(), max(), std(), mean() та інші методи

print('Групування таблиці за певними ознаками:', [i for i, j in Frame.groupby(['Name', 'Sex'])])

# використування групування для подальшої статки через агрегацію відповідних ф-цій
print(Frame.groupby('Sex')[['course']].agg(np.mean), '\n')  # ".agg(np.mean)" = ".mean()"

print('Звідні таблиці "crosstab":')
print(pd.crosstab(Frame['Name'], Frame['Sex']), '\n')  # позначення через "0" та "1" бінарних параметрів

print('Створення колонки по признаку:')
Frame['is_mag'] = (Frame['course'] >= 5).astype('int')  # ".astype('int')" - перевід True, False у 1,0
print(Frame, '\n')

print('Застосування ф-цій до значень таблиці:')
print(Frame['Sex'].apply(lambda g: 0 if g == 'Male' else 1))  # через apply(lambda)
print(Frame['is_mag'].map({0: 'False', 1: 'True'}), '\n')  # через map(dict)

print('Розбір колонки за унікальними значеннями:')
print(Frame['Sex'].value_counts(normalize=0), '\n')

print('Сортування таблиці за певним параметром:')
print(Frame.sort_values(by=['Name', 'course'], ascending=True), '\n')

# print('Звідні таблиці, метод "privot_table":')
# print(Frame.pivot_table(['0', '1', '2'], ['code'], aggfunc='mean'))

print(f"Вектор унікальних значень 'Name': {Frame['Name'].unique()}\n")

Frame['is_mag'].dropna()  # Видалення значень 'nan' із колонки 'is_mag'
