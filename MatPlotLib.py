from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import scale
from sklearn.metrics.pairwise import cosine_similarity
import connection as Project
import pandas as pd
from nltk.tokenize import sent_tokenize,word_tokenize
from sklearn import datasets
# from matplotlib import style
# style.use('ggplot')
import nltk
'''x = [1,3,5,7,9]
y = [5,2,7,8,2]
x1 = [2,4,6,8,10]
y1 = [8,6,2,5,6]
population_ages = [20,3,0,5,6,8,90,34,56,78,12,34,52,67,45,34]
bins = [10,20,30,40,50,60,70]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.scatter(x,y,label='skitscat',color='g')
plt.scatter(x1,y1,label='skitscat1',color='y')
#plt.bar(x1,y1,label='BAR 2',color='y')
plt.title('Histogram')
plt.xlabel('Bins')
plt.ylabel("Ages")
plt.legend()
# plt.grid(True,color='k')
plt.show()'''
#array = np.array([[1,2],[3,2.5],[5,6],[7,8],[3.5,8.7],[3.5,4.3]])
'''print(array[:,0])
print(array[:,1])

plt.scatter(array[:,0],array[:,1],s=150,color='black')
plt.show()
corpus = ['I love my cat',
          'cat is beautiful',
          'computer is good to learn'
          ,'i am learning computer']
cluster_number = 2
kmean = KMeans(n_clusters=cluster_number)
kmean.fit(array)
centroids = kmean.cluster_centers_
labels = kmean.labels_
colors = ['r.','g.']
plt.figure()
for x in range(len(array)):
    plt.plot(array[x,0],array[x,1],colors[labels[x]],markersize=10)
plt.scatter(centroids[:,0],centroids[:,1],marker='*',s=70,linewidths=1)
plt.show()'''

'''corpus = ['I love my cat',
          'cat is beautiful',
          'computer is good to learn'
          ,'i am learning computer']
wordToVec = CountVectorizer(stop_words='english')
z = wordToVec.fit_transform(corpus)
print(z.todense())
vocab = wordToVec.get_feature_names()
print(vocab)

tf = TfidfVectorizer(stop_words='english')
x = tf.fit_transform(corpus)
print(x.todense())
dist = 1 - cosine_similarity(x)
model = KMeans(n_clusters=2)
model.fit(x)
print(dist)
print("TOp Terms per cLuster: \n")
order_centroids = model.cluster_centers_.argsort()[:,::-1]
terms = tf.get_feature_names()
for i in range(2):
    print("Cluster %i" %i,end='')
    for ind in order_centroids[i,:3]:
        print(" %s ," % terms[ind],end='')
    print(" ")'''
'''plt.figure(figsize=(5,5))
data_set = Project.GetValuesFromDatabase()
data_pandas = pd.DataFrame(data_set)
data_pandas.columns=['Description','Newspaper']
 print(data_pandas)
my_values_of_description = ['My name is aleem','aleem is a good boy','caste of aleem is awan']
vectorizer =CountVectorizer(analyzer='word',stop_words='english',tokenizer=word_tokenize,token_pattern="[/w-]+")
X = vectorizer.fit_transform(my_values_of_description[:])
print(X.toarray())
X_names = vectorizer.get_feature_names()
print(X_names)
print(data_pandas.index)
print(data_pandas.columns)
simil = 1-cosine_similarity(X.toarray())
print(simil)
model = KMeans(n_clusters=2)
model.fit(X)
color_theme = np.array(['darkgrey', 'lightsalmon', 'powderblue'])
centroids = model.cluster_centers_
print(centroids)
print(X.shape[0])
for i in range(X.shape[0]):
    plt.plot(X[i,0],X[i,1],color_theme[model.labels_[i]],markersize=10)
plt.scatter(centroids[:,0],centroids[:,1],marker='*',s=70,linewidths=1)
plt.show()'''

'''count_vect = CountVectorizer(lowercase=True,stop_words='english',min_df=2)
x_countVect = count_vect.fit_transform(data_set)
names =count_vect.get_feature_names()
pd_Data = pd.DataFrame(x_countVect.toarray(),columns=names)
print(pd_Data.head())'''
#Count_Vect = TfidfVectorizer(stop_words='english')
#y_Count_Vect = Count_Vect.fit_transform(data_set)
#y_names = Count_Vect.get_feature_names()
#pd_Data_Freq = pd.DataFrame(y_Count_Vect.toarray(),columns=y_names)
#print(pd_Data_Freq.head())
#print(data_set)
#print(len(data_set))'''
'''word_to_vec =CountVectorizer(stop_words='english')
z = word_to_vec.fit_transform(data_set)
print(z.todense())
terms = word_to_vec.get_feature_names()
print(terms)
print(len(terms))'''

