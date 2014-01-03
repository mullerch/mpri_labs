from sklearn.metrics.metrics import confusion_matrix, classification_report
import pylab as pl

"""
Plot (and print) a confusion matrix from y_true and y_predicted
"""
def show_confusion_matrix(y_true, y_predicted, title=''):

    # compute confusion matrix
    cm = confusion_matrix(y_true, y_predicted)
    print cm
    # configure window
    pl.matshow(cm)
    pl.title(title)
    pl.colorbar()
    pl.ylabel('True label')
    pl.xlabel('Predicted label')
    pl.jet()
    # show confusion matrix plot
    pl.show()

"""
Print a classification report
"""
def print_classification_report(y_true, y_pred, title=''):

    cr = classification_report(y_true, y_pred)
    print cr