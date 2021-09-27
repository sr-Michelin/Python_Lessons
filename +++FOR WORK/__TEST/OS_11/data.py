import numpy as np
import matplotlib.pyplot as plt


def plotting(source: str):
    """
    :param source: path to data
    :return: [<matplotlib.lines.Line2D object]
    """

    with open(source) as file:
        row_data = file.readlines()

    row_data_1 = []
    for d in row_data:
        row_data_1.append(d.split(sep='\n'))

    data = []
    for el in row_data_1:
        if '  ' in el[0]:
            data.append([float(n) for n in el[0].split(sep='   ')])

    ind = data.index([data[i + 1] for i in range(len(data) - 1) if data[i][0] - data[i + 1][0] > 5][0])

    arr1, arr2 = np.array(data[0:ind]), np.array(data[ind:len(data)])

    plt.figure(figsize=(8, 6))

    plt.plot(arr1[:, 0], arr1[:, 1], c='k', label='(a) LNT')
    plt.plot(arr2[:, 0], arr2[:, 1], c='k', linestyle='dashed', label='(b) RT')

    plt.legend(loc=2)

    plt.xticks([2, 4, 6, 8, 10])
    plt.yticks([0, 2, 4, 6])

    plt.title(r'$(C_{2}H_{5}NH_{3})_{2}CuCl_{4}$')
    plt.xlabel('Photon energy (eV)', fontsize=11)
    plt.ylabel(r'Absorption coefficient $(x10^{5})$', fontsize=11)

    plt.savefig(f'{source[0:-5]}.jpg')
    plt.show()


if __name__ == '__main__':
    plotting(source='data/ea.CT+.txt')
    plotting(source='data/23.txt')
