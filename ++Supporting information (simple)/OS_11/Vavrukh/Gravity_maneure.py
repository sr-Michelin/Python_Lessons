import numpy as np
from numpy import cos, pi, sqrt
from matplotlib import pyplot as plt

plt.figure(figsize=(10, 8))

V = {'Mercury': 47.87,
     'Venus': 35.02,
     'Earth': 29.78,
     'Moon': 1.02,
     'Mars': 24.13,
     'Jupyter': 13.07,
     'Saturn': 9.69,
     'Uranus': 6.81,
     'Neptune': 5.43,
     'Pluto': 4.67}

alpha = 40 * pi / 180  # starting angle in gravitational maneure

db = 2 * pi  # step for result angle
betas = np.linspace(alpha - db, alpha + db, 100)  # result angle in gravitational maneure


def gravity(beta: float, v: float, const=1.5):
    """
    :param const: multiplier
    :param beta: result angle in gravitational maneure
    :param v: orbital velocity of planets
    :return: vf - ending velocity
    """
    vi = const * v
    vf = sqrt(vi ** 2 + 2 * v * (v * (1 - cos(beta)) + vi * (cos(alpha - beta) - cos(alpha))))
    return vf


def planets(save: bool, vis: bool):
    for p, v in V.items():
        vf_v = [gravity(beta, v) for beta in betas]
        plt.plot(betas, vf_v, label=f'{p}', marker='D', markersize=2.5, linewidth=1)

        beta_v_max = betas[vf_v.index(max(vf_v))]
        plt.vlines(beta_v_max, 0, 100, linestyles='--', colors='black', alpha=0.05)

        plt.title(r'Vf(β) for planets of Solar system'+
                  f'\nVf(β)->max: β-α={round((beta_v_max-alpha)*180/pi)}°', fontsize=10)

        plt.xlim([-1.7, 4.58])
        plt.ylim([0, 100])

        plt.grid(linestyle=':')
        plt.legend(loc=1, fontsize=8)

        plt.xlabel(r'β, radians')
        plt.ylabel(r'$vf(β), km/s$')

    if save is True:
        plt.savefig(f"graphs/g_m/K-1.pdf", format='pdf', dpi=2000)
    if vis is True:
        plt.show()


if __name__ == '__main__':
    planets(save=True, vis=False)
