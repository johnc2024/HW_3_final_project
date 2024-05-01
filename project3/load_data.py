import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action = 'ignore', category = Warning)

from tensorflow.keras.utils import to_categorical

def init(data):

    data_list = data['text'].tolist()
    return data_list
