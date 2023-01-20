#!/usr/bin/python3
for i in range(10):
    for i2 in range(i + 1, 10):
        if i < 8 :
            print("{:02d}".format(i * 10 + i2), end =", ")
        else :
            print("{:02d}".format(i * 10 + i2), end ="\n")
