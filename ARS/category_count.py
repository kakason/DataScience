import load_csv


# for testing
def count():
    cat_dict = dict()

    for k in range(100):
        print k
        cat_X = load_csv.load_fb_user_likes(k)
        cat_len = len(cat_X)
        for i in range(cat_len):
            cat = cat_X[i][3]
            if not load_csv.pandas.isnull(cat):
                cat = cat.lower()
            cat_dict[cat] = cat_dict.get(cat, 0) + 1

    output = open("category.txt", "w")
    c = 0
    for x in cat_dict:
        if not load_csv.pandas.isnull(x) and 'a' <= x[0] <= 'z' and cat_dict[x] >= 10:
            output.write("%s\n" % x)
            c += 1

    output.write("%s\n" % c)

    c = 0
    for x in cat_dict:
        if not load_csv.pandas.isnull(x) and not 'a' <= x[0] <= 'z' and cat_dict[x] >= 10:
            output.write("%s\n" % x)
            c += 1

    output.write("%s\n" % c)
