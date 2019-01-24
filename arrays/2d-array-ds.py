#!/bin/python3

# Complete the hourglassSum function below.
def hourglassSum(arr):
    print(arr)
    sums = []
    seed = [0,0]
    x, y, z = 0, 3, 1
    while seed[1] < 4: # traversal across
        seed[0] = 0 # before traversing down, reset first element to 0
        while seed[0] < 4: # traversal downward
            print(seed)
            # calculate hourglass
            hourglass = sum(arr[seed[0]][x:y]) + arr[seed[0]+1][z] + sum(arr[seed[0]+2][x:y])
            print(hourglass)
            seed[0] += 1 
            sums.append(hourglass)
        seed[1] += 1
        x += 1
        y += 1
        z += 1
    return max(sums)