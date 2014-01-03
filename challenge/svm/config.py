__author__ = 'romain'

import features


### DATA SELECTION ###

# KINECT specific infos
kinect_filename_prefix = 'Kinect'
kinect_data_headers = dict()
kinect_data_headers["FromSkeletonMassCenter"] = (1,2,3)
kinect_data_headers["ShoulderCenter"] = (16,17,18)
kinect_data_headers["Head"] = (21,22,23)
kinect_data_headers["ShoulderLeft"] = (26,27,28)
kinect_data_headers["ElbowLeft"] = (31,32,33)
kinect_data_headers["WristLeft"] = (36,37,38)
kinect_data_headers["HandLeft"] = (41,42,43)
kinect_data_headers["ShoulderRight"] = (46,47,48)
kinect_data_headers["ElbowRight"] = (51,52,53)
kinect_data_headers["WristRight"] = (56,57,58)
kinect_data_headers["HandRight"] = (61,62,63)

# XSENS specific infos
xsens_filename_prefix = 'Xsens'
xsens_data_headers = dict()
xsens_data_headers["ShoulderLinAcc"] = (2, 3, 4)
xsens_data_headers["ShoulderAngVel"] = (5, 6, 7)
xsens_data_headers["ShoulderMag"] = (8, 9, 10)
xsens_data_headers["ShoulderYawPitchRoll"] = (11, 12, 13)
xsens_data_headers["ShoulderQuat"] = (14, 15, 16, 17)
xsens_data_headers["ElbowLinAcc"] = (19, 20, 21)
xsens_data_headers["ElbowAngVel"] = (22, 23, 24)
xsens_data_headers["ElbowMag"] = (25, 26, 27)
xsens_data_headers["ElbowYawPitchRoll"] = (28, 29, 30)
xsens_data_headers["ElbowQuat"] = (31, 32, 33, 34)
xsens_data_headers["WristLinAcc"] = (36, 37, 38)
xsens_data_headers["WristAngVel"] = (39, 40, 41)
xsens_data_headers["WristMag"] = (42, 43, 44)
xsens_data_headers["WristYawPitchRoll"] = (45, 46, 47)
xsens_data_headers["WristQuat"] = (48, 49, 50, 51)
xsens_data_headers["HandLinAcc"] = (53, 54, 55)
xsens_data_headers["HandAngVel"] = (56, 57, 58)
xsens_data_headers["HandMag"] = (59, 60, 61)
xsens_data_headers["HandYawPitchRoll"] = (62, 63, 64)
xsens_data_headers["HandQuat"] = (65, 66, 67, 68)

# maximum rawdata files to load, 0=all
trainset_count = 0

# selected joints data from the KINECT device
kinect_sensors_selected = () # nothing selected

# selected joints data from the XSENS device
xsens_sensors_selected = xsens_data_headers["ShoulderAngVel"]

normalize_type = 'l2' # '' or 'l1' or 'l2'

### FEATURES EXTRACTION ###

# dictionary with various features extraction algorithms
extract = dict()
extract["flatten"] = features.extract_flatten
extract["pca"] = features.extract_pca

# select which algorithm to use for features extraction
features_type = "flatten"


### CLASSIFIER ###

# path to store the classifier
clf_path='clf.pkl'

# raw data path for training
trainset_path = "../data/Training/"

# parameters list for grid search
param_grid = [
    {'C': [0.01, 0.1, 1, 4, 8, 16, 32, 64, 128], 'gamma': [8.0, 4.0, 2.0, 1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.001, 0.0001], 'kernel': ['rbf']},
    {'C': [0.01, 0.1, 1, 4, 8, 16, 32, 64, 128], 'gamma': [8.0, 4.0, 2.0, 1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.001, 0.0001], 'kernel': ['linear']},
    {'C': [0.01, 0.1, 1, 4, 8, 16, 32, 64, 128], 'gamma': [8.0, 4.0, 2.0, 1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.001, 0.0001], 'kernel': ['poly']}
]

# svm params for real classifier
svm_kernel = 'linear'
svm_C = 32
svm_gamma = 1