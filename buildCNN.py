
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding, Dropout, Concatenate
from keras.models import Model
from tensorflow.keras import layers
from keras import initializers
import tensorflow as tf

import numpy as np


from changeTypeData import *
from SourceFileToVector import *
from datasets import *

def cnn_model(inter_matrix, trad_feature):
    A1 = Input(shape = (inter_matrix.shape[1]))
    AA1 = Input(shape = (trad_feature.shape[1]))

    A2 = Embedding(input_dim=7000, output_dim=30)(A1)

    A3 = Conv1D(filters=10, kernel_size=5, activation='relu')(A2)
    A4 = MaxPooling1D(pool_size=5, strides=5, padding='valid')(A3)

    A5 = Dense(100, activation='relu')(A4)

    A6 = Conv1D(filters=10, kernel_size=5, activation='relu')(A5)
    A7 = MaxPooling1D(pool_size=5, strides=5, padding='valid')(A6)

    A8 = Flatten()(A7)

    A9 = Concatenate()([A8, AA1])

    A10 = Dense(100, activation= 'relu', )(A9)

    A11 = Dense(1, activation= 'sigmoid')(A10)

    model = Model(inputs = [A1, AA1], outputs = A11)
    model.compile(optimizer='adam', loss='binary_crossentropy')

    return model





def test():
    # batch size is set as 32, the training epoch is 15,
    # and the embedding dimension is set as 30
    parser = Parser(jedit)
    x = parser.Parser()
    x_train1 = changeToNumpy(x[4.0].src_files, 'interVector')
    x_train2 = changeToNumpy(x[4.0].src_files, 'tradFeature')
    y_train = changeToNumpy(x[4.0].src_files, 'label')
    print(x_train1)
    print(x_train2)
    x_test1 = changeToNumpy(x[4.1].src_files, 'interVector')
    x_test2 = changeToNumpy(x[4.1].src_files, 'tradFeature')
    y_reality = changeToNumpy(x[4.1].src_files, 'label')

    print(x_train1.shape, x_train2.shape, x_test1.shape, x_test2.shape)

    m = cnn_model(x_train1,x_train2)
    print(m.summary())
    m.fit([x_train1, x_train2], y_train, batch_size=32, epochs=15)

    y_predict = m.predict([x_test1, x_test2], batch_size=32, verbose=1)
    print(y_predict)

if __name__ == "__main__":
    test()