from __future__ import division
from hmm import *


def validate(gestures):

    # Create initialized convolution matrix
    nb_gestures = len(gestures)
    validation_result = [None] * (nb_gestures+1)
    for i in range(nb_gestures+1):
        validation_result[i] = [0] * (nb_gestures+1)

    # Do validation for each gesture
    for validating_gesture in gestures:

        # Get each feature set from the gesture
        for features in validating_gesture.data_xsens_test:

            # Fill convolution matrix
            best_model = get_best_model(gestures, features)
            validation_result[validating_gesture.class_id-1][best_model-1] += 1
            validation_result[validating_gesture.class_id-1][nb_gestures] += 1
            validation_result[nb_gestures][best_model-1] += 1

    print("=== Convolution matrix ===")
    print("Lines are the gestures and columns how they are recognized")
    print "%2s %20s  " % ("ID", "GESTURE"),
    for gesture in gestures:
        print "%3d" % (gesture.class_id),

    print "%7s" % ("| TOTAL  ACCURACY")

    print "%s" % ("-" * ((nb_gestures*4)+43))

    mean_accuracy = 0
    for gesture in gestures:
        print "%2d %20s %s" % (gesture.class_id, gesture.name, ":"),
        print "%3d %3d %3d %3d %3d %3d %3d %3d %3d %3d | %3d" % tuple(validation_result[gesture.class_id-1]),
        accuracy = validation_result[gesture.class_id-1][gesture.class_id-1] /\
                   validation_result[gesture.class_id-1][nb_gestures]
        mean_accuracy += accuracy
        validation_result[nb_gestures][nb_gestures] += validation_result[gesture.class_id-1][nb_gestures]
        print "%8d%%" % (accuracy*100)

    print "%s" % ("-" * ((nb_gestures*4)+43))

    print "%23s %s" % ("TOTAL", ":"),
    print "%3d %3d %3d %3d %3d %3d %3d %3d %3d %3d | %3d" % tuple(validation_result[nb_gestures]),
    print "%8d%%" % (mean_accuracy/nb_gestures*100)
    print ""