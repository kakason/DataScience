from sklearn.model_selection import train_test_split
from sklearn import tree
import data


# for splitting data and target
def split():
    data_part, target_part = data.data_and_target()
    return train_test_split(data_part, target_part, test_size=0.33, random_state=1)


def classify():
    X_train, X_test, y_train, y_test = split()
    clf = tree.DecisionTreeClassifier()
    # for building decision tree
    clf.fit(X_train, y_train)
    # print the accuracy (current accuracy is about 0.15)
    print clf.score(X_test, y_test)
