#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

import math
import matplotlib.pyplot as plt
import numpy
import pandas
import sklearn.metrics
import sklearn.model_selection
import sklearn.linear_model
import sklearn.preprocessing

class Pair:
    def __init__(self):
        self.tp = 0
        self.fp = 0

class Data:
    def __init__(self):
        self.predict = 0
        self.expect = 0


def load_train_test_data(train_ratio=.5):
    data = pandas.read_csv('HTRU_2.csv', header=None, names=['x%i' % (i) for i in xrange(8)] + ['y'])
    X = numpy.asarray(data[['x%i' % (i) for i in xrange(8)]])
    y = numpy.asarray(data['y'])

    return sklearn.model_selection.train_test_split(X, y, test_size = 1 - train_ratio, random_state=0)


def scale_features(X_train, X_test, low=0, upp=1):
    minmax_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(low, upp)).fit(numpy.vstack((X_train, X_test)))
    X_train_scale = minmax_scaler.transform(X_train)
    X_test_scale = minmax_scaler.transform(X_test)

    return X_train_scale, X_test_scale


def cross_entropy(y, y_hat):
    loss = 0
    for i in xrange(len(y)):
        loss += -(y[i]*math.log(y_hat[i]) + (1-y[i])*math.log(1-y_hat[i]))

    return loss


def logistic_function(Xi, theta):

    return 1.0/(1 + numpy.exp(-numpy.dot(Xi, theta)))


def logreg_sgd(X, y, alpha = .001, iters = 100000, eps = 0.3):

    n, d = X.shape #(n, d)=(8949,8) y.shape=(8949,)
    theta = numpy.zeros((d, 1))
    y_hat = (1.0 / (1 + numpy.exp(numpy.dot(-X, theta)))).reshape(n)
    converged = False
    k = 0
    error = 0

    while not converged and k <= iters:
        for i in range(n):
            y_hat[i] = logistic_function(X[i], theta)
            L_theta = numpy.dot(X[i], y_hat[i] - y[i])
            theta -= alpha*L_theta.reshape(d, 1)

            # Check if converged #
            if i%2000 == 0:
                cel = cross_entropy(y, y_hat)
                if abs(cel - error) <= eps:
                    print("Finished")
                    print("Last cross entropy loss:", error)
                    print("Current cross entropy loss:", cel)
                    converged = True
                    break
                error = cel
        print("Iteration:", k)
        k += 1

    return theta


def predict_prob(X, theta):

    return 1./(1+numpy.exp(-numpy.dot(X, theta)))


def plot_roc_curve(y_test, y_prob):
    n = len(y_test) #n=8949
    tpr = [0 for x in range(n+1)]
    fpr = [0 for x in range(n+1)]
    tp = 0
    fp = 0
    true_number = 0
    false_number = 0

    tmp = [Data() for x in range(n+1)]
    table = [Pair() for x in range(n+1)]

    table[0].tp = 0
    table[0].fp = 0
    tmp[0].predict = 0
    tmp[0].expect = 0

    for i in range(1, n+1):
        tmp[i].predict = y_prob[i-1]
        tmp[i].expect = y_test[i-1]
        if y_test[i-1] == 1:
            true_number += 1
    false_number = n - true_number #true_number=768

    tmp.sort(key = lambda x:x.predict, reverse = True)

    for i in range(0, n):
        if tmp[i].expect == 1:
            tp += 1
        else:
            fp += 1
        table[i+1].tp = tp
        table[i+1].fp = fp

    for i in range(1, n+1):
        tpr[i] = table[i].tp / true_number
        fpr[i] = table[i].fp / false_number

    plt.plot(fpr, tpr)
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig("roc_curve.png")


def main(argv):
    X_train, X_test, y_train, y_test = load_train_test_data(train_ratio=.5)
    X_train_scale, X_test_scale = scale_features(X_train, X_test, 0, 1)

    theta = logreg_sgd(X_train_scale, y_train)
    print(theta)
    y_prob = predict_prob(X_train_scale, theta)
    print("Logreg train accuracy: %f" % (sklearn.metrics.accuracy_score(y_train, y_prob > .5)))
    y_prob = predict_prob(X_test_scale, theta)
    print("Logreg test accuracy: %f" % (sklearn.metrics.accuracy_score(y_test, y_prob > .5)))
    plot_roc_curve(y_test.flatten(), y_prob.flatten())


if __name__ == "__main__":
    main(sys.argv)


