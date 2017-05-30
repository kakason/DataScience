#!/usr/bin/python
# -*- coding: utf-8 -*-

import load_csv
import translate
import hobby_merge


def time_processing(s):
    s = s.split()
    s = s[1].split(":")

    return int(s[0])


def output_csv_file(num, data, target):
    output = open("result.csv", "w")
    output.write("\"gender\",\"location\",\"age\","
                 "\"morning\",\"afternoon\",\"night\",\"midnight\",\"category\"\n")
    for i in range(num):
        output.write("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"\n" %
                     (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                      data[i][5], data[i][6], target[i]))

    print "Data matrix and target matrix have completed"


def data_and_target():
    data_matrix = []
    user_dict = dict()

    # load fb user's information
    user_X = load_csv.load_fb_users()
    user_len = len(user_X)

    for i in range(user_len):
        tmp_list = []

        # gender
        tmp_list.append(translate.gender_trans(user_X[i][1]))

        # location
        tmp_list.append(translate.loc_trans(user_X[i][2]))

        # age
        tmp_list.append(translate.age_trans(user_X[i][3]))

        tmp_list.extend([0] * 4)
        tmp_user = user_X[i][0]
        user_dict[tmp_user] = i
        data_matrix.append(tmp_list)

    user_num = len(user_dict)

    # create category dictionary for each user
    user_cat_dict = [dict() for x in range(user_num)]

    # list used to count total likes for each user
    likes_ls = [0] * user_num

    for k in range(100):
        print(k)
        X = load_csv.load_fb_user_likes(k)
        likes_len = len(X)

        for i in range(likes_len):
            user = X[i][0]
            cat = X[i][3]
            if not load_csv.pandas.isnull(cat):
                # fix common errors
                cat = cat.replace("社區", "社群")
                cat = translate.cat_trans(cat)
                cat = hobby_merge.is_hobby(cat)

            # time process
            time = time_processing(X[i][4])
            if user in user_dict:
                index = user_dict[user]
                if cat != "not_a_hobby":
                    user_cat_dict[index][cat] = user_cat_dict[index].get(cat, 0) + 1

                likes_ls[index] += 1

                # morning
                if 6 <= time < 12:
                    data_matrix[index][3] += 1
                # afternoon
                elif 12 <= time < 18:
                    data_matrix[index][4] += 1
                # night
                elif 18 <= time < 24:
                    data_matrix[index][5] += 1
                # midnight
                else:
                    data_matrix[index][6] += 1

    target_matrix = []
    # backward
    for i in range(user_num - 1, -1, -1):
        # if no target
        if len(user_cat_dict[i]) == 0:
            # delete useless data
            del data_matrix[i][:]
            del data_matrix[i]
        else:
            # calculate percentage for each time interval (result is 0 ~ 10)
            for j in range(3, 7):
                data_matrix[i][j] = int(data_matrix[i][j] * 10 / likes_ls[i])
            cat = ""
            num = 0
            # calculate most favorite category for each user
            for x in user_cat_dict[i]:
                if user_cat_dict[i][x] > num:
                    cat = x
                    num = user_cat_dict[i][x]

            target_matrix.insert(0, cat)

    output_csv_file(len(data_matrix), data_matrix, target_matrix)

    return data_matrix, target_matrix