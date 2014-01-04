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

    # Format for HMM functions
    #single_file_features = single_file_features[:, np.newaxis]

    return single_file_features