#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

import xlsxwriter

import xlrd
import csv

import numpy
import pandas
import sklearn.metrics
import sklearn.model_selection
import sklearn.linear_model
import sklearn.preprocessing

def xlsx_to_csv():
    wb = xlrd.open_workbook("ENB2012_data.xlsx")
    sh = wb.sheet_by_index(0)

    fh = open("ENB2012_data.csv", "wb")
    csv_out = csv.writer(fh, quoting=csv.QUOTE_ALL)

    for i in range(0, sh.nrows):
        csv_out.writerow(sh.row_values(i))

    fh.close()


def mean_square_error(diff, n):
    value = numpy.sum(numpy.square(diff))

    return value/float(n)


def load_train_test_data(train_ratio=.5):
    data = pandas.read_csv('./ENB2012_data.csv')

    feature_col = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']
    label_col = ['Y1']
    X = data[feature_col].as_matrix()
    y = data[label_col].as_matrix()

    return sklearn.model_selection.train_test_split(X, y, test_size=1 - train_ratio, random_state=0)


def scale_features(X_train, X_test, low=0, upp=1):
    minmax_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(low, upp)).fit(numpy.vstack((X_train, X_test)))
    X_train_scale = minmax_scaler.transform(X_train)
    X_test_scale = minmax_scaler.transform(X_test)

    return X_train_scale, X_test_scale


def gradient_descent(X, y, alpha=.001, iters=100000, eps=1e-4):
    ## Initialize ##
    converged = False
    k = 0
    n, d = X.shape
    theta = numpy.random.rand(8, 1)
    y_hat = numpy.dot(X, theta)
    error = mean_square_error(y - y_hat, n)

    ## Create a .xlsx file to hold my result ##
    workbook = xlsxwriter.Workbook('result.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "k")
    worksheet.write(0, 1, "cur_error")
    worksheet.write(0, 2, "last_error")
    worksheet.write(0, 3, "error_rate")

    ## Learning ##
    while not converged and k <= iters:
        ## Update theta ##
        J_theta = numpy.dot(numpy.transpose(X), numpy.dot(X, theta) - y)
        theta -= alpha*J_theta

        ## Check if it's converged ##
        mse = mean_square_error(numpy.dot(X, theta) - y, n)
        tmp = abs(error - mse)

        ## Write into the .xlsx file ##
        worksheet.write(k + 1, 0, k)
        worksheet.write(k + 1, 1, mse)
        worksheet.write(k + 1, 2, error)
        worksheet.write(k + 1, 3, tmp)

        if tmp <= eps:
            converged = True
        error = mse
        k += 1

    workbook.close()

    return theta


def predict(X, theta):
    return numpy.dot(X, theta)


def main(argv):
    xlsx_to_csv()

    X_train, X_test, y_train, y_test = load_train_test_data(train_ratio=.5)
    X_train_scale, X_test_scale = scale_features(X_train, X_test, 0, 1)

    theta = gradient_descent(X_train_scale, y_train)

    y_hat = predict(X_train_scale, theta)
    print("Linear train R^2: %f" % (sklearn.metrics.r2_score(y_train, y_hat)))
    y_hat = predict(X_test_scale, theta)
    print("Linear test R^2: %f" % (sklearn.metrics.r2_score(y_test, y_hat)))


if __name__ == "__main__":
    main(sys.argv)
