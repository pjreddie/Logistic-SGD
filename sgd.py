from math import exp
import random
from data import load_adult_train_data

# TODO: Calculate logistic
def logistic(x):
    return 1.

# TODO: Calculate dot product of two lists
def dot(x, y):
    s = 0
    return s

# TODO: Calculate prediction based on model
def predict(model, point):
    return 0

# TODO: Update model using learning rate and L2 regularization
def update(model, point, delta, rate, lam):
    pass

def initialize_model(k):
    return [random.gauss(0, 1) for x in range(k)]

# TODO: Train model using training data
def train(data, epochs, rate, lam):
    model = initialize_model(len(data[0]['features']))
    return model
        
def submission(data):
    return train(data, 1, .01, 0)
    
# TODO: Calculate accuracy of predictions on data
def accuracy(data, predictions):
    correct = 0
    return float(correct)/len(data)


