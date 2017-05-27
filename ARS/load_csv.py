import pandas
import unit_test


class fb_pages(object):
    def __init__(self):
        self.id = 0
        self.name = 0
        self.category = 0


class fb_users(object):
    def __init__(self):
        self.id = 0  # the id should be independent?
        self.gender = 0
        self.location_name = 0
        self.birthday = 0


# 100(00, 01,... 99) .csv files need to be loaded
class fb_user_likes(object):
    def __init__(self):
        self.user_id = 0  # the user_id should be independent?
        self.page_id = 0
        self.page_name = 0
        self.category = 0
        self.created_time = 0


def load_fb_pages(folder_name):
    data = pandas.read_csv(folder_name + 'facebook_pages.csv')

    feature_col = ['id', 'name', 'category']
    X = data[feature_col].as_matrix()

    return X


def load_fb_users(folder_name):
    data = pandas.read_csv(folder_name + 'facebook_user.csv')

    feature_col = ['id', 'gender', 'location_name', 'birthday']
    X = data[feature_col].as_matrix()

    return X


def load_fb_user_likes(folder_name):
    data = pandas.read_csv(folder_name + 'facebook_user_likes_00.csv')

    feature_col = ['user_id', 'page_id', 'page_name', 'category', 'created_time']
    X = data[feature_col].as_matrix()

    return X


def run():
    folder_name = "./Social_Network_Data/"
    matrix_pages = load_fb_pages(folder_name)
    matrix_users = load_fb_users(folder_name)
    matrix_likes = load_fb_user_likes(folder_name)

    unit_test.run(matrix_pages, matrix_users, matrix_likes)
