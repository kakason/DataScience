import math

class Data:
    def __init__(self, str):
        self.sl = str[0]
        self.sw = str[1]
        self.pl = str[2]
        self.pw = str[3]
        self.attr = str[4]

class Pair:
    def __init__(self):
        self.dis = 0
        self.attr = 0

# The Euclidean distance
def EuclideanDis(a, b):
    value = math.pow(float(a.sl) - float(b.sl), 2) + \
            math.pow(float(a.sw) - float(b.sw), 2) + \
            math.pow(float(a.pl) - float(b.pl), 2) + \
            math.pow(float(a.pw) - float(b.pw), 2)
    return value

inData = []
inTmp = []
disTmp = [[Pair() for x in range(75)] for y in range(150)] # 150x75
outData = [[0 for x in range(20)] for y in range(150)] # 150X20

# Read the file
with open("data.txt") as file:
    for line in file:
        line = line.strip()
        inTmp.append(line.split(','))
        inData.append(0)

# Split the data into 2 parts
for i in range(0, 25):
    inData[i] = Data(inTmp[i])
    inData[i+25] = Data(inTmp[i+50])
    inData[i+50] = Data(inTmp[i+100])

    inData[i+75] = Data(inTmp[i+25])
    inData[i+100] = Data(inTmp[i+75])
    inData[i+125] = Data(inTmp[i+125])

# Calculate the L2 distance
for i in range(0, 150):
    for j in range(0, 75):
        disTmp[i][j].dis = EuclideanDis(inData[i], inData[j])
        disTmp[i][j].attr = inData[j].attr

# Sort the dis in ascending order of each row
for i in range(0, 150):
    disTmp[i].sort(key = lambda x:x.dis)

# Algorithm: K-nearest-neighbors
for i in range(0, 20):
    for j in range(0, 150):
        a, b, c = 0, 0, 0
        for k in range(0, i + 1):
            if disTmp[j][k].attr == 'Iris-setosa':
                a += 1
            elif disTmp[j][k].attr == 'Iris-versicolor':
                b += 1
            else:
                c += 1
        if a >= b:
            if a >= c:
                cla = 'Iris-setosa'
            else:
                cla= 'Iris-virginica'
        else:
            if b >= c:
                cla= 'Iris-versicolor'
            else:
                cla= 'Iris-virginica'

        outData[j][i] = cla

# Analyze the training error and testing error
for i in range(0, 20):
    err_train, err_test = 0, 0
    for j in range(0, 150):
        if outData[j][i] != inData[j].attr:
            if j < 75:
                err_train += 1
            else:
                err_test += 1
    print (i+1, err_train , err_test)
