"""
================================
Nearest Neighbors Classification
================================

"""

import sys
import numpy as np
from sklearn import neighbors, datasets

if __name__=="__main__":

    testset_name=sys.argv[1]
    n_neighbors = 15
    # import some data to play with

    ftrain_val =  open(('../data/{0}/TrainData.txt').format(testset_name))

    # extracting the values from the file for training data 
    X = []
    for train_sample in ftrain_val:
        temparray= np.array([float(x) for x in train_sample.split('\t')])
        X.append(temparray) 

    X = np.array(X)

    ftar_val =  open(('../data/{0}/TrainLabel.txt').format(testset_name))


    # extracting the values from the file for target training data 

    y = np.array([int(tar_sample.strip()) for tar_sample in ftar_val]) 

    ftest_val =  open(('../data/{0}/TestData.txt').format(testset_name))



    # extracting the values from the file for testing data 

    XX = []
    for test_sample in ftest_val:
        temparray= np.array([float(x) for x in test_sample.split('\t')])
        XX.append(temparray) 

    # avoid this ugly slicing by using a two-dim dataset

    h = .02  # step size in the mesh

    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        clf.fit(X, y)

        Z = clf.predict(XX)
        print Z

