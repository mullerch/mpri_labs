__author__ = 'romain'

import mdp
from sklearn import decomposition
import numpy as np

""" extract simple flatten features from rawdata """
def extract_flatten(raw_data):

    # pad with 0 until 200 frames
    shape = (200,raw_data.shape[1])
    zeros = np.zeros(shape, dtype=np.float32)
    zeros[:raw_data.shape[0], :raw_data.shape[1]] = raw_data

    return zeros.flatten()

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