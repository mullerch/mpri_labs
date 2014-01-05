from hmm import *
from Gesture import *

import re

def evaluate(gestures):
    print "Data evaluation in progess...",

    # Create a list of all files
    files = list_dir(evaluationset_path, "Xsens")

    # eventually strip files list up to given count
    files = strip_data(files, trainset_count)

    evaluation_results = list()
    # Iterate over data files
    for f in files:
        file_index = re.search('([0-9]+)', f).group(0)
        single_file_features = load_single_file_features(f)
        if single_file_features.ndim == 2:
            evaluation_results.append([int(file_index), get_best_model(gestures, single_file_features)])

    result_file = open(evaluation_result_path, 'w')
    result_file.write("#AlgoName\tHMM\n")
    result_file.write("#GroupName\t%s\n" % group_name)

    evaluation_results = sorted(evaluation_results, key=lambda col: col[0])

    for result in evaluation_results:
        result_file.write("%s\t%d\n" % (result[0], result[1]))

    print " done!"
    print "%d files evaluated successfully, result has been stored in '%s'" % (len(files), evaluation_result_path)