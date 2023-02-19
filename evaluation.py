from changeTypeData import *
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

def cal_F(tn, fp, fn, tp):
    P = tp / (tp + fp)
    R = tp / (tp + fn)

    F = (2 * P * R) / (P + R)

    return F


def evaluation():
    print('camel:')
    real_label , pre_label = readFromCSV('camel', 1.6)
    # su dung confusion matrix de danh gia hieu qua
    tn, fp, fn, tp = confusion_matrix(real_label, pre_label).ravel()
    print(f1_score(real_label,pre_label))

    print('jedit:')
    real_label , pre_label = readFromCSV('jedit', 4.1)
    # su dung confusion matrix de danh gia hieu qua
    tn, fp, fn, tp = confusion_matrix(real_label, pre_label).ravel()
    print(f1_score(real_label, pre_label))

    print('lucene:')
    real_label , pre_label = readFromCSV('lucene', 2.2)
    # su dung confusion matrix de danh gia hieu qua
    tn, fp, fn, tp = confusion_matrix(real_label, pre_label).ravel()
    print(f1_score(real_label, pre_label))

    print('xalan:')
    real_label , pre_label = readFromCSV('xalan', 2.6)
    # su dung confusion matrix de danh gia hieu qua
    tn, fp, fn, tp = confusion_matrix(real_label, pre_label).ravel()
    print(f1_score(real_label, pre_label))

    print('xerces:')
    real_label , pre_label = readFromCSV('xerces', 1.3)
    # su dung confusion matrix de danh gia hieu qua
    tn, fp, fn, tp = confusion_matrix(real_label, pre_label).ravel()
    print(f1_score(real_label, pre_label))

    print('synapse:')
    real_label , pre_label = readFromCSV('synapse', 1.2)
    # su dung confusion matrix de danh gia hieu qua
    tn, fp, fn, tp = confusion_matrix(real_label, pre_label).ravel()
    print(f1_score(real_label, pre_label))

    print('poi:')
    real_label , pre_label = readFromCSV('poi', 3.0)
    # su dung confusion matrix de danh gia hieu qua
    tn, fp, fn, tp = confusion_matrix(real_label, pre_label).ravel()
    print(f1_score(real_label, pre_label))


if __name__ == "__main__":
    evaluation()