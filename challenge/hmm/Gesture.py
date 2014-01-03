from __future__ import print_function
from sklearn import hmm
from rawdata import *

import pickle


class Gesture:
    def __init__(self, class_id, nb_states, name):
        self.model = None
        self.class_id = class_id
        self.nb_states = nb_states
        self.name = name
        self.kinect_features = []

    """
    Load an existing one or train a new HMM classifier, and return it.
    Once the classifier is trained, it's saved through pickle.
    """
    def train_nLoad_model(self, force_train=False):

        model_path = "gesture_" + 'self.class_id' + "_model.pkl"

        if not force_train and os.path.exists(model_path):
            self.model = pickle.load(open(model_path, 'rb'))
        else:
            print("Model training for gesture", self.name)
            # Loading all data
            self.load_features(trainset_path, 'Kinect')

            # Instantiate a model
            self.model = hmm.GaussianHMM(self.nb_states, algorithm='viterbi')

            # Fit the model to gesture
            self.model.fit([self.kinect_features])

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

    def load_features(self, path, type):

        # Create a list of all files ending in .jpg
        files = list_dir(path, type)

        # eventually strip files list up to given count
        files = strip_data(files, trainset_count)

        # iterate over kinect data files
        for f in files:
            of = open(f, "rb")

            # If data file correspond to gesture
            if kinect_get_classid(of) == self.class_id:

                # Read data and extract features
                data = np.loadtxt(of, usecols=kinect_selected_joints)
                self.kinect_features.append(extract_ft(data))

        # Format for HMM functions
        self.kinect_features = np.array(self.kinect_features)[0]
        self.kinect_features = self.kinect_features[:, np.newaxis]
