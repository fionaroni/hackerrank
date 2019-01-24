#!/bin/python3


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current_place, num_steps = 0, 0
    while current_place != len(c)-1: # index of curr place is <= index of last cloud
        if current_place + 2 > len(c)-1 or c[current_place+2] == 1: # distance 2 is beyond index of last cloud // thunderstorm
            current_place += 1 # default to 1 step // avoid 2, advance 1
        else: # cumulus
            current_place += 2 # advance 2
        num_steps += 1 # regardless of distance 1 or 2, add 1 step
    return num_steps