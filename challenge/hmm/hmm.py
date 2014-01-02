from __future__ import print_function
from sklearn import hmm, cross_validation
from rawdata import *

import pickle

"""
Load an existing one or train a new HMM classifier, and return it.
Once the classifier is trained, it's saved through pickle.
"""
def load_or_train(force_train=False):

    model = None

    if not force_train and os.path.exists(model_path):
        model = pickle.load(open(model_path, 'rb'))
    else:
        # Loading all data
        X = load_data(trainset_path, 'Kinect')

        n_components = 5

        # Instantiate a classifier
        # model = hmm.GaussianHMM(algorithm='viterbi', n_components=1, covariance_type='diag')
        # print X[0]

        model = hmm.GaussianHMM(n_components, algorithm='viterbi')

        model.fit([X])

        print(X)

        ###############################################################################
        # print trained parameters and plot
        print("=== Transition matrix ===")
        print(model.transmat_)
        print()


        print("=== Means and vars of each hidden state ===")
        for i in range(n_components):
            print("%dth hidden state" % i)
            print("mean = ", model.means_[i])
            print("var = ", np.diag(model.covars_[i]))
            print()


        # Cross validation
        # do cross-validation and print cross-validation result (mean accuracy +/- standard deviation)
        scores = cross_validation.cross_val_score(model, [X], y, cv=10)
        print(scores)
        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # return the classifier
    return model