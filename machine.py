"""
Author: Esteban Cairol
Text classifier.
"""
import sys
import os
import random
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn import metrics

path = 'data'
files = os.listdir(path)
perc_train = 80

# Randomize files
random.shuffle(files)

samples = []
labels = []

for file_name in files:
    if file_name.endswith(".txt"):
    	test = file_name
    	file = open(os.path.join(path, file_name) ,'r')
    	samples.append(file.read())
    	labels.append(file.name[5]) # TODO: remove 'data\' from string
    	file.close()

n_samples = len(samples)
print "Total samples read: {}".format(n_samples)

train_samples = samples[0:(perc_train*n_samples)]
train_labels = labels[0:(perc_train*n_samples)]

perc_test = 100-perc_train
test_samples = samples[0:(perc_test*n_samples)]
test_labels = labels[0:(perc_test*n_samples)]

text_clf = Pipeline([
	('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()), 
])

text_clf.fit(train_samples, train_labels)

# test_samples = [
# 	'I have had a pleasant experience with my HP Chromebook 14 these past few days. Its really good for multitasking.',
# 	'It is very easy to set up, simply choose wifi network and sign in into your google account.',
# 	'Stay out of it, is very slow',
# 	'I just decided to return this. While I initially felt the build quality was pretty good, I encountered two problems',
# ]

predicted = text_clf.predict(test_samples)
accuracy = text_clf.score(test_samples, test_labels)

print "Accuracy {}".format(accuracy)
