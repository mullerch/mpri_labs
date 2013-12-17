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

""" Return labels and features for all rawdata files in path. """
def load_data(path, type):

    # Create a list of all files ending in .jpg
    files = list_dir(path, 'Kinect')

    # eventually strip files list up to given count
    files = strip_data(files, trainset_count)

    # Global lists for the labels and features
    labels = []
    kinect_fts = []
    xsens_fts = []

    # iterate over kinect data files
    for f in files:
        of = open(f,"rb")

        # get label and features for current raw data file
        label = kinect_get_label(of)
        data = np.loadtxt(of, usecols=kinect_selected_joints)
        ft = extract_ft(data)

        # append to already global list of labels and features
        labels.append(int(label))
        kinect_fts.append(ft)

    # return features, and labels
    return np.array(kinect_fts), np.array(labels)