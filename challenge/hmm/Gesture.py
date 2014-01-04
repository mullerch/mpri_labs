from __future__ import print_function
from sklearn import hmm, cross_validation
from rawdata import *

import pickle

class Gesture:
    def __init__(self, class_id, nb_states, name):
        self.model = None
        self.class_id = class_id
        self.nb_states = nb_states
        self.name = name

        self.data_kinect_train = []
        self.data_kinect_test = []

        self.data_xsens_train = []
        self.data_xsens_test = []

        self.data_all_train = []
        self.data_all_test = []

    """
    Load an existing one or train a new HMM classifier, and return it.
    Once the classifier is trained, it's saved through pickle.
    """
    def train_nLoad_model(self, force_train=False):

        model_path = "gesture_" + str(self.class_id) + "_model.pkl"

        if not force_train and os.path.exists(model_path):
            with open(model_path, 'rb') as handle:
                self.model = pickle.load(handle)
        else:
            print("Model training for gesture", self.name)

            # Instantiate a model
            self.model = hmm.GaussianHMM(self.nb_states, algorithm='viterbi')

            # Loading all data
            data_kinect = self.load_features(trainset_path, 'Kinect')
            data_xsens = self.load_features(trainset_path, 'Xsens')

            # Decompose datas in train/test sets
            self.data_kinect_train, self.data_kinect_test = \
                cross_validation.train_test_split(data_kinect, test_size=test_data_ratio, random_state=random_state_seed)

            self.data_xsens_train, self.data_xsens_test = \
                cross_validation.train_test_split(data_xsens, test_size=test_data_ratio, random_state=random_state_seed)

            self.data_all_train.append(self.data_kinect_train)
            self.data_all_train.append(self.data_xsens_train)

            self.data_all_test.append(self.data_kinect_test)
            self.data_all_test.append(self.data_xsens_test)

            # Fit the model to gesture
            self.model.fit(self.data_xsens_train)

            with open(model_path, 'wb') as handle:
                pickle.dump(self.model, handle)

            ###############################################################################
            # print trained parameters and plot
            print("=== Transition matrix ===")
            print(self.model.transmat_)
            print()

            # print("=== Means and vars of each hidden state ===")
            for i in range(self.nb_states):
                print("%dth hidden state" % i)
                print("mean = ", self.model.means_[i])
                print("var = ", np.diag(self.model.covars_[i]))
                print()

    def load_features(self, path, sensor_type):

        # Create a list of all files ending in .jpg
        files = list_dir(path, sensor_type)

        # eventually strip files list up to given count
        files = strip_data(files, trainset_count)

        model_features = []

        # iterate over data files
        for f in files:
            # If data file correspond to gesture
            if get_classid(f) == self.class_id:
                model_features.append(load_single_file_features(f))

        return model_features
