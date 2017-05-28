import pandas
import statistics



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


def load_fb_pages():
    data = pandas.read_csv(folder_name + 'facebook_pages.csv')

    feature_col = ['id', 'name', 'category']
    X = data[feature_col].as_matrix()

    return X


def load_fb_users():
    data = pandas.read_csv(folder_name + 'facebook_user.csv')

    feature_col = ['id', 'gender', 'location_name', 'birthday']
    X = data[feature_col].as_matrix()

    return X

fff776288aa24d426d85be28c756b53f5a9c1ee7

def load_fb_user_likes(i):
    if i < 10:
        string = "0" + str(i)
    else:
        string = str(i)
    data = pandas.read_csv(folder_name + 'facebook_user_likes_' + string + '.csv')

version_1

def run():
    matrix_pages = load_fb_pages()
    matrix_users = load_fb_users()
fff776288aa24d426d85be28c756b53f5a9c1ee7
    matrix_likes = load_fb_user_likes(0)

version_1

    '''
    users_hobby can be used to build decision tree
    it is an 2 * n array, n is the amount of id
    the first row is user id, the second row is the user's hobby
    '''
    users_hobby = load_fb_user_likes()

    #unit_test.run(matrix_pages, matrix_users, matrix_likes)


    folder_name = "./Social_Network_Data/"
