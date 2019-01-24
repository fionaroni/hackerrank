#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/bin/python3


# Complete the countingValleys function below.
def countingValleys(n, s):
    num_valleys, elevation = 0, 0
    for i in s:
        if i == "D":
            elevation -= 1
        else: # i == "U"
            elevation += 1
            if elevation == 0:
                num_valleys += 1
    return num_valleys

