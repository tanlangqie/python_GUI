import numpy as np
from sklearn.decomposition import PCA
import pandas as pd




X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=1)
pca.fit(X)
# PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
#   svd_solver='auto', tol=0.0, whiten=False)
print(pca.explained_variance_ratio_)

print(pca.singular_values_)
