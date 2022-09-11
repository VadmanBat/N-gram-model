import re
import random
import pickle
import argparse


class Generate:
    words = []
    words_num, links = {}, {}

    def __init__(self):
        model = open(args.model, 'rb')
        self.words = pickle.load(model)
        self.words_num = pickle.load(model)
        self.links = pickle.load(model)

    def generate(self):
        text = args.prefix
        if text:
            text = re.sub('[^a-zа-яё]', ' ', text.lower()).split()
        else:
            text = [random.choice(self.words)]
        if len(text) == 1:
            text.append(self.words[random.choice(self.links[self.words_num[text[0]]])])
        if not (self.words_num[text[-2]], self.words_num[text[-1]]) in self.words_num:
            text.append(self.words[random.choice(self.links[self.words_num[text[-1]]])])
        for word in text:
            print(word, end=' ')
        word_ind_1, word_ind_2 = self.words_num[text[-2]], self.words_num[text[-1]]
        for i in range(len(text), args.length):
            word_ind_3 = random.choice(self.links[(word_ind_1, word_ind_2)])
            print(self.words[word_ind_3], end=' ')
            word_ind_1, word_ind_2 = word_ind_2, word_ind_3


parser = argparse.ArgumentParser(description="Generate text of desired length")
parser.add_argument("-m", "--model", type=str, metavar='', required=True, help="path to the file from which the model is loaded")
parser.add_argument("-p", "--prefix", type=str, metavar='', help="optional argument. Beginning of a sentence (one or more words)")
parser.add_argument("-l", "--length", type=int, metavar='', required=True, help="length of generated sequence")
args = parser.parse_args()

generate = Generate()
generate.generate()
