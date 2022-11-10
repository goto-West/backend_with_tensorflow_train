import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# df = pd.read_csv("Dataset/pose_angles.csv")
df = pd.read_csv("pose_angles_2.csv")

df = df.drop('num', axis = 1)

# get X, y
X = df.values[:, :-1]
y = df.values[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# class probability p(Ck)
gnb.class_prior_
# mean of each feature per class for p(x|Ck)
gnb.theta_
# variance of each feature per class for p(x|Ck)
# gnb.sigma_
gnb.var_
# predict class of X_test[10] ~ X_test[14]
gnb.predict(X_test[10:16])
# predict class probabilty of X_test[10] ~ X_test[14]
gnb.predict_proba(X_test[10:16])

# Compute train accuracy
acc = gnb.score(X_train, y_train)
# Compute test accuracy
acc = gnb.score(X_test, y_test)

import joblib
filename = '221105NBC_2.pkl'
joblib.dump(gnb, filename)