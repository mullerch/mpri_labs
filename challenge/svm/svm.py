import os
import pickle
from sklearn import svm, grid_search, cross_validation
from rawdata import *


"""
Load an existing one or train a new SVM classifier, and return it.
Once the classifier is trained, it is saved through pickle.
"""
def load_or_train(force_train=False):

    clf = None

    if not force_train and os.path.exists(clf_path):
        clf = pickle.load(open(clf_path, 'rb'))
    else:
        # Loading all data
        X, y = load_data(trainset_path, 'Kinect')

        # Instantiate a classifier
        clf = svm.SVC()
        print X.shape
        print y.shape
        clf.fit(X, y)

        # Cross validation
        # do cross-validation and print cross-validation result (mean accuracy +/- standard deviation)
        scores = cross_validation.cross_val_score(clf, X, y, cv=10)
        print scores
        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # return the classifier
    return clf