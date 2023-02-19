from buildCNN import *
from changeTypeData import *
from imblearn.over_sampling import SMOTE, BorderlineSMOTE, RandomOverSampler, ADASYN, SVMSMOTE
from imblearn.under_sampling import NearMiss, NeighbourhoodCleaningRule, RandomUnderSampler, CondensedNearestNeighbour, TomekLinks, EditedNearestNeighbours, OneSidedSelection
import numpy as np

def sampling(name_samp, inter_vector, trad_feature, label):
    try:
        t = len(inter_vector[0])
        print([t])
        print(inter_vector.shape)
        print(trad_feature.shape)
        feature = np.concatenate((inter_vector.T, trad_feature.T), axis= 0).T
        print(feature.shape)
        print(label.shape)
        # over sampling
        if (name_samp == 'SMOTE'):
            model_sampling = SMOTE(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'BorderlineSMOTE'):
            model_sampling = BorderlineSMOTE(sampling_strategy='minority', random_state=2)
        if (name_samp == 'SVMSMOTE'):
            model_sampling = SVMSMOTE(sampling_strategy='minority', random_state=2)
        if (name_samp == 'RandomOverSampler'):
            model_sampling = RandomOverSampler(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'ADASYN'):
            model_sampling = ADASYN(sampling_strategy='minority' ,random_state=2)

        #under sampling
        if (name_samp == 'RandomUnderSampler'):
            model_sampling = RandomUnderSampler(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'CNN'):
            model_sampling = CondensedNearestNeighbour(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'NearMiss'):
            model_sampling = NearMiss(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'NCR'):
            model_sampling = NeighbourhoodCleaningRule(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'TomekLink'):
            model_sampling = TomekLinks(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'ENN'):
            model_sampling = EditedNearestNeighbours(sampling_strategy='minority' ,random_state=2)
        if (name_samp == 'OSS'):
            model_sampling = OneSidedSelection(sampling_strategy='minority' ,random_state=2)



        feature_res, label_res = model_sampling.fit_resample(feature, label.ravel())
        split_feature= np.split(feature_res, [t], axis=1)
        inter_res = split_feature[0]
        trad_res = split_feature[1]
        print('inter_res')
        print(inter_res)
        print(inter_res.shape)
        print('trad_res')
        print(trad_res.shape)

    except:
        inter_res = inter_vector
        trad_res = trad_feature
        label_res = label
    return inter_res, trad_res, label_res



def test():
    parser = Parser(camel)
    x = parser.Parser()
    x_train1 = changeToNumpy(x[1.4].src_files, 'interVector')
    x_train2 = changeToNumpy(x[1.4].src_files, 'tradFeature')
    y_train = changeToNumpy(x[1.4].src_files, 'label')

    sampling('SVMSMOTE', x_train1, x_train2, y_train)


if __name__ == "__main__":
    test()