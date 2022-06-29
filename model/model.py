import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.text import tokenizer_from_json
import logging

class Translate:
    def __init__(self, model_path):
        logging.info("Translate class initialized")
        self.model = load_model(model_path)
        logging.info("Model is loaded!")

    def predict(self, text):
        # frFile = open("fr_tokenizer.json", mode='r')
        # fr_data = json.load(frFile)
        # fr_tokenizer = tokenizer_from_json(fr_data)
        #
        # enFile = open("en_tokenizer.json", mode='r')
        # en_data = json.load(enFile)
        # en_tokenizer = tokenizer_from_json(en_data)

        # y_id_to_word = {value: key for key, value in fr_tokenizer.word_index.items()}
        # y_id_to_word[0] = '<PAD>'

        # sentence = en_tokenizer.texts_to_sequences([text])
        # # sentence = pad_sequences(sentence, maxlen=15, padding='post')
        # predictions = self.model.predict(sentence)

        # return ' '.join([y_id_to_word[np.argmax(x)] for x in predictions[0]])
        return "a"
