import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def tree_class(X, y, max_depth=2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=17)
    clf = DecisionTreeClassifier(max_depth=max_depth, random_state=17)
    clf.fit(X_train, y_train)
    predict = clf.predict_proba(X_test)
    return f"Точність: {round(accuracy_score(y_test, predict.argmax(axis=1)) * 100, 2)}%"


iris = load_iris()
X, y = iris.data, iris.target

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print('Iris dataset:')
print(f'{tree_class(X, y) = }')
print(f'{tree_class(X_reduced, y) = }')

plt.figure(figsize=(6, 5))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, alpha=.7, cmap='Accent', edgecolors='k')
# plt.scatter(X[:, 0], X[:, 1], c=y, alpha=.7, cmap='Accent')
plt.show()

# #----------------------

tsne = TSNE(n_components=2, n_iter=1000, random_state=17, n_jobs=-1)
X_reduced = tsne.fit_transform(X)

print('\nIris dataset (TSNE):')
print(f'{tree_class(X, y) = }')
print(f'{tree_class(X_reduced, y) = }')

plt.figure(figsize=(6, 5))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, alpha=.7, cmap=plt.cm.get_cmap('nipy_spectral', 3), edgecolors='k')
plt.colorbar(ticks=[0, 1, 2])
plt.show()

# -------------------

wine = load_wine()
X, y = wine.data, wine.target

X_reduced = pca.fit_transform(X)

print('\nWine dataset:')
print(f'{tree_class(X, y) = }')
print(f'{tree_class(X_reduced, y) = }')

plt.figure(figsize=(6, 5))
# plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, alpha=.7, cmap='Accent')
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=.7, cmap='gnuplot_r', edgecolors='k')
plt.show()

# #----------------------

tsne = TSNE(n_components=2, n_iter=1000, random_state=17, n_jobs=-1)
X_reduced = tsne.fit_transform(X)

print('\nWine dataset (TSNE):')
print(f'{tree_class(X, y) = }')
print(f'{tree_class(X_reduced, y) = }')

plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=.7, cmap=plt.cm.get_cmap('nipy_spectral', 3), edgecolors='k')
plt.colorbar(ticks=[0, 1, 2])
plt.show()

# -------------------
digits = load_digits()
X, y = digits.data, digits.target

X_reduced = pca.fit_transform(X)

print('\nDigits dataset:')
print(f'{tree_class(X, y) = }')
print(f'{tree_class(X_reduced, y) = }')

plt.figure(figsize=(6, 5))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, alpha=.7, cmap=plt.cm.get_cmap('nipy_spectral', 10), edgecolors='k')
plt.colorbar()
plt.show()

# #-----------------
tsne = TSNE(n_components=2, n_iter=1000, random_state=17, n_jobs=-1)
X_reduced = tsne.fit_transform(X)

print('\nDigits dataset (TSNE):')
print(f'{tree_class(X, y) = }')
print(f'{tree_class(X_reduced, y) = }')

plt.figure(figsize=(6, 5))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, alpha=.7, cmap=plt.cm.get_cmap('nipy_spectral', 10), edgecolors='k')
plt.colorbar()
plt.show()