'''tf = TfidfVectorizer(stop_words='english')
x = tf.fit_transform(data_set)
print(type(x))
print(x)
#print(x.todense()[0])
dist = 1 - cosine_similarity(x)
model = KMeans(n_clusters=2)
model.fit(dist)
print(dist)
print("TOp Terms per cLuster: \n")
order_centroids = model.cluster_centers_.argsort()[:,::-1]
terms = tf.get_feature_names()
for i in range(2):
    print("Cluster %i" %i,end='')
    for ind in order_centroids[i,:3]:
        print(" %s ," % terms[ind],end='')
    print(" ")
cluster_number = 2
kmean = KMeans(n_clusters=cluster_number)
kmean.fit(dist)
print("These are Centroids")
centroids = kmean.cluster_centers_
print(centroids)
labels = kmean.labels_
print("Thers eare Labels \n")
print(labels)
colors = ['r.','g.']
plt.figure()
print(x.shape)
print(dist[0])
for i in range(x.shape[0]):
    plt.plot(x[i,0],x[i,1],colors[labels[i]],markersize=10)
plt.scatter(centroids[:,0],centroids[:,1],marker='*',s=70,linewidths=1)
plt.show()''''''
iris = datasets.load_iris()
X = scale(iris.data)
Y = pd.DataFrame(iris.target)
variable_names = iris.feature_names
cluster = KMeans(n_clusters=3,random_state=5)
cluster.fit(X)
iris_df = pd.DataFrame(iris.data)
import sklearn
iris_df.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
Y.columns = ['Targets']
color_theme = np.array(['darkgrey','lightsalmon','powderblue'])
plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width,c=color_theme[iris.target],s=50)
plt.title("HEy THis is")
plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width,c=color_theme[cluster.labels_],s=50)
plt.title("HEy THis is 2")
plt.show()'''


'''corpus = {
 'a' : "Mr. Green killed Colonel Mustard in the study with the candlestick. \
Mr. Green is not a very nice fellow.",
 'b' : "Professor Plum has a green plant in his study.",
 'c' : "Miss Scarlett watered Professor Plum's green plant while he was away \
from his office last week."
}'''

data_set = Project.GetValuesFromDatabase()
aray = np.array(data_set)
#print(aray)
pd_Data_Set = pd.DataFrame(data_set,columns=['Description','Newspaper'])
def GetCorpus():
    dict_vlues = pd_Data_Set.to_dict('records')
    corpus = {}
    count = 0
    for x in dict_vlues:
        corpus.update({"%s"%str(count):"%s"%x["Description"]})
        count = count+1
    return corpus
'''corpus ={
    'a':"Aleem is a good boy",
    'b':"Good thing to meet you ",
    'c':"aleem is working good"
}'''
corpus = GetCorpus()
'''terms = {
 'a' : [i.lower() for i in corpus['a'].split() ],
 'b' : [i.lower() for i in corpus['b'].split() ],
 'c' : [i.lower() for i in corpus['c'].split() ]
 }'''

from math import log

# XXX: Enter in a query term from the corpus variable
QUERY_TERMS = ['Pakistan','Kashmir','US',"Afghanistan"]

def tf(term, doc, normalize=True):
    doc = doc.lower().split()
    if normalize:
        return doc.count(term.lower()) / float(len(doc))
    else:
        return doc.count(term.lower()) / 1.0

def idf(term, corpus):
    num_texts_with_term = len([True for text in corpus if term.lower()
                               in text.lower().split()])

    # tf-idf calc involves multiplying against a tf value less than 0, so it's
    # necessary to return a value greater than 1 for consistent scoring.
    # (Multiplying two values less than 1 returns a value less than each of
    # them.)

    try:
        return 1.0 + log(float(len(corpus)) / num_texts_with_term)
    except ZeroDivisionError:
        return 1.0


def tf_idf(term, doc, corpus):
    return tf(term, doc) * idf(term, corpus)

'''corpus = \
    {'a': 'Mr. Green killed Colonel Mustard in the study with the candlestick. \
Mr. Green is not a very nice fellow.',
     'b': 'Professor Plum has a green plant study in his study.',
     'c': "Miss Scarlett watered Professor study Plum's green plant while he was away \
from his office last week."}'''

for (k, v) in sorted(corpus.items()):
    print(k, ':', v)

# Score queries by calculating cumulative tf_idf score for each term in query
def GetQueryScores():
    query_scores = {}
    for (k,v) in corpus.items():
        query_scores.update({k:0})
    return query_scores
query_scores = GetQueryScores()
for term in [t.lower() for t in QUERY_TERMS]:
    for doc in sorted(corpus):
        print
        'TF(%s): %s' % (doc, term), tf(term, corpus[doc])
    print
    'IDF: %s' % (term,), idf(term, corpus.values())
    print

    for doc in sorted(corpus):
        score = tf_idf(term, corpus[doc], corpus.values())
        print
        'TF-IDF(%s): %s' % (doc, term), score
        query_scores[doc] += score
    print
append_doc=[]
print("Overall TF-IDF scores for query '%s'" % (' '.join(QUERY_TERMS),))
for (doc, score) in sorted(query_scores.items()):
    if score <= 0.0:
        continue
        #print(doc + " : " + str(score))
    else:
        append_doc.append(doc)
# print(append_doc)
# print(len(pd_Data_Set))
def GetValuesForDisplay(values):
    dict_vlues = pd_Data_Set.to_dict('records')
    list = []
    count = 0
    # print(dict_vlues)
    for x in dict_vlues:
        for val in values:
            # print(count == int(val))
            if int(val) != count:
                 continue
            else:
                list.append([x["Description"], x["Newspaper"]])
        count = count + 1
    return list
array_of_Selected_Terms =np.array(GetValuesForDisplay(append_doc))
print(array_of_Selected_Terms[:,0])