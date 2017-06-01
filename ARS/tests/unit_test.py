# Test for loading of .csv

import load_csv


def test_load_fb_pages(a):
    print("Test_load_fb_pages:")
    for i in range(0, 5):
        for j in range(0, 3):
            print a[i][j]  # the Chinese name could be printed correctly


def test_load_fb_users(b):
    print("\nTest_load_fb_users:")
    for i in range(0, 5):
        for j in range(0, 4):
            print b[i][j]


def test_load_fb_user_likes(c):
    print("\nTest_load_fb_user_likes:")
    for i in range(0, 5):
        for j in range(0, 5):
            print c[i][j]


def test_object(a):
    print("\nTest_object:")
    tmp = [load_csv.fb_pages() for x in range(5)]
    for i in range(0, 5):
        tmp[i].id = a[i][0]
        tmp[i].name = a[i][1]
        tmp[i].category = a[i][2]
        print ("%d, %s, %s" % (tmp[i].id, tmp[i].name, tmp[i].category))


def run(a, b, c):
    test_load_fb_pages(a)
    test_load_fb_users(b)
    test_load_fb_user_likes(c)

    test_object(a)
