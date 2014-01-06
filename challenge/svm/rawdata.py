__author__ = 'romain'

import os
import csv
import re

from config import *
from features import *
from sklearn import preprocessing

""" List a directory for the given extension. A tag can be provided for further filtering """
def list_dir(path, tag="", extension='.txt'):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(extension) and f.__contains__(tag)]

""" Search a key-value into the raw data header file """
def get_label(open_file, header_start='#', tag='ClassId'):
    reader = csv.reader(open_file, dialect="excel-tab")
    label = ''
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
    if cfg_norm_type == '':
        return X
    else:
        return preprocessing.normalize(X, norm=cfg_norm_type)

"""
Return labels and features for all rawdata files in path.
if 'labeled' then returned 'y' contains corresponding class id.
if not then 'y' contains corresponding file id.
"""
def load_data(path, sensors, labeled):

    # Create a list of all files of Kinect sensor datas
    filenames = list_dir(path, cfg_device_selected)

    # eventually strip files list up to given count
    filenames = strip_data(filenames, cfg_trainset_count)

    # Global lists for the labels and features
    ids = []
    fts = []

    # iterate over kinect data files
    for filename in filenames:
        file = open(filename,"rb")

        # default matrix and get label for current file
        rawdatas = np.zeros(1)
        if labeled:
            label = get_label(file)
        else:
            file_index = re.search('([0-9]+)', filename).group(0)

        # load sensors data as columns for current gesture file
        if len(sensors_selected) > 0:
            rawdatas = np.loadtxt(file, usecols=sensors)

        # skip if loading data failed
        if rawdatas.size == 0:
            continue

        # extract some proper features from raw datas
        ft = extract[cfg_features_type](rawdatas)

        # append to already global list of labels and features
        if labeled:
            ids.append(int(label))
        else:
            ids.append(int(file_index))

        fts.append(ft)

    # return features, and labels
    return norm(np.array(fts)), np.array(ids)