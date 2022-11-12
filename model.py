import sys
import numpy as np
import joblib as jl
import pandas as pd
import matplotlib.pyplot as plt

# interpreter  python 3.7.2

# filename = 'model_NBC.sav'
# filename = '221105NBC.json'
filename = '221105NBC_2.pkl'
loaded_model = jl.load(filename)

# load models, test and return result
def pose_classification (angles) :
    angles_p = [angles] # input is 2d array!! 
    # print(angles_p, type(angles_p))
    result = list(loaded_model.predict(angles_p))[0]
    return result

def main () :
    #get parameter
    ag = list(map(float, sys.argv[1:]))
    data = pose_classification(ag)
    # print("result : ", result, type(result))
    print(data)
    return data

if __name__ == "__main__" : 
    main()