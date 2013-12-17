__author__ = 'romain'

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

# selected joints data from the kinect device
kinect_selected_joints = \
    kinect_data_headers["HandRight"] + \
    kinect_data_headers["WristRight"]

# path to store the classifier
clf_path='clf.pkl'

# raw data path for training
trainset_path = "../data/Training/"

# maximum rawdata files to load, 0=all
trainset_count = 200

