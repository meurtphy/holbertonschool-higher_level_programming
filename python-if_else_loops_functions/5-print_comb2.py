#!/usr/bin/python3
for number in range(0, 99):
    print("{:d}".format(number), end=", " if number < 98 else "\n")
