import numpy as np
import time
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
X, y = digits.data, digits.target

for n in np.arange(300, 3100, 100):
    t = time.time_ns()
    tsne_ = TSNE(n_jobs=-1, n_iter=n, n_components=2, random_state=17)
    X_reduced = tsne_.fit_transform(X)

    plt.figure(figsize=(8, 6))
    plt.title(f't-SNE(digits): iteration {n}, t = {round((time.time_ns() - t ) / pow(10, 9), 1)}s', fontsize=10)
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, edgecolors='k', cmap=plt.cm.get_cmap('nipy_spectral', 10),
                alpha=0.7, s=20)
    dt = f'{(t - time.time_ns()) / pow(10, 9)} s'
    plt.colorbar(label='digits')
    # plt.savefig(f'photo/{n}.jpg')
    # plt.show()
