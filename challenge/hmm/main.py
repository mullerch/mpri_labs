from __future__ import print_function
__author__ = 'christian'

from Gesture import *
from rawdata import *

# Define gestures
gestures = list()
gestures.append(Gesture(1, 5, "Swipe left"))
gestures.append(Gesture(2, 5, "Swipe right"))
gestures.append(Gesture(3, 5, "Push to screen"))
gestures.append(Gesture(4, 5, "Take from screen"))
gestures.append(Gesture(5, 5, "Palm-up rotation"))
gestures.append(Gesture(6, 5, "Palm-down rotation"))
gestures.append(Gesture(7, 5, "Draw circle 1"))
gestures.append(Gesture(8, 5, "Draw circle 2"))
gestures.append(Gesture(9, 9, "Wave hello"))
gestures.append(Gesture(10, 9, "Shake hand"))

# Train gestures models
for gesture in gestures:
    gesture.train_nLoad_model(True)


of = open(trainset_path + "Kinect_250.txt", "rb")
kinect_features = []
best_score = -1000000000
best_id = 0

# Read data and extract features
data = np.loadtxt(of, usecols=kinect_selected_joints)
kinect_features.append(extract_ft(data))

# Format for HMM functions
kinect_features = np.array(kinect_features)[0]
kinect_features = kinect_features[:, np.newaxis]


for gesture in gestures:
    score = gesture.model.score(kinect_features)

    if score > best_score:
        best_id = gesture.class_id
        best_score = score

    print("Score with gesture", gesture.class_id, ":", score)

print("==> Gesture recognised as", best_id) #", kinect_get_classid(of), "