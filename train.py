import os
import re
import pickle
import argparse


class Train:
    words = []
    words_num, links = {}, {}

    def fit(self, file_name):
        text = open(args.input_dir + '/' + file_name, encoding='utf-8').read().lower()
        text = re.sub('[^a-zа-яё]', ' ', text).split()
        for word in text:
            if word in self.words_num:
                continue
            self.words_num[word] = len(self.words)
            self.words.append(word)
        for i in range(1, len(text)):
            key = self.words_num[text[i - 1]]
            self.links.setdefault(key, []).append(self.words_num[text[i]])
        for i in range(2, len(text)):
            key = (self.words_num[text[i - 2]], self.words_num[text[i - 1]])
            self.links.setdefault(key, []).append(self.words_num[text[i]])

    def read_files(self):
        files = os.listdir(args.input_dir)
        for file in files:
            self.fit(file)

    def dump_model(self):
        model = open(args.model, 'wb')
        pickle.dump(self.words, model)
        pickle.dump(self.words_num, model)
        pickle.dump(self.links, model)


parser = argparse.ArgumentParser(description="Train Model for Text Generation")
parser.add_argument("-d", "--input-dir", type=str, metavar='', required=True, help="path to the directory containing the collection of documents")
parser.add_argument("-m", "--model", type=str, metavar='', required=True, help="path to the file where the model is saved")
args = parser.parse_args()

train = Train()
train.read_files()
train.dump_model()
