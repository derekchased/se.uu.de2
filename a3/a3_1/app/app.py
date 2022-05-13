# from collections import Counter
# import socket
# import time

# def f():
#     time.sleep(0.001)
#     # Return IP address.
#     return socket.gethostbyname(socket.gethostname())

# ip_addresses = [f() for _ in range(100)]
# print(Counter(ip_addresses))



from sklearn.ensemble import RandomForestClassifier
import numpy as np
from numpy import loadtxt
from numpy.random import default_rng
from sklearn.model_selection import cross_val_score

import ray
from tune_sklearn import TuneGridSearchCV

print(ray.init("localhost:6379"))

print(f"Nodes\n{ray.nodes()}\n")

# Load Data
train_data = loadtxt("train.csv",delimiter=',', skiprows=1)
# test_data = loadtxt("test.csv",delimiter=',', skiprows=1)

# Shuffle Data
train_data_shuffled = train_data[ default_rng().permutation(train_data.shape[0]) ]

# Separate train and labels
X_train = train_data[:,:-1]
y_train = train_data[:,-1]



# print(f"\nRandomForestClassifier Default\nAccuracy: {classifier.score(X_train, y_train)}")

classifier = RandomForestClassifier()

params = {"max_depth":np.arange(5,20,1), "n_estimators":np.arange(5,20,1), "ccp_alpha":[0,.1,1]}
print(f"\nRandomForestClassifier Params\n{params}")

gcv = TuneGridSearchCV(classifier, params)
gcv.fit(X_train, y_train)

print(f"\nRandomForestClassifier Tuned\nCrossval Score: {gcv.best_score_}, Accuracy: {gcv.score(X_train, y_train)}, Best Params:\n{gcv.best_params_}")

classifier = RandomForestClassifier()

print(f"Cross Val Score, default: {cross_val_score(classifier, X_train, y_train, cv=5)}")


