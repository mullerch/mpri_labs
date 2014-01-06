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

    if not force_train and os.path.exists(cfg_clf_path):
        clf = pickle.load(open(cfg_clf_path, 'rb'))

    elif tuning_mode:
        results = dict()

        # do grid search for every sensor in selected device
        for header in sensors[cfg_device_selected].iterkeys():

            if cfg_tuning_use_all_sensors:
                _sensors = sensors[cfg_device_selected][header]
            else:
                # list with corresponding columns index related to the sensors selected
                sensors_selected_columns = ()
                for sensor in sensors_selected:
                    sensors_selected_columns = sensors_selected_columns + sensors[cfg_device_selected][sensor]

                _sensors = sensors_selected_columns
                header = str(sensors_selected) + "\n"

            X, y = load_data(cfg_trainset_path, _sensors, True)

            clf = grid_search.GridSearchCV(svm.SVC(), cfg_tuning_gridsearch_params, verbose=1)
            clf.fit(X, y, cross_validation=10)

            # print which is the best set of params found
            print "Best set of params found for sensor '" + header + "':"
            clf = clf.best_estimator_
            print(clf)

            # Cross validation
            scores = cross_validation.cross_val_score(clf, X, y, cv=10)
            metrics.print_cross_validation_results(scores)

            # add result to global result list
            results[header + " (kernel=" + clf.kernel + ", C=" + str(clf.C) + ", gamma=" + str(clf.gamma) + ")"] = scores.mean()

            # exit if we are not testing all sensors
            if not cfg_tuning_use_all_sensors:
                break;

        # plot results
        desc = "Various parameters used:\n\n" + "training set size (0 means all) = " + str(cfg_trainset_count) + "\n"\
        "normalize type = " + cfg_norm_type + "\n"\
        "features extraction type = " + cfg_features_type

        fig = plt.figure(1)
        labels = np.arange(len(results.values()))
        ax1 = fig.add_axes((.35,.4,.5,.5))
        ax1.barh(labels ,results.values(), align='center', height=0.2)    # notice the 'height' argument
        plt.yticks(labels, results.keys())
        plt.xlabel('Accuracy')
        plt.title('Best accuracy for ' + cfg_device_selected + ' selected sensors (found by grid searching)')
        plt.grid(True)
        plt.xlim([0,1.0])
        fig.text(.1,.1,desc)
        plt.show()


    else:

                # list with corresponding columns index related to the sensors selected
        sensors_selected_columns = ()
        for sensor in sensors_selected:
            sensors_selected_columns = sensors_selected_columns + sensors[cfg_device_selected][sensor]

        # Load training data set
        X, y = load_data(cfg_trainset_path, sensors_selected_columns, True)

        # Instantiate a classifier
        clf = svm.SVC(kernel=cfg_svm_kernel, C=cfg_svm_C, gamma=cfg_svm_gamma)

        # Cross validation
        # do cross-validation and print cross-validation result (mean accuracy +/- standard deviation)
        scores = cross_validation.cross_val_score(clf, X, y, cv=10)
        print scores
        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

        clf.fit(X, y)

        # save trained classifier on disk
        pickle.dump(clf, open(cfg_clf_path, 'wb'))

    # return the classifier
    return clf