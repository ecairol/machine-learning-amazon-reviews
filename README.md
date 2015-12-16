# sklearn-amazon-reviews
Classify product reviews on Amazon into Positive or Negative labels

## Files

  - scrapper.py - the scrapper tool used to get the reviews from amazon. You can add more data by runnin `python scrapper.py`
  - machine.py - the code that implements the machine learning logic. Use `python machine.py` to run it using the data folder and also test it manually

## Data
The current data consists of 2500 reviews taken from Amazon, all of them are from laptops or tablets products.
Each review is stored into it's own .txt file. Files starting with 0 represent a negative review (1 or 2 stars) while files starting with 1 are positive reviews (4 or 5 stars)

## About
I'm starting to learn machine learning, so this was created as a first mini-project using Python's sklearn library.

The original idea was to use not only Positive and Negative labels, but also Neutral label representing 3-star reviews. However I learned that this increases the noise in data and confusion, so I decided to keep only 2 classes: positive (2) or negative (0)

I first started using `MultinomialNB()` classifier, but learned that `svm.LinearSVC()` gives a better accuracy at a similar cost. Also, `svm.LinearSVC()` seems to process data faster than `svm.SVC(kernel='linear')`. The default value of `C=1.0` gives a better accuracy than other values.

I initially used `CountVectorizer()` for tokenization and then `TfidfTransformer()` to leverage the importance of a word within a document in relationship to the collection of documents. However, after some research I ended up using one single function called `TfidfVectorizer()`