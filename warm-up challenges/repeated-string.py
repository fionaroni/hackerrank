#!/bin/python3


# Complete the repeatedString function below.
def repeatedString(s, n):
    return s.count("a") * (n//len(s)) + s[:n%len(s)].count("a")

