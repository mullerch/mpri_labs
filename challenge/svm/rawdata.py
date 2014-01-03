__author__ = 'romain'

import os
import csv
import numpy as np

from config import *
from features import *
from sklearn import preprocessing

""" List a directory for the given extension. A tag can be provided for further filtering """
def list_dir(path, tag="", extension='.txt'):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(extension) and f.__contains__(tag)]

""" Search a key-value into the raw data header file """
def kinect_get_label(open_file, header_start='#', tag='ClassId'):
    reader = csv.reader(open_file, dialect="excel-tab")
    for line in reader:
        # exit if the line is no more part of the header
        if not line[0].startswith(header_start):
            break

        # test if the key is found, if true return the value and exit
        if line[0] == header_start+tag:
            label = line[1]
            break

    return label

""" strip rawdata files up to given count """
def strip_data(files, count):

    if count == 0:
        return files

    return files[:count]

""" normalize raw data between -1:1 """
def norm(X):
    if normalize_type == '':
        return X
    else:
        return preprocessing.normalize(X, norm=normalize_type)

""" Return labels and features for all rawdata files in path. """
def load_data(path, kinect_selected, xsens_selected):

    # Create a list of all files of Kinect sensor datas
    kinect_filenames = list_dir(path, kinect_filename_prefix)

    # eventually strip files list up to given count
    kinect_filenames = strip_data(kinect_filenames, trainset_count)

    # Global lists for the labels and features
    labels = []
    fts = []

    # iterate over kinect data files
    for kinect_filename in kinect_filenames:
        kinect_file = open(kinect_filename,"rb")

        # get xsens equivalent gesture filename
        xsens_filename = kinect_filename.replace(kinect_filename_prefix, xsens_filename_prefix)
        xsens_file = open(xsens_filename,"rb")

        # get label and features for current gesture
        kinect_data = np.zeros(1)
        xsens_data = np.zeros(1)
        label = kinect_get_label(kinect_file)
        if len(kinect_sensors_selected) > 0:
            kinect_data = np.loadtxt(kinect_file, usecols=kinect_selected)
        if len(xsens_sensors_selected) > 0:
            xsens_data = np.loadtxt(xsens_file, usecols=xsens_selected)

        # skip if loading data failed
        if kinect_data.size + xsens_data.size == 0:
            continue

        # extract some proper features from raw datas
        ft = extract[features_type](kinect_data + xsens_data)

        # append to already global list of labels and features
        labels.append(int(label))
        fts.append(ft)

    # return features, and labels
    return norm(np.array(fts)), np.array(labels)