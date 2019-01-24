#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    for num in list(set(ar)): # get unique nums in ar
        pairs += ar.count(num)//2
    return pairs


arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]