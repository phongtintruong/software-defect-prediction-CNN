import numpy as np
import pandas as pd
import csv
from SourceFileToVector import *
from datasets import *
from assets import *

def changeToNumpy(src_files, properties):
    matrix = []
    if (properties == "interVector"):
        for src_id in src_files:
            matrix.append(src_files[src_id].interVector)
    elif (properties == "tradFeature"):
        for src_id in src_files:
            matrix.append(src_files[src_id].tradFeature)
    elif (properties == "label"):
        for src_id in src_files:
            matrix.append(src_files[src_id].label)
    return np.array(matrix)

# function be used to save data to CSV file
def saveToCSV(src_files_predict, name, version):
    _INPUT_ROOT = Path(__file__).parent / 'data_predict'
    data = pd.DataFrame(src_files_predict.items(), columns = ['name', 'data'])
    path_filecsv = _INPUT_ROOT / name /  (name + '-' + str(version) + '.csv')
    with open(path_filecsv, 'w') as f:
        data.to_csv(f)


#function be used to read data from CSV file
def readFromCSV(name, version):
    _INPUT_ROOT = Path(__file__).parent / 'data_predict'
    real_label = []
    predic_label = []
    path_filecsv = _INPUT_ROOT / name / (name + '-' + str(version) + '.csv')
    with open(path_filecsv, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        reader.__next__()
        for line in reader:
            if(line == []):
                pass
            else:
                real_label.append(float(line[2][1:-1].split(',')[0]))
                predic_label.append(float(line[2][1:-1].split(',')[2]))
    f.close
    return real_label, predic_label

def test():
    pass

if __name__ == "__main__":
    test()