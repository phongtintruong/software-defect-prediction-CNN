from buildCNN import *
from changeTypeData import *
from sampling import *



mark = 0.5

# DP-CNN use camel, jEdit, lucene, xalan, xerces, synapse, poi
def predict(name, sampling_name):
    data = OrderedDict()
    if (name == 'camel'):
        parser = Parser(camel)
        x = parser.Parser()
        x_train1 = changeToNumpy(x[1.4].src_files, 'interVector')
        x_train2 = changeToNumpy(x[1.4].src_files, 'tradFeature')
        y_train = changeToNumpy(x[1.4].src_files, 'label')
        # sampling to delete imbalance
        x1_res, x2_res, y_res = sampling(sampling_name, x_train1, x_train2, y_train)

        x_test1 = changeToNumpy(x[1.6].src_files, 'interVector')
        x_test2 = changeToNumpy(x[1.6].src_files, 'tradFeature')
        y_reality = changeToNumpy(x[1.6].src_files, 'label')
        m = cnn_model(x_train1, x_train2)
        print(1)
        m.fit([x1_res, x2_res], y_res, batch_size=32, epochs=15)

        y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)

        for src_id, y_real, y_pre in zip(x[1.6].src_files, y_reality, y_predict):
            data[src_id] = float(y_real),float(y_pre),int(0 if float(y_pre) < mark else 1)
        saveToCSV(data, 'camel', 1.6)


    elif (name == 'jedit'):
        parser = Parser(jedit)
        x = parser.Parser()
        x_train1 = changeToNumpy(x[4.0].src_files, 'interVector')
        x_train2 = changeToNumpy(x[4.0].src_files, 'tradFeature')
        y_train = changeToNumpy(x[4.0].src_files, 'label')

        # sampling to delete imbalance
        x1_res, x2_res, y_res = sampling(sampling_name, x_train1, x_train2, y_train)

        x_test1 = changeToNumpy(x[4.1].src_files, 'interVector')
        x_test2 = changeToNumpy(x[4.1].src_files, 'tradFeature')
        y_reality = changeToNumpy(x[4.1].src_files, 'label')

        m = cnn_model(x_train1, x_train2)
        m.fit([x1_res, x2_res], y_res, batch_size=32, epochs=15)

        y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
        for src_id, y_real, y_pre in zip(x[4.1].src_files, y_reality, y_predict):
            data[src_id] = float(y_real),float(y_pre),int(0 if float(y_pre) < mark else 1)

        saveToCSV(data, 'jedit', 4.1)

    elif (name == 'lucene'):
        parser = Parser(lucene)
        x = parser.Parser()
        x_train1 = changeToNumpy(x[2.0].src_files, 'interVector')
        x_train2 = changeToNumpy(x[2.0].src_files, 'tradFeature')
        y_train = changeToNumpy(x[2.0].src_files, 'label')

        # sampling to delete imbalance
        x1_res, x2_res, y_res = sampling(sampling_name, x_train1, x_train2, y_train)

        x_test1 = changeToNumpy(x[2.2].src_files, 'interVector')
        x_test2 = changeToNumpy(x[2.2].src_files, 'tradFeature')
        y_reality = changeToNumpy(x[2.2].src_files, 'label')
        m = cnn_model(x_train1, x_train2)
        m.fit([x1_res, x2_res], y_res, batch_size=32, epochs=15)

        y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
        for src_id, y_real, y_pre in zip(x[2.2].src_files, y_reality, y_predict):
            data[src_id] = float(y_real), float(y_pre), int(0 if float(y_pre) < mark else 1)

        saveToCSV(data, 'lucene', 2.2)
    elif (name == 'xalan'):
        parser = Parser(xalan)
        x = parser.Parser()
        x_train1 = changeToNumpy(x[2.5].src_files, 'interVector')
        x_train2 = changeToNumpy(x[2.5].src_files, 'tradFeature')
        y_train = changeToNumpy(x[2.5].src_files, 'label')

        # sampling to delete imbalance
        x1_res, x2_res, y_res = sampling(sampling_name, x_train1, x_train2, y_train)

        x_test1 = changeToNumpy(x[2.6].src_files, 'interVector')
        x_test2 = changeToNumpy(x[2.6].src_files, 'tradFeature')
        y_reality = changeToNumpy(x[2.6].src_files, 'label')
        m = cnn_model(x_train1, x_train2)
        m.fit([x1_res, x2_res], y_res, batch_size=32, epochs=15)

        y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
        for src_id, y_real, y_pre in zip(x[2.5].src_files, y_reality, y_predict):
            data[src_id] = float(y_real),float(y_pre),int(0 if float(y_pre) < mark else 1)

        saveToCSV(data, 'xalan', 2.6)
    elif (name == 'xerces'):
        parser = Parser(xerces)
        x = parser.Parser()
        x_train1 = changeToNumpy(x[1.2].src_files, 'interVector')
        x_train2 = changeToNumpy(x[1.2].src_files, 'tradFeature')
        y_train = changeToNumpy(x[1.2].src_files, 'label')

        # sampling to delete imbalance
        x1_res, x2_res, y_res = sampling(sampling_name, x_train1, x_train2, y_train)

        x_test1 = changeToNumpy(x[1.3].src_files, 'interVector')
        x_test2 = changeToNumpy(x[1.3].src_files, 'tradFeature')
        y_reality = changeToNumpy(x[1.3].src_files, 'label')
        m = cnn_model(x_train1, x_train2)
        m.fit([x1_res, x2_res], y_res, batch_size=32, epochs=15)

        y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
        for src_id, y_real, y_pre in zip(x[1.3].src_files, y_reality, y_predict):
            data[src_id] = float(y_real),float(y_pre),int(0 if float(y_pre) < mark else 1)

        saveToCSV(data, 'xerces', 1.3)
        y_test = m.predict([x_test1, x_test2], batch_size=32, verbose=1)

    elif (name == 'synapse'):
        parser = Parser(synapse)
        x = parser.Parser()
        x_train1 = changeToNumpy(x[1.1].src_files, 'interVector')
        x_train2 = changeToNumpy(x[1.1].src_files, 'tradFeature')
        y_train = changeToNumpy(x[1.1].src_files, 'label')

        # sampling to delete imbalance
        x1_res, x2_res, y_res = sampling(sampling_name, x_train1, x_train2, y_train)

        x_test1 = changeToNumpy(x[1.2].src_files, 'interVector')
        x_test2 = changeToNumpy(x[1.2].src_files, 'tradFeature')
        y_reality = changeToNumpy(x[1.2].src_files, 'label')
        m = cnn_model(x_train1, x_train2)
        m.fit([x1_res, x2_res], y_res, batch_size=32, epochs=15)

        y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
        for src_id, y_real, y_pre in zip(x[1.2].src_files, y_reality, y_predict):
            data[src_id] = float(y_real),float(y_pre),int(0 if float(y_pre) < mark else 1)

        saveToCSV(data, 'synapse', 1.2)

        y_test = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
    elif (name == 'poi'):
        parser = Parser(poi)
        x = parser.Parser()
        x_train1 = changeToNumpy(x[2.5].src_files, 'interVector')
        x_train2 = changeToNumpy(x[2.5].src_files, 'tradFeature')
        y_train = changeToNumpy(x[2.5].src_files, 'label')

        # sampling to delete imbalance
        x1_res, x2_res, y_res = sampling(sampling_name, x_train1, x_train2, y_train)

        x_test1 = changeToNumpy(x[3.0].src_files, 'interVector')
        x_test2 = changeToNumpy(x[3.0].src_files, 'tradFeature')
        y_reality = changeToNumpy(x[3.0].src_files, 'label')
        m = cnn_model(x_train1, x_train2)
        m.fit([x1_res, x2_res], y_res, batch_size=32, epochs=15)

        y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
        for src_id, y_real, y_pre in zip(x[3.0].src_files, y_reality, y_predict):
            data[src_id] = float(y_real),float(y_pre),int(0 if float(y_pre) < mark else 1)

        saveToCSV(data, 'poi', 3.0)



if __name__ == '__main__':
    # DP-CNN use SMOTE, BorderlineSMOTE, RandomOverSampler, ADASYN, SVMSMOTE for oversampling
    # DP-CNN use NearMiss, NCR, RandomUnderSampler, CNN, TomekLinks, ENN, OSS for unsersampling
    # DP-CNN use camel, jEdit, lucene, xalan, xerces, synapse, poi
    sampling_name = 'OSS'
    predict('camel', sampling_name)
    predict('jedit', sampling_name)
    predict('lucene', sampling_name)
    predict('xalan', sampling_name)
    predict('xerces', sampling_name)
    predict('synapse', sampling_name)
    predict('poi', sampling_name)