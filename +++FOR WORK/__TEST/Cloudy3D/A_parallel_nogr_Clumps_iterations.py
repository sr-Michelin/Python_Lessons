from os import makedirs, path

"""age = input('Введіть вік галактики: ')
min_sector = input('Введіть початковий сектор: ')
max_sector = input('Введіть кінцевий сектор: ')

n = input('Введіть кількість процесів: ')"""
# Iteration = input('Введіть ітерацію: ')

min_sector = 1
max_sector = 5
age = 140
n = 4
Iteration = 2

is_sector = min_sector

path_1 = f".\\result\\ngc\\nograins_parallel_clumps_i{Iteration}"
path_2 = f".\\result\\ngc\\nograins_parallel_clumps_i{Iteration}\\{age}"

if not path.exists(path_1):
    makedirs(path_1, mode=0o777, exist_ok=False)

if not path.exists(path_2):
    makedirs(path_2, mode=0o777, exist_ok=False)

while is_sector <= max_sector:
    n_Processes = 0
    i_process = 0
    r_Sector = is_sector

    while i_process < n:

        if r_Sector > max_sector:
            break

        print(f"Start process {i_process} ({r_Sector})\n")

        n_Processes += n_Processes
        print(f"Entering $pid for {r_Sector} ({n_Processes})\n")

        try:
            with open(f'commands\\commands{age}.{r_Sector}.i{Iteration}.ini', 'r') as data:
                for d in data:
                    print(data)
                    print(d)
        except FileNotFoundError as err:
            print(err)
            break

        theta = 3.14 * (r_Sector - 0.05) / (2 * max_sector)

        r_Sector = is_sector + i_process
        i_process = i_process + 1

    print(f"Finished iter {n_Processes}\n")

    is_sector += n_Processes
