import os
import csv
import nltk
import re
import string
import numpy as np
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer


def number_of_letters(doc):  # includes punctuation
    return (len(doc))


def number_of_punctuation(doc):
    punctuation = string.punctuation
    n = 0
    for l in doc:
        if l in punctuation:
            n += 1
    return (n)


def number_of_letters_np(doc):  # no punctuation
    return (number_of_letters(doc) - number_of_punctuation(doc))


def number_of_sentences(doc):
    return (len(sent_tokenize(doc)))


def number_of_words(doc):  # includes punctuation
    return (len(word_tokenize(doc)))


def number_of_words_np(doc):  # no punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    return (len(tokenizer.tokenize(doc)))


def word_occurence(doc, word):
    number_of_occurences = doc.count(word)
    return (number_of_occurences)


def words_per_sentence(doc):  # average number of words per sentence (includes puncutation)
    return (number_of_words(doc) / number_of_sentences(doc))


def words_per_sentence_np(doc):  # average number of words per sentence (no punctuation)
    return (number_of_words_np(doc) / number_of_sentences(doc))


def punctuation_per_sentence(doc):
    return (number_of_punctuation(doc) / number_of_sentences(doc))


def average_word_length(doc):
    return (number_of_letters(doc) / number_of_words(
        doc))  # including punctuation, so this one is not relevant because for punctuation 1 word = 1 letter


def average_word_length_np(doc):
    return (number_of_letters_np(doc) / number_of_words_np(doc))


def egocentricity_level(doc):  # can work as a kind of "score" ? (it's a frequency)
    n = 0
    ego_list = ["me", "Me", "myself", "Myself", "I", "mine", "Mine", "my", "My"]
    for w in word_tokenize(doc):
        for item in ego_list:
            if w == item:
                n += 1
    return (n / number_of_words_np(doc))


def modal_verbs_frequency(doc):
    modal_list = ["can", "could", "could have", "must", "need", "must have", "may", "might", "would", "would have",
                  "shall", "need", "have to", "ought to", "dare", "should", "should have", "will be able to", "forced",
                  "will have to", "allowed", "Can", "Could", "Could have", "Must", "Need", "Must have", "May", "Might",
                  "Would", "Would have", "Shall", "Need", "Have to", "Ought to", "Dare", "Should", "Should have",
                  "Will be able to", "Forced", "Will have to", "Allowed"]
    n = 0
    for w in doc:
        for item in modal_list:
            if w == item:
                n += 1
    return (n / number_of_words_np(doc))


def connector_frequency(doc):  # checker si y'a moyen de trouver + de mots
    connector_frequency_list = []
    emphasis = comparison = contrast = addition = illustration = 0
    emphasis_list = ["Especially", "Also", "In particular", "Furthermore", "In addition", "Indeed", "Of course",
                     "Certainly", "Above all", "Specifically", "Significantly", "Notably"]
    emphasis_list2 = []
    comparison_list = ["As if", "As", "Equally", "Similarly", "In the same way", "Comparable", "In like manner",
                       "Alternatively", "Unless", "Despite this", "By the way"]
    comparison_list2 = []
    contrast_list = ["But", "However", "On the other hand", "Otherwise", "Unlike", "Conversely", "At the same time",
                     "In spite of", "Whereas", "While", "Yet", "Apart from"]
    contrast_list2 = []
    addition_list = ["As well as", "Further", "Furthermore", "And then", "And", "Too", "Also", "In addition to",
                     "Not only", "Or"]
    addition_list2 = []
    illustration_list = ["Such as", "In this case", "For one thing", "For instance", "For example", "In the case of",
                         "Illustrated by", "As an example", "As instance", "In other words"]
    illustration_list2 = []
    for item in emphasis_list:
        emphasis_list2.append(item.lower())
    emphasis_list.extend(comparison_list2)
    for item in comparison_list:
        comparison_list2.append(item.lower())
    comparison_list.extend(comparison_list2)
    for item in contrast_list:
        contrast_list2.append(item.lower())
    contrast_list.extend(contrast_list2)
    for item in addition_list:
        addition_list2.append(item.lower())
    addition_list.extend(addition_list2)
    for item in illustration_list:
        illustration_list2.append(item.lower())
    illustration_list.extend(illustration_list2)
    for w in word_tokenize(doc):

        if w in emphasis_list:
            emphasis += 1
        if w in comparison_list:
            comparison += 1
        if w in contrast_list:
            contrast += 1
        if w in addition_list:
            addition += 1
        if w in illustration_list:
            illustration += 1
    connector_frequency_list.append(emphasis / number_of_words_np(doc))
    connector_frequency_list.append(comparison / number_of_words_np(doc))
    connector_frequency_list.append(contrast / number_of_words_np(doc))
    connector_frequency_list.append(addition / number_of_words_np(doc))
    connector_frequency_list.append(illustration / number_of_words_np(doc))
    return (connector_frequency_list)


def type_of_punctuation(doc):
    """"""


def average_word_length(doc):
    """"""


def pos_tag_frequency(doc):  # copier le truc de tagging de Seweryn
    """"""


with open("/home/macaire/Bureau/nlpproject/texts_by_sentences/processedbysentences_Bacon_essays.txt", "r") as document:
    doc = document.read()
    print(number_of_letters(doc))
