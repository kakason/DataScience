#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import load_csv


def count():
    matrix = []
    user_dict = {}
    user_X = load_csv.load_fb_users()
    user_len = len(user_X)

    for i in range(user_len):
        tmp_list = []
        for j in range(4):
            if j == 3 and not load_csv.pandas.isnull(user_X[i][j]):
                int_arr = user_X[i][j].split("/")
                tmp_list.append(2017 - int(int_arr[0]))
            else:
                tmp_list.append(user_X[i][j])

        tmp_list.extend([0] * 4)
        temp = user_X[i][0]
        user_dict[temp] = i
        matrix.append(tmp_list)

    user_num = len(user_dict)
    cat_arr = [dict() for x in range(user_num)]

    for k in range(100):
        print k
        X = load_csv.load_fb_user_likes(k)
        likes_len = len(X)
        for i in range(likes_len):
            user = X[i][0]
            cat = X[i][3]
            time_str = X[i][4]
            time_arr = re.split("[: ]", time_str)
            time = int(time_arr[1])
            if user in user_dict:
                index = user_dict[user]
                if cat in cat_arr[index]:
                    cat_arr[index][cat] += 1
                else:
                    cat_arr[index][cat] = 1

                if 6 <= time < 12:
                    matrix[index][4] += 1
                elif 12 <= time < 18:
                    matrix[index][5] += 1
                elif 18 <= time < 24:
                    matrix[index][6] += 1
                else:
                    matrix[index][7] += 1

    for i in range(user_num):
        if len(cat_arr[i]) == 0:
            matrix[i].append("nan")
        else:
            cat = ""
            num = 0
            for x in cat_arr[i]:
                if cat_arr[i][x] > num:
                    cat = x
                    num = cat_arr[i][x]

            matrix[i].append(cat)

    output = open("out.csv", "w")
    output.write("\"id\",\"gender\",\"location\",\"age\","
                 "\"morning\",\"afternoon\",\"night\",\"midnight\",\"category\"\n")
    for i in range(user_num):
        output.write("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"\n" %
                     (matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3], matrix[i][4],
                      matrix[i][5], matrix[i][6], matrix[i][7], matrix[i][8]))

    print "done"
