"""
    Logistic Regression with Stochastic Gradient Descent.
    Copyright (c) 2009, Naoaki Okazaki
"""
import collections
import math
import pickle

N = 10662  # Change this to present the number of training instances.
eta0 = 0.1  # Initial learning rate; change this if desired.
epoch = 10


def update(W, X, l, eta):
    # Compute the inner product of features and their weights.
    a = sum([W[x] for x in X])

    # Compute the gradient of the error function (avoiding +Inf overflow).
    g = ((1. / (1. + math.exp(-a))) - l) if -100. < a else (0. - l)

    # Update the feature weights by Stochastic Gradient Descent.
    for x in X:
        W[x] -= eta * g


def train(fi: list, epoch: int, eta0: float) -> dict:
    t = 1
    W = collections.defaultdict(float)
    # Loop for instances.
    for i in range(epoch):
        for line in fi:
            fields = line.strip('\n').split(' ')
            if fields[0] == '1':
                update(W, fields[1:], float(1), eta0 / (1 + t / float(N)))
            else:
                update(W, fields[1:], float(0), eta0 / (1 + t / float(N)))
            t += 1
        # print(W)
    return W


if __name__ == '__main__':
    with open('features_mod.txt', 'r') as f:
        fi = f.readlines()

    s = train(fi, epoch, eta0)
    pickle.dump(s, open('nlp73_pickle', 'wb'))
