from __future__ import print_function

import sys

def get_best_model(gestures, features):
    best_score = -sys.maxint
    best_model = 0

    # Get bettest model for the gesture features with HMM
    for model_gesture in gestures:
        score = model_gesture.model.score(features)

        if score > best_score:
            best_model = model_gesture.class_id
            best_score = score

    return best_model