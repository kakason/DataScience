#!/usr/bin/python
# -*- coding: utf-8 -*-

import load_csv
import translate


def data_and_target():
    data_matrix = []
    user_dict = dict()
    user_X = load_csv.load_fb_users()
    user_len = len(user_X)

    for i in range(user_len):
        tmp_list = []
        for j in range(1, 4):
            if j == 3 and not load_csv.pandas.isnull(user_X[i][j]):
                int_arr = user_X[i][j].split("/")
                tmp_list.append(2017 - int(int_arr[0]))
            else:
                tmp_list.append(user_X[i][j])

        tmp_list.extend([0] * 4)
        tmp_user = user_X[i][0]
        user_dict[tmp_user] = i
        data_matrix.append(tmp_list)

    user_num = len(user_dict)
    user_cat_dict = [dict() for x in range(user_num)]
    likes_ls = [0] * user_num

    for k in range(100):
        print k
        X = load_csv.load_fb_user_likes(k)
        likes_len = len(X)
        for i in range(likes_len):
            user = X[i][0]
            cat = X[i][3]
            if not load_csv.pandas.isnull(cat):
                cat = cat.replace("社區", "社群")
                cat = translate.switch(cat)

            time_str = X[i][4]
            time_str = time_str.split()
            time_str = time_str[1].split(":")
            time = int(time_str[0])
            if user in user_dict:
                index = user_dict[user]
                user_cat_dict[index][cat] = user_cat_dict[index].get(cat, 0) + 1

                likes_ls[index] += 1
                if 6 <= time < 12:
                    data_matrix[index][3] += 1
                elif 12 <= time < 18:
                    data_matrix[index][4] += 1
                elif 18 <= time < 24:
                    data_matrix[index][5] += 1
                else:
                    data_matrix[index][6] += 1

    target_matrix = []
    # backward
    for i in range(user_num - 1, -1, -1):
        if len(user_cat_dict[i]) == 0:
            del data_matrix[i][:]
            del data_matrix[i]
        else:

            for j in range(3, 7):
                data_matrix[i][j] = int(data_matrix[i][j] * 10 / likes_ls[i])
            cat = ""
            num = 0
            for x in user_cat_dict[i]:
                if user_cat_dict[i][x] > num:
                    cat = x
                    num = user_cat_dict[i][x]

            target_matrix.insert(0, cat)

    user_num = len(data_matrix)

    output = open("out.csv", "w")
    output.write("\"gender\",\"location\",\"age\","
                 "\"morning\",\"afternoon\",\"night\",\"midnight\",\"category\"\n")
    for i in range(user_num):
        output.write("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"\n" %
                     (data_matrix[i][0], data_matrix[i][1], data_matrix[i][2], data_matrix[i][3], data_matrix[i][4],
                      data_matrix[i][5], data_matrix[i][6], target_matrix[i]))

    print "done"

    return data_matrix, target_matrix
