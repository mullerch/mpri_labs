__author__ = 'romain'

from sklearn import decomposition
import numpy as np

""" extract simple flatten features from rawdata """
def extract_flatten(raw_data):
    return raw_data.flatten()

def extract_pca(raw_data):

    import matplotlib.pyplot as plt
    fig = plt.figure()
    fig.plot(raw_data)

    pca = decomposition.PCA(n_components=30)
    pca.fit(raw_data.T)
    X = pca.transform(raw_data.T)
    print raw_data.T[0]
    print X[0]
    #exit()

    return X.flatten()