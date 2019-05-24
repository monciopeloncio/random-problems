# encoding: utf-8

from requests import get
import constants as c
from nltk import download
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import csv
import argparse
import string

# Read script parameters
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nltk", help="Use nltk package",
                    action="store_true", default='0')
args = parser.parse_args()

def read_file(file_name):
    """ Returns a file readed from a path

        :param file_name: string
    """

    with open(c.FILES_DATA_PATH + file_name,'r') as f:
        file = f.read()
    return file

def save_dict(word_count_dict, file_name):
    """
        Write a dictionary into a file

        :param diword_count_dict: dict 
        :param file_name:string 
    """

    with open(c.FILE_RESULTS_PATH + file_name,'w+') as f:
        w = csv.writer(f)
        w.writerows(word_count_dict.items())

def nltk_process(file):
    """ Process a file using nltk functions and return a counter object

        :param file: string
        :return: Counter
    """
    tokenizer = RegexpTokenizer(r'\w+')
    file_tokenized = tokenizer.tokenize(file)
    word_count_dict = Counter(w.title() for w in file_tokenized if w.lower() not in stopwords.words())

    return word_count_dict

def normal_process(file):
    """ Process a file using string and Counter functions and return a counter object

        :return: Counter
    """

    # Remove special chars
    for char in string.punctuation + '\n':
        file = file.replace(char,' ')
        file = file.lower()

    file_tokenized = file.split()

    word_count_dict = Counter(w.title() for w in file_tokenized if w not in c.ENGLISH_STOP_WORDS)

    return word_count_dict

def word_count(file_name, use_nltk):
    """ Returns a word_count dictionary from a file. Depending on the use_nltk
        is possible to use nltk library for processing.

        :param file_name: string
        :param use_nltk: bool
    """
    file = read_file(file_name)

    word_count_dict = {}

    if use_nltk == True:
        print("NLTK processing for " + file_name)
        word_count_dict = nltk_process(file)
        file_name = 'nltk_' + file_name
    else:
        print("Normal processing for " + file_name)
        word_count_dict = normal_process(file)

    save_dict(word_count_dict, file_name)
    

if __name__ == "__main__":
    
    word_count("kinglear.txt", args.nltk)
    word_count("othello.txt", args.nltk)
    word_count("romeoandjuliet.txt", args.nltk)
