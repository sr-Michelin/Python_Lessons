import numpy as np
from numpy import sin, pi
import matplotlib.pyplot as plt

from V_t import time_t


def E_t(E: float, e: pi) -> float:
    """
    :param E: Energy
    :param e: eccentricity
    :return: t*
    """
    t = E - e * sin(E)
    return t


E_t = np.vectorize(E_t)
time_t = np.vectorize(time_t)


def visualization(vis: bool, save: bool):
    E = [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 0.9, 0.999, 1]
    X = np.linspace(0, 2 * pi, 100)
    V = X

    for e in E:
        plt.figure(figsize=(10, 8))

        Y = [E_t(x, e) for x in X]

        x, y = [time_t(v, e_=e) for v in V if v >= 0.001], [v for v in V if v >= 0.001]

        plt.title(r'Comparison of v($t^*$) and E($t^*$),' + f' {e=}', fontsize=10)

        plt.plot(X, Y, label=f'E(t), {e=}', marker="*", markersize=2.5, linewidth=1, c='black')
        plt.plot(x, y, label=f'v(t), {e=}', marker="D", markersize=2.5, linewidth=1, c='r')

        plt.xlabel(r'$t^*$')
        plt.ylabel(r'$F(t^*)$')

        plt.xticks(np.linspace(0, 2 * pi, 5), ['0', 'π/2', 'π', '3π/2', '2π'])
        plt.yticks(np.linspace(0, 2 * pi, 5), ['0', 'π/2', 'π', '3π/2', '2π'])

        plt.grid(linestyle=':')
        plt.legend(loc=4, fontsize=8)

        if vis is True:
            plt.show()
        if save is True:
            plt.savefig(f'graphs/e_t/{e}.jpg', dpi=100)


if __name__ == '__main__':
    visualization(vis=False, save=True)
