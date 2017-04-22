"""
    Logistic Regression with Stochastic Gradient Descent.
    Copyright (c) 2009, Naoaki Okazaki
"""
import collections
import math

N = 10662  # Change this to present the number of training instances.
eta0 = 0.1  # Initial learning rate; change this if desired.


def update(W, X, l, eta):
    # Compute the inner product of features and their weights.
    a = sum([W[x] for x in X])

    # Compute the gradient of the error function (avoiding +Inf overflow).
    g = ((1. / (1. + math.exp(-a))) - l) if -100. < a else (0. - l)

    # Update the feature weights by Stochastic Gradient Descent.
    for x in X:
        W[x] -= eta * g


def train(fi):
    t = 1
    W = collections.defaultdict(float)
    # Loop for instances.
    for line in fi:
        fields = line.strip('\n').split(' ')
        update(W, fields[1:], float(fields[0]), eta0 / (1 + t / float(N)))
        t += 1
    return W


if __name__ == '__main__':
    with open('features_mod.txt', 'r') as f:
        fi = f.read()

    for i in range(10):
        train(fi)
