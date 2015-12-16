"""
Author: Esteban Cairol
Text classifier. Binary sentiment text analysis for Amazon's computer reviews
"""

import sys
import os
import random
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm

from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix

# from sklearn.model_selection import GridSearchCV
# from sklearn.datasets import load_files


path = 'data'
files = os.listdir(path)
perc_train = 0.8

# Randomize files
random.shuffle(files)

samples = []
labels = []

for file_name in files:
    if file_name.endswith(".txt"):
    	test = file_name
    	file = open(os.path.join(path, file_name) ,'r')
    	samples.append(file.read())
    	labels.append(file.name[5]) # remove 'data\' from string
    	file.close()

n_samples = len(samples)
index_split = int(perc_train*n_samples)

print "Total samples read: {}".format(n_samples)

train_samples = samples[0:index_split]
train_labels = labels[0:index_split]

perc_test = 100-perc_train
test_samples = samples[index_split+1:n_samples]
test_labels = labels[index_split+1:n_samples]

text_clf = Pipeline([
	('vect', TfidfVectorizer(max_df = 0.8,sublinear_tf=True,use_idf=True)),
	('clf', svm.LinearSVC(C=1.0)),
])


print "Starting fit process..."
text_clf.fit(train_samples, train_labels)

print "Starting prediction..."
predicted = text_clf.predict(test_samples)


# Calculate Accuracy
print "Calculating accuracy..."
accuracy = text_clf.score(test_samples, test_labels)
print "Accuracy {}".format(accuracy)

# Confusion Matrix Analysis
print "Building confusion matrix..."
conf = confusion_matrix(test_labels, predicted)
print "Confusion Matrix \n {}".format(conf)
plt.imshow(conf, cmap='binary', interpolation='None')


# Manual test
def manualPredict(review):
    prediction = text_clf.predict([review])
    print prediction
    userReview = raw_input('Enter another Amazon review: ')
    manualPredict(userReview)
    pass

userReview = raw_input('Enter an Amazon review: ')
manualPredict(userReview)


"""
Developer Notes
------------------------------------------------------------------------------------
 - The original idea was to use not only Positive and Negative labels, but also Neutral label representing 3-star reviews. However I learned that this increases 
   the noise and confusion, so I decided to keep only 2 classes: positive (2) or negative (0)
 - I first started using MultinomialNB() classifier, but svm.LinearSVC() gives a better accuracy at a similar cost
 - svm.LinearSVC() process data faster than svm.SVC(kernel='linear')
 - On TfidfVectorizer(), max_df = 0.8 words appering in more than 80% of the documents
 - TfidfVectorizer() is being used as both, Vectorizes and Transformer (instead of CountVectorizer and then TfidfTransformer)
------------------------------------------------------------------------------------
"""