import nltk
import re
import numpy as np
from nltk.corpus import gutenberg
from nltk.corpus import wordnet as wrdNet
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.regexp import RegexpStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")
'''print(type(text1))
print(len(text1))
print(len(text4))
print(len(set(text1)))
print(text1[:10])
print(text4[:5])'''

'''print(gutenberg.fileids())
book = gutenberg.words('austen-persuasion.txt')
print(len(book))
book2 = gutenberg.words('austen-emma.txt')
print(len(book2))
book_sentences = gutenberg.sents('austen-emma.txt')
print(len(book_sentences))
print(book_sentences[20])'''
'''text = "Aleem is my name and he be the one and one and one "
print(text)
print(text.count('Aleem'))
vocab = nltk.FreqDist(text)
print(len(vocab))
print(vocab.most_common(5))'''
'''word = wrdNet.synsets("intense")[0]
print(word.name() + " : " + word.definition())
print(word.examples()
strings = "Hello ,he is doing  a job for us. Our  working procedures with 'punctuation',he said,'he is beautiful'"
print(punctuation)
with_out_punc = [w for w in strings if w not in punctuation]
print(with_out_punc)
sw = stopwords.words('english')
print(sw)
words_with_out_stopwords = [s for s in strings.split() if s not in sw ]
print("without",words_with_out_stopwords)

print(len(strings))
print(len(with_out_punc))
print(len(words_with_out_stopwords))

token_words = word_tokenize(strings)
print(token_words)
sentences_in_strings = sent_tokenize(strings)
print(sentences_in_strings)
st = PorterStemmer()
lm = WordNetLemmatizer()
for words in token_words:
    print(words + " : "+ st.stem(words))
for words in token_words:
    print(words + " : "+lm.lemmatize(words))
print(nltk.pos_tag(token_words,tagset='universal')'''
strings = """My name is aleem. I study in CS department.I like green color.Hurrah! we have won the match.
Just watching the match on television is not enough so I would like to get to the point that is necessary for me.
These things that are happening are not good for me.While Iam getting risks."""
'''sentences = sent_tokenize(strings)
print(sentences)
#tokens = [word_tokenize(s) for s in sentences]
#print(tokens)
#pos_tagged_tokens = [nltk.pos_tag(t,tagset='universal') for t in tokens]
#print(pos_tagged_tokens)

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
print(tokenizer.tokenize(strings))

tokens = tokenizer.tokenize(strings)
stop = stopwords.words('english')
with_out_stop_words = [item for item in tokens if item not in stop]
print(with_out_stop_words)'''
'''word = "rifle"
synsets = wrdNet.synsets(word)
print(synsets[0].pos())
# Generating Synonyms and antonyms lists
word = "move"
synsets_of_word = wrdNet.synsets(word)
print(synsets_of_word)'''
# print(synsets_of_word[0].lemmas()[0].name())
'''synonyms_array = []
antonyms_array = []
for word in synsets_of_word:
    for lem in word.lemmas():
        synonyms_array.append(lem.name())
        for ant in lem.antonyms():
            antonyms_array.append(ant.name())
''''''print(set(synonyms_array))
print(set(antonyms_array))
lstem = LancasterStemmer()
pstem = PorterStemmer()
restem = RegexpStemmer('ing')
print(lstem.stem('crawler')+" : "+pstem.stem('crawler')+" : "+restem.stem('crawling'))
'''
'''lzr = WordNetLemmatizer()
print(lzr.lemmatize('busy'))
print(lzr.lemmatize('dances',pos='v'))

from Replacer import RegexReplacer
regex = RegexReplacer()
result = regex.ReplaceMethod("I'd do this.I'm working. I've a pet. I'll do. ")
print(result)
array = np.array([1,2,34,5,56])
print(array.shape)
print(array.size)
print(type(array[0]))
array1 = np.zeros(3)
print(array1)
array2 = np.ones(5)
print(array2)
print(array[0:2])
print(array[-1])
print(array[2:])
print(array[2:]*2)
print(array[:])
print(array+[2])
print(array > 3)
print(array[array<7])
print(np.array(2,10,4))'''

'''word = 'pass'
synsets_of_word = wrdNet.synsets(word)
synonyms_array = []
antonyms_array = []
for word in synsets_of_word:
    for lem in word.lemmas():
        synonyms_array.append(lem.name())
        for ant in lem.antonyms():
            antonyms_array.append(ant.name())
print(set(synonyms_array))
print(set(antonyms_array))'''