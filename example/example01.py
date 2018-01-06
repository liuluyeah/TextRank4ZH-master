#-*- encoding:utf-8 -*-
from __future__ import print_function

import sys,importlib
try:
    importlib.reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

stopwords = codecs.open('../test/doc/stopwords.txt','r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]

text = codecs.open('../test/doc/hua.txt', 'r', 'utf-8').read()
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

print( '关键词：' )
to_print=""
for item in tr4w.get_keywords(10, word_min_len=2):
    if item.word not in stopwords:
        to_print+=item.word+' '
        print(item.word, item.weight)
print(to_print)
# print()
# print( '关键短语：' )
# for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
#     print(phrase)
#
# tr4s = TextRank4Sentence()
# tr4s.analyze(text=text, lower=True, source = 'all_filters')
#
# print()
# print( '摘要：' )
# for item in tr4s.get_key_sentences(num=3):
#     print(item.index, item.weight, item.sentence)