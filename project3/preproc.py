import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
import numpy as np
import string
import random
import re

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

def preprocessor(data):
    
   tokenizer = Tokenizer(num_words = 2000, oov_token = '<UNK>')
   tokenizer.fit_on_texts(data)
   sequences = tokenizer.texts_to_sequences(data)
   padded = pad_sequences(sequences, padding = 'post', truncating = 'post', maxlen = 40)
   
   return padded

def encoder(data): 

   le = LabelEncoder()

   enc = data
   enc['label'] = le.fit_transform(y_train_enc['label'])
   enc = to_categorical(y_train_enc)
   
   return enc