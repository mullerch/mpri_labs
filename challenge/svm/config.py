__author__ = 'romain'

####################
### FIXED CONFIG ###
####################

# KINECT specific data file format infos
kinect = 'Kinect'
kinect_sensors = dict()
kinect_sensors["FromSkeletonMassCenter"] = (1,2,3)
kinect_sensors["ShoulderCenter"] = (16,17,18)
kinect_sensors["Head"] = (21,22,23)
kinect_sensors["ShoulderLeft"] = (26,27,28)
kinect_sensors["ElbowLeft"] = (31,32,33)
kinect_sensors["WristLeft"] = (36,37,38)
kinect_sensors["HandLeft"] = (41,42,43)
kinect_sensors["ShoulderRight"] = (46,47,48)
kinect_sensors["ElbowRight"] = (51,52,53)
kinect_sensors["WristRight"] = (56,57,58)
kinect_sensors["HandRight"] = (61,62,63)

# XSENS specific data file format infos
xsens = 'Xsens'
xsens_sensors = dict()
xsens_sensors["ShoulderLinAcc"] = (2, 3, 4)
xsens_sensors["ShoulderAngVel"] = (5, 6, 7)
xsens_sensors["ShoulderMag"] = (8, 9, 10)
xsens_sensors["ShoulderYawPitchRoll"] = (11, 12, 13)
xsens_sensors["ShoulderQuat"] = (14, 15, 16, 17)
xsens_sensors["ElbowLinAcc"] = (19, 20, 21)
xsens_sensors["ElbowAngVel"] = (22, 23, 24)
xsens_sensors["ElbowMag"] = (25, 26, 27)
xsens_sensors["ElbowYawPitchRoll"] = (28, 29, 30)
xsens_sensors["ElbowQuat"] = (31, 32, 33, 34)
xsens_sensors["WristLinAcc"] = (36, 37, 38)
xsens_sensors["WristAngVel"] = (39, 40, 41)
xsens_sensors["WristMag"] = (42, 43, 44)
xsens_sensors["WristYawPitchRoll"] = (45, 46, 47)
xsens_sensors["WristQuat"] = (48, 49, 50, 51)
xsens_sensors["HandLinAcc"] = (53, 54, 55)
xsens_sensors["HandAngVel"] = (56, 57, 58)
xsens_sensors["HandMag"] = (59, 60, 61)
xsens_sensors["HandYawPitchRoll"] = (62, 63, 64)
xsens_sensors["HandQuat"] = (65, 66, 67, 68)

# global dict for all sensors
sensors = dict()
sensors[kinect] = kinect_sensors
sensors[xsens] = xsens_sensors

# global dict for all selected sensors
sensors_selected = list()

# path to store the classifier
cfg_clf_path='clf.pkl'

# raw data path for training
cfg_trainset_path = "../data/Training/"

###################
### USER CONFIG ###
###################

# force the training or load the stored classifier (see below)
cfg_force_train = True

# activate classifier tuning mode (see parameters below)
cfg_do_tuning = True

# maximum number of files to load, 0=all
cfg_trainset_count = 200

# selected device
cfg_device_selected = xsens # kinect or xsens or ''

# selected sensors for previously selected device
sensors_selected = ["WristQuat"]

# normalize type
cfg_norm_type = 'l2' # '' or 'l1' or 'l2'

# select which algorithm to use for features extraction
cfg_features_type = "flatten"

### CLASSIFIER TUNING ###

# use all sensors for selected device or only the selected ones
cfg_tuning_use_all_sensors = False

# parameters list for grid search
cfg_tuning_gridsearch_params = [
    {'C': [0.1, 1, 4, 8, 16, 32, 64, 128], 'gamma': [4.0, 2.0, 1.0, 0.5, 0.25, 0.1, 0.001], 'kernel': ['rbf']},
    {'C': [0.1, 1, 4, 8, 16, 32, 64], 'gamma': [4.0, 2.0, 1.0, 0.5, 0.25, 0.1], 'kernel': ['linear']},
    {'C': [0.1, 1, 4, 8, 16, 32, 64], 'gamma': [4.0, 2.0, 1.0, 0.5, 0.25, 0.1], 'kernel': ['poly']}
]

### CLASSIFIER FINAL ###

# svm params for real classifier
cfg_svm_kernel = 'linear'
cfg_svm_C = 32
cfg_svm_gamma = 1