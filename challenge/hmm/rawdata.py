__author__ = 'romain'

import os
import csv
import numpy as np
from config import *
from features import *

""" List a directory for the given extension. A tag can be provided for further filtering """
def list_dir(path, tag="", extension='.txt'):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(extension) and f.__contains__(tag)]

""" Search a key-value into the raw data header file """
def get_classid(file, header_start='#', tag='ClassId'):

    of = open(file, "rb")

    reader = csv.reader(of, dialect="excel-tab")
    for line in reader:
        # exit if the line is no more part of the header
        if not line[0].startswith(header_start):
            break

        # test if the key is found, if true return the value and exit
        if line[0] == header_start+tag:
            label = line[1]
            break

    return int(label)


""" strip rawdata files up to given count """
def strip_data(files, count):

    if count == 0:
        return files

    return files[:count]


def load_features(path, sensor_type, class_id="all"):

    # Create a list of all files
    files = list_dir(path, sensor_type)

    # eventually strip files list up to given count
    files = strip_data(files, trainset_count)

    model_features = []

    # iterate over data files
    for f in files:
        # If data file correspond to gesture
        file_class_id = get_classid(f)
        if class_id == "all" or file_class_id == class_id:
            single_file_features = load_single_file_features(f)
            if single_file_features.ndim == 2:
                model_features.append(single_file_features)

    return model_features


def load_single_file_features(f):
    of = open(f, "rb")

    # Read data and extract features
    if "Kinect" in f:
        data = np.loadtxt(of, usecols=kinect_sensors_selected)
        single_file_features = extract[features_type](data)
        single_file_features = data

    elif "Xsens" in f:
        data = np.loadtxt(of, usecols=xsens_sensors_selected)
        single_file_features = extract[features_type](data)
        single_file_features = data

    else:
        print("Unrecognised data file")
        return

    return single_file_features