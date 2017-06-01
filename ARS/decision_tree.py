from sklearn.model_selection import train_test_split
from sklearn import tree
import pydotplus
import data


# for splitting data and target
def split():
    data_part, target_part = data.data_and_target()

    # use gender, afternoon,and night only
    for x in data_part:
        del x[6:7]
        del x[1:4]

    # train:test is 1:1
    return train_test_split(data_part, target_part, test_size=0.5, random_state=1)


def classify():
    X_train, X_test, y_train, y_test = split()
    clf = tree.DecisionTreeClassifier()

    # for building decision tree
    clf.fit(X_train, y_train)

    # print the accuracy (current accuracy is about 0.319)
    print clf.score(X_test, y_test)

    # sample prediction
    out = clf.predict([[0, 0, 0], [0, 0, 5], [0, 0, 10], [0, 5, 0], [0, 5, 5], [0, 10, 0],
                       [1, 0, 0], [1, 0, 5], [1, 0, 10], [1, 5, 0], [1, 5, 5], [1, 10, 0]])
    for x in out:
        print x


'''
    # output decision tree
    dot_data = tree.export_graphviz(clf, out_file=None)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("tree.pdf")
'''
