from sklearn.model_selection import train_test_split
from sklearn import tree
import data


# this function is used to find best combination of features
def get_and_find():
    X, y = data.data_and_target()
    max_num = 0
    current = 0
    flag_list = [0] * 7
    best_list = []
    for i in range(1, 128):
        print i
        new_X = []
        temp = i
        for j in range(7):
            r = temp % 2
            if r == 1:
                flag_list[j] = 1
            else:
                flag_list[j] = 0
            temp /= 2
        for x in X:
            tmp_list = []
            for j in range(7):
                if flag_list[j] == 1:
                    tmp_list.append(x[j])

            new_X.append(tmp_list)
        acc = 0
        for j in range(100):
            acc += result(new_X, y, j)
        tmp_res = acc / 10
        if tmp_res > max_num:
            max_num = tmp_res
            current = i
            best_list = list(flag_list)

    print "Maximum score is %f" % max_num
    print "The result is from %d" % current
    print best_list


def result(X, y, ran):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=ran)
    clf = tree.DecisionTreeClassifier()

    # for building decision tree
    clf.fit(X_train, y_train)

    return clf.score(X_test, y_test)
