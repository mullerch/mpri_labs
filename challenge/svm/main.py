__author__ = 'romain'

from svm import *
from metrics import *

# Get trained classifier
clf = load_or_train(cfg_force_train, cfg_do_tuning)

# If in tuning mode we exit here
if cfg_do_tuning:
    exit()

# list with corresponding columns index related to the sensors selected
sensors_selected_columns = ()
for sensor in sensors_selected:
    sensors_selected_columns = sensors_selected_columns + sensors[cfg_device_selected][sensor]

# Load validation rawdatas
data_is_labeled = False
X, y = load_data(cfg_evaluationset_path, sensors_selected_columns, data_is_labeled)

# Classification
y_pred = clf.predict(X)

result_file = open(cfg_evaluation_result_path, 'w')
result_file.write("#AlgoName\t%s\n" % cfg_algo_name)
result_file.write("#GroupName\t%s\n" % cfg_group_name)

evaluation_results = list()
# Iterate over data files
for i in range(0,y.size):
    evaluation_results.append([y[i], y_pred[i]])

evaluation_results = sorted(evaluation_results, key=lambda col: col[0])

for result in evaluation_results:
    result_file.write("%s\t%d\n" % (result[0], result[1]))

print " done!"
print "result file has been stored in '%s'" % cfg_evaluation_result_path

if (data_is_labeled):
    # show classification report
    print_classification_report(y, y_pred)
    # show confusion matrix
    show_confusion_matrix(y_pred, y)
