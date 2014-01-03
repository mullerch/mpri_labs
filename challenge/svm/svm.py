from Carbon.QuickTime import kVDGetInputGammaRecordSelect
import os
import pickle
from sklearn import svm, grid_search, cross_validation
from rawdata import *
import metrics
import config
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt


"""
Load an existing one or train a new SVM classifier, and return it.
Once the classifier is trained, it is saved through pickle.
"""
def load_or_train(force_train=False, tuning_mode=False):

    clf = None

    if not force_train and os.path.exists(clf_path):
        clf = pickle.load(open(clf_path, 'rb'))

    elif tuning_mode:
        results = dict()

        # do grid search for every Xsens sensor
        for header in xsens_data_headers.iterkeys():

            X, y = load_data(trainset_path, dict(), xsens_data_headers[header])

            clf = grid_search.GridSearchCV(svm.SVC(), param_grid, verbose=1)
            clf.fit(X, y, cross_validation=10)

            # print which is the best set of params found
            print "Best set of params found for sensor '" + header + "':"
            clf = clf.best_estimator_
            print(clf)

            # Cross validation
            scores = cross_validation.cross_val_score(clf, X, y, cv=10)
            metrics.print_cross_validation_results(scores)

            # add result to global result list
            results[header + "\n(kernel=" + clf.kernel + ", C=" + str(clf.C) + ", gamma=" + str(clf.gamma) + ")"] = scores.mean()

        # plot results
        desc = "Various parameters used:\n\n" + "training set size (0 means all) = " + str(trainset_count) + "\n"\
        "normalize type = " + normalize_type + "\n"\
        "features extraction type = " + features_type

        fig = plt.figure(1)
        labels = np.arange(len(results.values()))
        ax1 = fig.add_axes((.35,.4,.5,.5))
        ax1.barh(labels ,results.values(), align='center', height=0.2)    # notice the 'height' argument
        plt.yticks(labels, results.keys())
        plt.xlabel('Accuracy')
        plt.title('Best accuracy for each Xsens sensor (found by grid searching)')
        plt.grid(True)
        plt.xlim([0,1.0])
        fig.text(.1,.1,desc)
        plt.show()


    else:
        # Load training data set
        X, y = load_data(trainset_path, kinect_sensors_selected, xsens_sensors_selected)

        # Instantiate a classifier
        clf = svm.SVC(svm_kernel, svm_C, svm_gamma)
        clf.fit(X, y)

    # return the classifier
    return clf