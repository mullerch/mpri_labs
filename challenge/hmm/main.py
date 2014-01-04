from __future__ import print_function
__author__ = 'christian'

from Gesture import *
from validation import *

# Define gestures (Id, Number of hidden states, label)
gestures = list()
gestures.append(Gesture(1, 5, "Swipe left"))
gestures.append(Gesture(2, 5, "Swipe right"))
gestures.append(Gesture(3, 3, "Push to screen"))
gestures.append(Gesture(4, 3, "Take from screen"))
gestures.append(Gesture(5, 9, "Palm-up rotation"))
gestures.append(Gesture(6, 9, "Palm-down rotation"))
gestures.append(Gesture(7, 3, "Draw circle 1"))
gestures.append(Gesture(8, 3, "Draw circle 2"))
gestures.append(Gesture(9, 5, "Wave hello"))
gestures.append(Gesture(10, 5, "Shake hand"))

# Train gestures models
for gesture in gestures:
    gesture.train_nLoad_model(True)

# Validate data (result is printed)
validate(gestures)


# features = []
# best_score = -1000000000
# best_id = 0
#
# # Load single file features
# features = load_single_file_features(trainset_path + "Xsens_102.txt")
#
# # Compute score for each gesture model
# for gesture in gestures:
#     score = gesture.model.score(features)
#
#     if score > best_score:
#         best_id = gesture.class_id
#         best_score = score
#
#     print("Score with gesture", gesture.class_id, ":", score)
#
# print("==> Gesture recognised as", best_id) #", kinect_get_classid(of), "