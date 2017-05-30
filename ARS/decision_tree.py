from sklearn.model_selection import train_test_split
from sklearn import tree
import pydotplus
import data


# for splitting data and target
def split():
    data_part, target_part = data.data_and_target()
    # train:test is 1:1
    return train_test_split(data_part, target_part, test_size=0.5, random_state=1)


def classify():
    X_train, X_test, y_train, y_test = split()
    clf = tree.DecisionTreeClassifier()
    # for building decision tree
    clf.fit(X_train, y_train)
    # print the accuracy (current accuracy is about 0.18)
    print clf.score(X_test, y_test)

    # output decision tree
    dot_data = tree.export_graphviz(clf, out_file=None)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("tree.pdf")
