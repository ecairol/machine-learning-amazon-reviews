"""
Author: Esteban Cairol
Text classifier.
"""
import sys
import os
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
filelen = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
samples = [] # Use filelen to fix length of array
labels = []

# TODO: Randomize and take 20% for Test - Check Cross-Validation requirements
for file_name in os.listdir(path):
    if file_name.endswith(".txt"):
    	file = open(os.path.join(path, file_name) ,'r')
    	samples.append(file.read())
    	labels.append(file.name[5]) # TODO: remove 'data\' from string
    	file.close()


print("n_samples: %d" % len(samples))
print("n_labels: %d" % len(labels))
# print samples[2]

text_clf = Pipeline([
	('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()), 
])

text_clf.fit(samples, labels)

test_data = [
	'I have had a pleasant experience with my HP Chromebook 14 these past few days. Its really good for multitasking.',
	'It is very easy to set up, simply choose wifi network and sign in into your google account.',
	'Stay out of it, is very slow',
	'I just decided to return this. While I initially felt the build quality was pretty good, I encountered two problems',
]

predicted = text_clf.predict(test_data)
print predicted