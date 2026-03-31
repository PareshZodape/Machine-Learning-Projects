# Import all the dependencies 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer  # to convert text data into numerical format
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Data Collection And Preprocessing 

data = 'D:\DS Projects\ML Projects\Spam mail prediction\mail_data.csv'

df = pd.read_csv(data)

print(df)

# drop the missing values
df.dropna()

df.head(5)
df.shape

# Label encoding
# - spam = 1
# - ham = 0


# Label spam mail as 0 and ham mail as 1
df.loc[df['Category'] == 'spam', 'Category', ] = 1
df.loc[df['Category'] == 'ham', 'Category' , ]= 0

print(df)

X = df['Message']
y = df['Category']

print(X)
print(y)

# Splitting the Data Into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3 )

# Feature Extraction
# Convert Text into numbers

# transform the text data to feature vector that can be used as input to the logistic regression
feature_ext = TfidfVectorizer(min_df = 1 , stop_words='english', lowercase = True)

X_train_features = feature_ext.fit_transform(X_train)
X_test_features = feature_ext.transform(X_test)


# convert y_train and y_test values as integers
y_train = y_train.astype('int')
y_test = y_test.astype('int')

print(X_train_features)
print(X_test_features)



#Training Model

models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "DecisionTree": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier()
}

models.fit(X_train_features, y_train)

# Model Evaluation on Training data
# prediction on training data
training_pred = models.predict(X_train_features)
training_acc = accuracy_score(y_train, training_pred)

print("Accuracy Score is : ", training_acc)

# Model Evaluation on testing data
# Prediction on testing data

testing_pred = models.predict(X_test_features)
testing_acc = accuracy_score(y_test, testing_pred)

print("The accuracy score is : ", testing_acc)

# # Building a Predictive System

# input_mail = ["URGENT! You have won a 1 week FREE membership in our Â£100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18"]

# # convert text to feature vectors
# input_data_features = feature_ext.transform(input_mail)

# # making prediction

# prediction = models.predict(input_data_features)
# print(prediction)

# if (prediction[0]==0):
#   print('Ham mail')

# else:
#   print('Spam mail')


import pickle

# Save model
pickle.dump(models, open("model.pkl", "wb"))

# Save vectorizer
pickle.dump(feature_ext, open("vectorizer.pkl", "wb"))

print("Model and Vectorizer saved successfully!")