import numpy as np
import matplotlib.pyplot as plt


def plotting(source: str):
    """
    :param source: path to data
    :return: [<matplotlib.lines.Line2D object]
    """

    # відкриття дастасету
    with open(source) as file:
        row_data = file.readlines()

    # первинна обробка розбиттям за знаком переносу
    row_data_1 = []
    for d in row_data:
        row_data_1.append(d.split(sep='\n'))

    # вторнна обробка, яка відсікає некоординатні наді (використав пробіл між [x, y] як критерій зберреження)
    data = []
    for el in row_data_1:
        if '  ' in el[0]:
            data.append([float(n) for n in el[0].split(sep='   ')])

    # опрацювання виключення для випадку із однією кривою із датасету (визначення к-сті кривих за різницею абсцис)
    try:
        ind = data.index([data[i + 1] for i in range(len(data) - 1) if data[i][0] - data[i + 1][0] > 5][0])
        style = 'dashed'
    except IndexError:
        print('\nДані складаються лиш з одної кривої!\nПропускаю один вектор...')
        ind, style = 1, '-'

    # векторизація для оптимізації
    arr1, arr2 = np.array(data[0:ind]), np.array(data[ind:len(data)])

    # побудова кінцевих графіків
    plt.figure(figsize=(8, 6))
    plt.title(r'$(C_{2}H_{5}NH_{3})_{2}CuCl_{4}$')

    plt.plot(arr1[:, 0], arr1[:, 1], c='k', label='(a) LNT')
    plt.plot(arr2[:, 0], arr2[:, 1], c='k', linestyle=style, label='(b) RT')

    plt.legend(loc=2)

    plt.xticks([2, 4, 6, 8, 10])
    plt.yticks([0, 2, 4, 6])

    plt.xlim([2, 10])
    plt.ylim([-2, 6])

    plt.xlabel('Photon energy (eV)', fontsize=11)
    plt.ylabel(r'Absorption coefficient $(x10^{5})$', fontsize=11)

    plt.savefig(f'{source[0:-4]}.jpg')
    plt.show()


if __name__ == '__main__':
    plotting(source='data/row_DATA.txt')
    plotting(source='data/row_DATA_1.txt')
