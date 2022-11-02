import numpy as np
import joblib as jl
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

filename = 'model_NBC.sav'

jl.dump(gnb, filename)
loaded_model = jl.load(filename)
result = loaded_model.score(X_test, Y_test)