__author__ = 'romain'

import features

# dictionary to hold corresponding columns indices for each body part tracked
kinect_data_headers = dict()
kinect_data_headers["Global"] = (1,2,3)
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

# selected joints data from the KINECT device
kinect_sensors_selected = \
    kinect_data_headers["Global"] + \
    kinect_data_headers["ShoulderCenter"] + \
    kinect_data_headers["Head"] + \
    kinect_data_headers["ShoulderLeft"] + \
    kinect_data_headers["ElbowLeft"] + \
    kinect_data_headers["WristLeft"] + \
    kinect_data_headers["HandLeft"] + \
    kinect_data_headers["ShoulderRight"] + \
    kinect_data_headers["ElbowRight"] + \
    kinect_data_headers["WristRight"] + \
    kinect_data_headers["HandRight"]

# selected joints data from the XSENS device
# xsens_sensors_selected = \
#     xsens_data_headers["ShoulderLinAcc"] + \
#     xsens_data_headers["ShoulderAngVel"] + \
#     xsens_data_headers["ShoulderMag"] + \
#     xsens_data_headers["ShoulderYawPitchRoll"] + \
#     xsens_data_headers["ShoulderQuat"] + \
#     xsens_data_headers["ElbowLinAcc"] + \
#     xsens_data_headers["ElbowAngVel"] + \
#     xsens_data_headers["ElbowMag"] + \
#     xsens_data_headers["ElbowYawPitchRoll"] + \
#     xsens_data_headers["ElbowQuat"] + \
#     xsens_data_headers["WristLinAcc"] + \
#     xsens_data_headers["WristAngVel"] + \
#     xsens_data_headers["WristMag"] + \
#     xsens_data_headers["WristYawPitchRoll"] + \
#     xsens_data_headers["WristQuat"] + \
#     xsens_data_headers["HandLinAcc"] + \
#     xsens_data_headers["HandAngVel"] + \
#     xsens_data_headers["HandMag"] + \
#     xsens_data_headers["HandYawPitchRoll"] + \
#     xsens_data_headers["HandQuat"]

xsens_sensors_selected = \
    xsens_data_headers["ShoulderLinAcc"] + \
    xsens_data_headers["ShoulderYawPitchRoll"] + \
    xsens_data_headers["ShoulderAngVel"] + \
    xsens_data_headers["ElbowLinAcc"] + \
    xsens_data_headers["ElbowYawPitchRoll"] + \
    xsens_data_headers["ElbowAngVel"] + \
    xsens_data_headers["WristLinAcc"] + \
    xsens_data_headers["WristYawPitchRoll"] + \
    xsens_data_headers["WristAngVel"] + \
    xsens_data_headers["HandLinAcc"] + \
    xsens_data_headers["HandYawPitchRoll"] + \
    xsens_data_headers["HandAngVel"]


# dictionary with various features extraction algorithms
extract = dict()
extract["flatten"] = features.extract_flatten
extract["pca"] = features.extract_pca

# select which algorithm to use for features extraction
features_type = "flatten"

# raw data path for training
trainset_path = "../data/Training/"
evaluationset_path = "../data/Sample_Evaluation/"

# maximum rawdata files to load, 0=all
trainset_count = 0

test_data_ratio = 0.4

random_state_seed = 0