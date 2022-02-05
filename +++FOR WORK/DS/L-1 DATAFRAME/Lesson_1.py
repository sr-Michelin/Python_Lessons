import pandas as pd


P = pd.read_csv('adult.data', sep=',')
print(P.columns)

# 1. Сколько мужчин и женщин (признак sex) представлено в этом наборе данных?
print('Task 1')
print(f"Процент жінок у вибірці: {len(P[P['sex'] != 'Male']) / len(P) * 100}%")
print(f"Процент чоловіків у вибірці: {len(P[P['sex'] == 'Male']) / len(P) * 100}%\n")

# 2. Каков средний возраст (признак age) женщин?
print('Task 2')
print(f"Середній вік жінок у вибірці: {round(P[P['sex'] != 'Male'].mean().age)} років\n")

# 3. Какова доля граждан Германии (признак native-country)?
print('Task 3')
print(f"Процент громадян Німеччини у вибірці: {round(len(P[P['native-country'] == 'Germany']) / len(P) * 100, 2)} %\n")


# 4-5. Каковы средние значения и среднеквадратичные отклонения возраста тех,
# кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год?
def sts_a(condition):
    return (f"STD of age with salary {condition}: {round(P[P['salary'] == condition].std().age, 2)}",
            f"MEAN of age with salary {condition}: {round(P[P['salary'] == condition].mean().age, 2)}")


print(f"Task 4-5\n{list(map(sts_a, ['>50K', '<=50K']))}\n")

# 6. Правда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование?
# (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
print(
    f"Task 6\n{len(P[(P['salary'] == '>50K') & (P['education'] == 'Bachelors')])} "
    f"чоловік мають зарплату >50K та, як мінімум, вищу освіту\n")

# 7. Выведите статистику возраста для каждой расы (признак race) и каждого пола.
# Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Amer-Indian-Eskimo.
print('Task 7')

races, sexes = set(P['race']), set(P['sex'])

for race in races:
    for sex in sexes:
        print(f"Середнє за віком для {race, sex}: {round(P[(P['race'] == race) & (P['sex'] == sex)].mean().age)}")
        if race == "Amer-Indian-Eskimo" and sex == "Male":
            print(f"!Максимальний вік для {race, sex}: {round(P[(P['race'] == race) & (P['sex'] == sex)].max().age)}")

# 8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)?
# Женатыми считаем тех, у кого marital-status начинается с Married (Married-civ-spouse,
# Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.
print('\nTask 8')

married = [n for n in list(set(P['marital-status'])) if n.startswith('Married')]

m_with_salary = len(P.loc[(P['salary'] == '>50K') & (P['marital-status'].isin(married))])
nm_with_salary = len(P.loc[(P['salary'] == '>50K') & (~P['marital-status'].isin(married))])

print(f'{m_with_salary > nm_with_salary = } - к-сть одружених резидентів із високою ЗП(ПП) переважає к-сть неодружених')

# 9. Какое максимальное число часов человек работает в неделю (признак hours-per-week)?
# Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?
print('\nTask 9')

persons_m = len(P[P['hours-per-week'] == P['hours-per-week'].max()])
p_p_m = len(P[(P['hours-per-week'] == P['hours-per-week'].max()) & (P['salary'] == '>50K')]) / persons_m * 100
print(f'Успішних трудоголіків: {round(p_p_m, 2)}%')

# 10. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary)
# для каждой страны (native-country).
print('\nTask 10')

Salaries = set(P['salary'])
Native_countries = set(P['native-country'])

H = []
for salary in Salaries:
    for native_country in Native_countries:
        m_hours_p_w = P[(P['native-country'] == native_country) & (P['salary'] == salary)].mean()[-1]
        H.append([native_country, salary, round(m_hours_p_w, 2)])
        """print(f"Для резидента із {native_country, salary} середня тривалість тижневого навантаження: "
              f"{round(m_hours_p_w, 2)} годин")"""

print(f"N = {len(H)}, {H}")
