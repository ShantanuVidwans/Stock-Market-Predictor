import csv

data = list(csv.reader(open("stock.csv", "r+")))
a = [1] * 4
b = [1] * 4
n = 0
cn = 0
j = 0.001
while n < 4000:
    cn = 0
    while cn < 100000:
        b[0] = a[0] * float(data[n][0])
        b[1] = a[1] * float(data[n][1])
        b[2] = a[2] * float(data[n][2])
        b[3] = a[3] * float(data[n][3])
        result = b[0] + b[1] + b[2] + b[3]
        if float(data[n + 1][0]) < result:
            max1 = max(b[0], b[1], b[2], b[3])
            if max1 == b[0]:
                opt = 0
            if max1 == b[1]:
                opt = 1
            if max1 == b[2]:
                opt = 2
            if max1 == b[3]:
                opt = 3
            a[opt] = a[opt] - j
        if float(data[n + 1][0]) > result:
            max1 = min(b[0], b[1], b[2], b[3])
            if max1 == b[0]:
                opt = 0
            if max1 == b[1]:
                opt = 1
            if max1 == b[2]:
                opt = 2
            if max1 == b[3]:
                opt = 3
            a[opt] = a[opt] + j
            cn = cn + 1
    n = n + 1
    print(str(result) + "---" + str(result / float(data[n + 1][0])))
