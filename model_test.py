import sys
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# interpreter  python 3.7.2

def pose_classification (list) : 
    print(list)
    result = 'harry'
    return result

def main () :
    #get parameter
    ag = sys.argv[1:]
    result = pose_classification(ag)
    print("result : "+ result)
    return result


if __name__ == "__main__" : 
    main()
    
