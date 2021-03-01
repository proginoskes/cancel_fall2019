import codecs, sys, json
from cfgen import GrammarModel
from random import seed

CORPUS_PATH = './cancel_tweets_clean.txt'
MODEL_ORDER = 2
my_model = GrammarModel(CORPUS_PATH, MODEL_ORDER)

seed(5)

for ii in range(3):
    print(my_model.make_sentence(do_markov=True))
