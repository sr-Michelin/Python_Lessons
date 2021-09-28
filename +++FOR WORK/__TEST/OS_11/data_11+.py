import numpy as np
import matplotlib.pyplot as plt


def plotting(source8: str, source11: str):
    """

    :param source8:
    :param source11:
    :return:
    """
    # відкриття дастасету
    with open(source8) as file_8:
        row_data_8 = file_8.readlines()

    with open(source11) as file:
        row_data = file.readlines()

    # первинна обробка розбиттям за знаком переносу
    row_data_8_ = []
    for d in row_data_8:
        row_data_8_.append(d.split(sep='\n'))

    row_data_11_ = []
    for d in row_data:
        row_data_11_.append(d.split(sep='\n'))

    # вторнна обробка за міжкоординатними розділювачами
    data_8 = []
    for el in row_data_8_:
        data_8.append([float(n.replace(',', '.')) for n in el[0].split(sep='\t')])

    data_11 = []
    for el in row_data_11_:
        if '  ' in el[0]:
            data_11.append([float(n) for n in el[0].split(sep='   ')])

    # векторизація для оптимізації
    arr_8, arr_11 = np.array(data_8), np.array(data_11)

    # Нормалізація arr_8 за максимумом ординат arr_11
    norm_coif = arr_11.max(axis=0, initial=None)[1]

    # побудова кінцевих графіків
    plt.figure(figsize=(8, 6))
    plt.title(r'$(C_{2}H_{5}NH_{3})_{2}CuCl_{4}$')

    plt.plot(arr_8[:, 0], arr_8[:, 1] * norm_coif, c='k', label='Visible spectrum (8)')
    plt.plot(arr_11[:, 0], arr_11[:, 1], c='k', linestyle='dashed', label='UV spectrum (11)')

    plt.legend(loc=4)

    plt.xticks([2, 4, 6, 8, 10])
    plt.yticks([0, 2, 4, 6])

    plt.xlim([1, 10])
    plt.ylim([-2, 6])
    plt.xlabel('Photon energy (eV)', fontsize=11)
    plt.ylabel(r'Absorption coefficient $(x10^{5})$', fontsize=11)

    plt.savefig('out/L11.jpg')
    plt.show()


if __name__ == '__main__':
    plotting('data/L8.txt', 'data/L11.txt')
