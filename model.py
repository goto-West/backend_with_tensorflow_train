import numpy as np
import joblib as jl
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.naive_bayes import GaussianNB
# from sklearn.model_selection import train_test_split

# https://github.com/goto-West/pose-classification/blob/main/csvPose.ipynb
# 경서 코드 리뷰하면서 predict 코드 작성하기
# interpreter  python 3.7.2


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# gnb = GaussianNB()
# gnb.fit(X_train, y_train)

# filename = 'model_NBC.sav'
filename = '221105NBC.json'
filename = '221105NBC_2.pkl'
loaded_model = jl.load(filename)

# result = loaded_model.predict([[160, 145, 176, 164, 112, 72, 176, 176]])
# print("it's working!")
# print(result)

def pose_classification () : 
    result = loaded_model.predict([[160, 145, 176, 164, 112, 72, 176, 176]])
    # print("it's working!")
    print(result)
    return result

