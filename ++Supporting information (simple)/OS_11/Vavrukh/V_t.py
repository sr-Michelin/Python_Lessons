import numpy as np
from numpy import arctan as atan, tan, sqrt, sin, cos, pi
from matplotlib import pyplot as plt

plt.figure(figsize=(10, 8))

V = np.linspace(0, 2 * pi, 100)
E = [0, 0.25, 0.5, 0.75, 0.9, 0.999]
Markers = ["^", "s", "D", "*", "v", "x"]


def time_t(v, e_) -> float:
    """
    :param v: істинна аномалія
    :param e_: екстренциситет
    :return: t* - зведений час (τ=0)
    """
    t = 2. * atan(sqrt((1. - e_) / (1. + e_)) * tan(v / 2.)) - e_ * sqrt(1. - e_ ** 2.) * sin(v) / (
            1. + e_ * cos(v))
    if t > 0:
        return t
    else:
        return t + 2 * pi


def visualisation(save: bool, vis: bool):
    """
    :param vis: прапорець, що вказує на подальшу візуалізацію в окремому вікні pyplot
    :param save: прапорець, що вказує на подальше зберігання графіка у векторному форматі
    :return: pdf
    """
    for e, m in zip(E, Markers):
        x, y = [time_t(v, e_=e) for v in V if v >= 0.001], [v for v in V if v >= 0.001]
        plt.plot(x, y, label=f'{e=}', marker=m, markersize=2.5, linewidth=1)

    plt.title(r'Залежність істинної аномалії v від часу $t^*$', fontsize=10)

    plt.xlabel(r'$t^*$')
    plt.ylabel(r'$v(t^*)$')

    plt.xticks(np.linspace(0, 2 * pi, 5), ['0', 'π/2', 'π', '3π/2', '2π'])
    plt.yticks(np.linspace(0, 2 * pi, 5), ['0', 'π/2', 'π', '3π/2', '2π'])

    plt.grid(linestyle=':')
    plt.legend(loc=4, fontsize=8)

    if save is True:
        plt.savefig("graphs/v_t/☺.pdf", format='pdf', dpi=2000)
    if vis is True:
        plt.show()


if __name__ == '__main__':
    visualisation(save=True, vis=False)
