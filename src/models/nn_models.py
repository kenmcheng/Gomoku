import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow.python.keras import Model, Input
from tensorflow.python.keras.layers import Dense, Dropout, Embedding, LeakyReLU

from tensorflow.python.keras.layers import LSTM, Conv1D, GlobalMaxPool1D
from keras.layers import Bidirectional

def print_tf_info():
   print(f'Tensorflow version: {tf.__version__}') 

class base_model:

    def train():
        pass

class ann_model():
    
    def __init__(self, layers, num_inputs, num_outputs = 1):
        self.layers = layers
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

    def build(self):
        inputs = Input(shape=(self.num_inputs,), dtype='int32')
        x = inputs
        
        for n_neurons in self.layers:
            x = Dense(n_neurons, activation=LeakyReLU(alpha=0.01))(x)
        
        outputs = Dense(self.num_outputs, activation="sigmoid")(x)
        model = Model(inputs=inputs, outputs=outputs)
        return model


class lstm_model():

    def __init__(self, layers, num_inputs, num_outputs) -> None:
        self.embedding_len = 500
        self.layer = layers
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

    def build(self):
        inputs = Input(shape=(self.num_inputs,))
        x = inputs
        x = Embedding(input_dim=self.num_inputs,
                     output_dim=self.embedding_len)(x)
        x = Bidirectional(LSTM(64)(x))
        x = Dense(16)(x)
        x = Dropout(0.4)(x)
        outputs = Dense(self.num_outputs, activation='sigmoid')
        model = Model(inputs=inputs, outputs=outputs)

        return model
        
def model_factory(model_type):
    if model_type == 'ann':
        return ann_model
    elif model_type == 'lstm':
        return lstm_model

    return ""

if __name__ == '__main__':
    print_tf_info()