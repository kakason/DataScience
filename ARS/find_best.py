from sklearn.model_selection import train_test_split
from sklearn import tree
import data


# this function is used to find best combination of features
def get_and_find():
    X, y = data.data_and_target()
    max_num = 0
    current = 0
    for i in range(1, 128):
        new_X = []
        for x in X:
            temp = i
            tmp_list = []
            for j in range(7):
                r = temp % 2
                if r == 1:
                    tmp_list.append(x[j])

                temp /= 2
            new_X.append(tmp_list)

        tmp_res = result(new_X, y)
        if tmp_res > max_num:
            max_num = tmp_res
            current = i

    print "Maximum score is %f" % max_num
    print "The result is from %d" % current


def result(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)
    clf = tree.DecisionTreeClassifier()

    # for building decision tree
    clf.fit(X_train, y_train)

    return clf.score(X_test, y_test)
