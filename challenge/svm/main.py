__author__ = 'romain'

from svm import *

# Get trained classifier
clf = load_or_train(cfg_force_train, cfg_do_tuning)
