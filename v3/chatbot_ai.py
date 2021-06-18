#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import numpy
import tflearn
import tensorflow
import random
import json
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import word_tokenize


class chatbot_ai:
    def __init__(self, jsonFile):
        self.stemmer = LancasterStemmer()

        with open(jsonFile) as file:
            self.data = json.load(file)

        try:
            with open("v3/model/data.pickle", "rb") as f:
                self.words, self.labels, training, output = pickle.load(f)
        except Exception:
            self.words = []
            self.labels = []
            docs_x = []
            docs_y = []

            for intent in self.data['intents']:
                for pattern in intent['patterns']:
                    wrds = word_tokenize(pattern)
                    self.words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent['tag'])

                if intent['tag'] not in self.labels:
                    self.labels.append(intent['tag'])

            self.words = [self.stemmer.stem(w.lower()) for w in self.words]
            self.words = sorted(list(set(self.words)))

            self.labels = sorted(self.labels)

            training = []
            output = []

            out_empty = [0 for _ in range(len(self.labels))]

            for x, doc in enumerate(docs_x):
                bag = []
                wrds = [self.stemmer.stem(w.lower()) for w in doc]

                for w in self.words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)

                output_row = out_empty[:]
                output_row[self.labels.index(docs_y[x])] = 1

                training.append(bag)
                output.append(output_row)

            training = numpy.array(training)
            output = numpy.array(output)

            with open("v3/model/data.pickle", "wb") as f:
                pickle.dump((self.words, self.labels, training, output), f)

        tensorflow.compat.v1.reset_default_graph()

        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        self.model = tflearn.DNN(net)

        try:
            self.model.load("v3/model/model.tflearn")
        except Exception:
            self.model = tflearn.DNN(net)
            self.model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
            self.model.save("v3/model/model.tflearn")

    def bag_of_words(self):
        bag = [0 for _ in range(len(self.words))]

        s_words = word_tokenize(self.message)
        s_words = [self.stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(self.words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)

    def set_Message(self, message):
        self.message = str(message)

    def get_Response(self):
        results = self.model.predict([self.bag_of_words()])
        results_index = numpy.argmax(results)
        tag = self.labels[results_index]

        for tg in self.data['intents']:
            if tg['tag'] == tag:
                responses = tg['responses']

        return random.choice(responses)


if __name__ == "__main__":
    pass
